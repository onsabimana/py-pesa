import re
from dateutil.parser import parse
import datetime

example ='''Z10DN636 Confirmed.
You have received Tsh50,000 from
FREDRICK KIMARO
on 27/1/14 at 1:19 PM
New M-PESA balance is Tsh214,676'''

example2 ='X89IQ877 Confirmed. Tsh2,100 sent to MUSHI WILLIAM on 15/12/13 at 10:19 PM. New M-PESA balance is Tsh23,232.'

example3 ='''Z92FP098 confirmed. You bought Tsh3,500 of airtime on 22/2/14 at 8:12 PM
New M-PESA balance is Tsh2,720'''

example4='''Y24KU015 confirmed. You bought Tsh501 of airtime for 0765567959 on 1/1/14 at 10:09 PM
New M-PESA balance is Tsh1,430'''

example5 ='''Z15EE301 Confirmed. Tsh212,000 sent to business Bank for account ACB-11567341482 on 28/1/14 at 11:30 PM
New M-PESA balance is Tsh225.'''

example6 = 'BA35RS735 Confirmed. on 8/3/14 at 4:59 PM Give Tsh10,000 cash to Hilda Joseph Mushi New M-PESA balance is Tsh10,015'

example7 ='''BA35RT157 Confirmed.
on 8/3/14 at 5:19 PM
Withdraw Tsh6,000 from
128137 - EMANUEL SHANI
New M-PESA balance is Tsh3,415'''
example8='''BB43UB521 Confirmed. Your M-PESA balance was Tsh2,354
on 8/3/14 at 5:26 PM.'''
#-----------------------------------------------------START COMMON FUNCTIONS-----------------------------------------------------------------

# function to check which type of sms
def checkTypeOfSMS(word, str):
    if word in str:
        return True
    else:
        return False
#extract and format date in the string
def extractDate(str):
	words = str.split()
	datepart =''
	timepart =''
	timepart2 =''
	errorReturn='Error parsing date!'
	for word in words:
		if '/' in word:
			datepart = word
		elif ':' in word: 
			timepart = word
		elif (word=='PM') or (word=='AM') or (word=='PM.') or (word=='AM.'):
			timepart2 = word
	fulldate = datepart + ' ' + timepart+' '+timepart2
	try:
		fulldate = parse(fulldate,fuzzy=True)
		fulldate = fulldate.strftime("%d-%m-%Y %H:%M:%S")
	except ValueError:
		return errorReturn
	return fulldate
#-----------------------------------------------------END COMMON FUNCTIONS-----------------------------------------------------------------

#-----------------------------------------------------START SMS TRANSACTION FUNCTIONS-----------------------------------------------------------------

