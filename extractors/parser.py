import re

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

#regex =r"([A-Z0-9]+\s+Confirmed.)|(received\s+Tsh\d+,\d+)|(from\s+(.+?)\s+?on)|(\d{2}\/\d\/\d{2}\s+at\s+\d:\d{2}\s+(PM|AM))|(balance\s+is\s+Tsh\d+,\d+)"
#matches = re.finditer(regex, example)


#-----------------------------------------------------START COMMON FUNCTIONS-----------------------------------------------------------------

# function to check which type of sms
def checkTypeOfSMS(word, str):
    if word in str:
        return True
    else:
        return False
#-----------------------------------------------------END COMMON FUNCTIONS-----------------------------------------------------------------

#-----------------------------------------------------START SMS TRANSACTION FUNCTIONS-----------------------------------------------------------------

def recievedMPesa(str):
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
    elif checkTypeOfSMS('fdhgfhgfhgfh',str) == True and len(str):
        regex = r"([A-Z0-9]+\s+Confirmed.)|(\s+Tsh\d+,\d+|Tsh\d+)|(sent\s+(.+?)\s+?on)|(\d{2}\/\d{2}\/\d{2}\s+at\s+\d{2}:\d{2}\s+(PM|AM))|(balance\s+is\s+Tsh\d+,\d+|Tsh\d+)"
    elif checkTypeOfSMS('airtime on',str) == True and checkTypeOfSMS('bought',str):
        regex = r"([A-Z0-9]+\s+confirmed.|[A-Z0-9]+\s+Confirmed.)|(bought\s+Tsh\d+,\d+|Tsh\d+)|(from\s+(.+?)\s+?on)|(\d{2}\/\d\/\d{2}\s+at\s+\d:\d{2}\s+(PM|AM))|(balance\s+is\s+Tsh\d+,\d+|Tsh\d+)"
    elif checkTypeOfSMS('airtime for',str) == True  and checkTypeOfSMS('bought', str):
        regex=r"([A-Z0-9]+\s+confirmed.|[A-Z0-9]+\s+Confirmed.)|(bought\s+Tsh\d+,\d+|Tsh\d+)|(for\s+(.+?)\s+?on)|(\d{2}\/\d\/\d{2}|\d\/\d\/\d{2}\s+at\s+\d{2}:\d{2}\s+(PM|AM)|\s+\d:\d\s+(PM|AM))|(balance\s+is\s+Tsh\d+,\d+|Tsh\d+)"
    elif checkTypeOfSMS('sent to business', str) == True:
        regex = r"([A-Z0-9]+\s+confirmed.|[A-Z0-9]+\s+Confirmed.)|(Tsh\d+,\d+|Tsh\d+)|(for account\s+(.+?)\s+?on)|(\d{2}\/\d\/\d{2}\s+at\s+\d{2}:\d{2}\s+(PM|AM)|\d\/\d\/\d{2}\s+at\s+\d{2}:\d{2}\s+(PM|AM)|\s+\d:\d\s+(PM|AM))|(balance\s+is\s+Tsh\d+,\d+|balance\s+is\s+Tsh\d+)"
    elif checkTypeOfSMS('Give',str) == True:
        regex ="([A-Z0-9]+\s+confirmed.|[A-Z0-9]+\s+Confirmed.)|(on\s+\d{2}\/\d\/\d{2}\s+at\s+\d{2}:\d{2}\s+(PM|AM)|on\s+\d\/\d\/\d{2}\s+at\s+\d:\d{2}\s+PM|AM)"
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
        transactionNo =lisfOfActualMatchs[0].split()
        transactionNo = transactionNo[0]

        # Extract Amount
        amount = lisfOfActualMatchs[1].split()
        amount = amount[1]

        # Extract sender
        sender = lisfOfActualMatchs[2].split()
        sender = " ".join(sender[1:3])

        # Extract timestamp
        timestamp = lisfOfActualMatchs[3].split()
        timestamp = " ".join(timestamp[0] + timestamp[2:4])

        # Extract timestamp
        balance = lisfOfActualMatchs[4].split()[2]

    elif len(str) and checkTypeOfSMS('fsfdsfdsf', str):
        # Extract transaction number
        transactionNo = lisfOfActualMatchs[0].split()[0]

        # Extract Amount
        amount = lisfOfActualMatchs[1]

        # Extract sender
        reciever = lisfOfActualMatchs[2].split()
        reciever = " ".join(reciever[2:4])

        # Extract timestamp
        timestamp = lisfOfActualMatchs[3].split()
        timestamp = " ".join(timestamp[0] + timestamp[2:4])

        # Extract timestamp
        balance = lisfOfActualMatchs[4].split()[2]

    elif checkTypeOfSMS('airtime on', str) and checkTypeOfSMS('bought', str):
        transactionAndAmountStr, _ , timestampStr, balanceStr = [elemet.split() for element in listOfActualMatchs]

        # Extract transaction number
        transactionNo, amount = transactionAndAmountStr[0], transactionAndAmountStr[1]

        # Extract timestamp
        timestamp = " ".join(timestamp[0] + timestamp[2:4])

        # Extract balance
        balance = balanceStr[2]

    elif checkTypeOfSMS('airtime for', str) and checkTypeOfSMS('bought', str):
        transactionNoStr, amountStr, receiverStr, timestampStr, balanceStr = [e.split() for e in lisfOfActualMatchs]

        # Extract transaction number
        transactionNo = transactionStr[0]

        # Extract Amount
        amount = transactionStr[1]

        # amount = amount[1]
        # Extract reciever
        receiver = receiverStr[1]

        # Extract timestamp
        timestamp = " ".join(timestampStr[0] + timestampStr[2: 3])

        # Extract timestamp
        balance = balanceStr[2]

    elif checkTypeOfSMS('sent to business', str):
        transactionNo, amount, receiver, timestamp, balance = [e.split() for e in lisfOfActualMatchs]

    elif checkTypeOfSMS('Give', str):
        # Extract transaction number
        transactionNo = lisfOfActualMatchs[0].split()[0]

        # Extract Amount: this produces "Give Tsh78,878"
        amount = re.findall('Give\s+Tsh{1}[,0-9]{1,10}', str)[0].split()[1]

        # Extract reciever
        reciever = re.search('to\s(.+?)\sNew', str)  #Extract the characters after "to" and space and before space and "on"
        reciever = reciever.group(1)

        # Extract timestamp
        timestamp = lisfOfActualMatchs[1]

        # timestamp = timestamp[0] + ' '+timestamp[2]+' '+timestamp[3]
        # Extract timestamp
        # balance = lisfOfActualMatchs[4]

    return [transactonNo, amount, sender, reciever, timestamp, balance]

print(recievedMPesa(example6))