def computeTanzMPesa(str):
    lisfOfActualMatchs = [];
    transactionDetails = []
    regex = ''

    # Return is a array list of the following values
    # 0 - TransactionNo
    transactionNo = ''

    # 1 - Amount
    amount = ''

    # 2 - Sender
    sender =''

    # 3 - Reciever
    reciever = ''

    # 4 - Timestamp
    timestamp =''

    # 5 - Balance
    balance = ''
    transactionType =''

    if checkTypeOfSMS('received',str) == True:       #check if this is for M-PESA recieved transaction
        regex =r"([A-Z0-9]+\s+Confirmed.)|(received\s+Tsh\d+,\d+|Tsh\d+)|(from\s+(.+?)\s+?on)|(\d{2}\/\d\/\d{2}\s+at\s+\d:\d{2}\s+(PM|AM))|(balance\s+is\s+Tsh\d+,\d+|Tsh\d+)"
    elif (checkTypeOfSMS('sent',str) ==True) and (checkTypeOfSMS('business',str) ==False):
        regex = r"([A-Z0-9]+\s+Confirmed.)|(\s+Tsh\d+,\d+|Tsh\d+)|(sent\s+(.+?)\s+?on)|(\d{2}\/\d{2}\/\d{2}\s+at\s+\d{2}:\d{2}\s+(PM|AM))|(balance\s+is\s+Tsh\d+,\d+|Tsh\d+)"
    elif (checkTypeOfSMS('airtime on',str) == True) and (checkTypeOfSMS('bought',str)==True):
        regex = r"([A-Z0-9]+\s+confirmed.|[A-Z0-9]+\s+Confirmed.)|(bought\s+Tsh\d+,\d+|Tsh\d+)|(from\s+(.+?)\s+?on)|(\d{2}\/\d\/\d{2}\s+at\s+\d:\d{2}\s+(PM|AM))|(balance\s+is\s+Tsh\d+,\d+|Tsh\d+)"
    elif (checkTypeOfSMS('airtime for',str) == True) and (checkTypeOfSMS('bought', str)==True):
        regex=r"([A-Z0-9]+\s+confirmed.|[A-Z0-9]+\s+Confirmed.)|(bought\s+Tsh\d+,\d+|Tsh\d+)|(for\s+(.+?)\s+?on)|(\d{2}\/\d\/\d{2}|\d\/\d\/\d{2}\s+at\s+\d{2}:\d{2}\s+(PM|AM)|\s+\d:\d\s+(PM|AM))|(balance\s+is\s+Tsh\d+,\d+|Tsh\d+)"
    elif checkTypeOfSMS('sent to business', str) == True:
        regex = r"([A-Z0-9]+\s+Confirmed.)|(Tsh\d+,\d+)|(for account\s+(.+?)\s+?on)|(business Bank)|(\d{2}\/\d\/\d{2}\s+at\s+\d:\d{2}\s+(PM|AM))|(balance\s+is\s+(Tsh\d+,\d+|Tsh\d+))"
    elif checkTypeOfSMS('Give',str) == True:
        regex = r"([A-Z0-9]+\s+Confirmed.)|(Give\s+Tsh\d+,\d+)|(to\s+(.+?)\s+?New)|(balance\s+is\s+(Tsh\d+,\d+|Tsh\d+))"
    elif checkTypeOfSMS('Withdraw',str) == True:
        regex = r"([A-Z0-9]+\s+Confirmed.)|(Withdraw\s+Tsh\d+,\d+)|(from\s+(.+?)\s+?New)|(balance\s+is\s+(Tsh\d+,\d+|Tsh\d+))"
    elif checkTypeOfSMS('Your M-PESA',str) == True:
        regex = r"([A-Z0-9]+\s+Confirmed.)|(balance\s+was\s+(Tsh\d+,\d+|Tsh\d+))"
    else:
        print("Wrong function for this transaction!")

    # Extract required matches from the regular expression results
    matches = re.finditer(regex, str)
    for matchNum, match in enumerate(matches):
        if match.group(0):
            lisfOfActualMatchs.append(match.group(0))
        else:
            print('it did not work')

    # Final extraction of required transaction details:
    if checkTypeOfSMS('received',str) ==True:

        # Extract transaction number
        transactionNo =lisfOfActualMatchs[0].split()[0]

        # Extract Amount
        amount = lisfOfActualMatchs[1].split()[1]

        # Extract sender
        sender = lisfOfActualMatchs[2].split()
        sender = " ".join(sender[1:3])

        # Extract timestamp
        timestamp = extractDate(str)

        # Extract balance
        balance = lisfOfActualMatchs[4].split()[2]

    elif (checkTypeOfSMS('sent',str) ==True) and (checkTypeOfSMS('business',str) ==False):
        # Extract transaction number
        transactionNo = lisfOfActualMatchs[0].split()[0]

        # Extract Amount
        amount = lisfOfActualMatchs[1]

        # Extract sender
        reciever = lisfOfActualMatchs[2].split()
        reciever = " ".join(reciever[2:4])

        # Extract timestamp
        timestamp = extractDate(str)

        # Extract balance
        balance = lisfOfActualMatchs[4].split()[2]

    elif (checkTypeOfSMS('airtime on',str) ==True) and (checkTypeOfSMS('bought',str)==True):
        #transactionAndAmountStr, _ , timestampStr, balanceStr = [elemet.split() for element in listOfActualMatchs]

        # Extract transaction number
        transactionNo=lisfOfActualMatchs[0].split()[0]

        # Extract Amount
        amount = lisfOfActualMatchs[1].split()[1]
		
        # Extract timestamp
        timestamp = extractDate(str)
		
        # Extract balance
        balance = lisfOfActualMatchs[3].split()[2]

    elif (checkTypeOfSMS('airtime for',str) ==True) and (checkTypeOfSMS('bought',str)==True):
        transactionNoStr, amountStr, receiverStr, timestampStr, balanceStr = [e.split() for e in lisfOfActualMatchs]

        # Extract transaction number
        transactionNo=lisfOfActualMatchs[0].split()[0]

        # Extract Amount
        amount = lisfOfActualMatchs[1]
		
        # Extract reciever
        reciever = lisfOfActualMatchs[2].split()[1]

        # Extract timestamp
        timestamp = extractDate(str)
		
        # Extract balance
        balance = lisfOfActualMatchs[4].split()[2]

    elif checkTypeOfSMS('sent to business', str):
		#transactionNo, amount, receiver, timestamp, balance = [e.split() for e in lisfOfActualMatchs]
		# Extract transaction number
        transactionNo=lisfOfActualMatchs[0].split()
        transactionNo = transactionNo[0]
		
		# Extract Amount
        amount=lisfOfActualMatchs[1]
		
		# Extract sender
        sender = lisfOfActualMatchs[3].split()[2]
		
		# Extract reciever
        reciever = lisfOfActualMatchs[2]
		
		# Extract timestamp
        timestamp = extractDate(str)
		
		# Extract balance
        balance = lisfOfActualMatchs[4].split()[2]
        
    elif checkTypeOfSMS('Give', str):
        # Extract transaction number
        transactionNo=lisfOfActualMatchs[0].split()[0]
       
        # Extract Amount
        amount=lisfOfActualMatchs[1].split()[1]

        # Extract reciever
        reciever = re.search('to\s(.+?)\sNew', str)  #Extract the characters after "to" and space and before space and "on"
        reciever = reciever.group(1)

        # Extract timestamp
        timestamp = extractDate(str)

        # Extract balance
        balance = lisfOfActualMatchs[3].split()[2]
	# elif checkTypeOfSMS('Withdraw',str) == True:
	# 	# Extract transaction number
     #    transactionNo=lisfOfActualMatchs[0].split()[0]
    elif checkTypeOfSMS('Withdraw', str):
        # Extract transaction number
        transactionNo = lisfOfActualMatchs[0].split()[0]

        # Extract Amount
        amount = lisfOfActualMatchs[1].split()[1]

        # Extract reciever
        reciever = re.search('from\s(.+?)\sNew',
                             str)  # Extract the characters after "to" and space and before space and "on"
        reciever = reciever.group(1)

        # Extract timestamp
        timestamp = extractDate(str)

        # Extract balance
        balance = lisfOfActualMatchs[3].split()[2]
    elif checkTypeOfSMS('Your M-PESA', str):
        # Extract transaction number
        transactionNo = lisfOfActualMatchs[0].split()[0]

        # Extract timestamp
        timestamp = extractDate(str)

        # Extract balance
        balance = lisfOfActualMatchs[1].split()[2]
    else:
        print("No match")
	
    #All the transactions details to the final list
    transactionDetails.append(transactionNo)    # add transaction number

    transactionDetails.append(amount)    # add amount

    transactionDetails.append(sender)    # add sender
	
    transactionDetails.append(reciever)    # add reciever
	
    transactionDetails.append(timestamp)    # add timestamp
	
    transactionDetails.append(balance)    # add balance

    return transactionDetails

print(computeTanzMPesa(example8))
