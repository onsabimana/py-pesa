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

regex =r"([A-Z0-9]+\s+Confirmed.)|(received\s+Tsh\d+,\d+)|(from\s+(.+?)\s+?on)|(\d{2}\/\d\/\d{2}\s+at\s+\d:\d{2}\s+(PM|AM))|(balance\s+is\s+Tsh\d+,\d+)"
matches = re.finditer(regex, example)


#-----------------------------------------------------START GOMMON FUNCTIONS-----------------------------------------------------------------
#function to check which type of sms
def checkTypeOfSMS(word, str):
	if word in str:
		return True
	else:
		return False
#-----------------------------------------------------END GOMMON FUNCTIONS-----------------------------------------------------------------

#-----------------------------------------------------START SMS TRANSACTION FUNCTIONS-----------------------------------------------------------------
def recievedMPesa(str):
	lisfOfActualMatchs = [];
	transactionDetails = []
	regex = ''	
	#Return is a array list of the following values
	#0 - TransactionNo
	transactionNo = ''
	#1 - Amount
	amount = ''
	#2 - Sender
	sender =''
	#3 - Reciever
	reciever = ''
	#4 - Timestamp
	timestamp =''
	#5 - Balance
	balance = ''
	if checkTypeOfSMS('received',str) ==True:		#check if this is for M-PESA recieved transaction
		regex =r"([A-Z0-9]+\s+Confirmed.)|(received\s+Tsh\d+,\d+|Tsh\d+)|(from\s+(.+?)\s+?on)|(\d{2}\/\d\/\d{2}\s+at\s+\d:\d{2}\s+(PM|AM))|(balance\s+is\s+Tsh\d+,\d+|Tsh\d+)"
	elif checkTypeOfSMS('sent',str) ==True:
		regex = r"([A-Z0-9]+\s+Confirmed.)|(\s+Tsh\d+,\d+|Tsh\d+)|(sent\s+(.+?)\s+?on)|(\d{2}\/\d{2}\/\d{2}\s+at\s+\d{2}:\d{2}\s+(PM|AM))|(balance\s+is\s+Tsh\d+,\d+|Tsh\d+)"
	elif checkTypeOfSMS('airtime on',str) ==True & checkTypeOfSMS('bought',str):
		regex = r"([A-Z0-9]+\s+confirmed.|[A-Z0-9]+\s+Confirmed.)|(bought\s+Tsh\d+,\d+|Tsh\d+)|(from\s+(.+?)\s+?on)|(\d{2}\/\d\/\d{2}\s+at\s+\d:\d{2}\s+(PM|AM))|(balance\s+is\s+Tsh\d+,\d+|Tsh\d+)"
	elif checkTypeOfSMS('airtime for',str) ==True & checkTypeOfSMS('bought',str):
		regex=r"([A-Z0-9]+\s+confirmed.|[A-Z0-9]+\s+Confirmed.)|(bought\s+Tsh\d+,\d+|Tsh\d+)|(for\s+(.+?)\s+?on)|(\d{2}\/\d\/\d{2}|\d\/\d\/\d{2}\s+at\s+\d{2}:\d{2}\s+(PM|AM)|\s+\d:\d\s+(PM|AM))|(balance\s+is\s+Tsh\d+,\d+|Tsh\d+)"
	else:
		print("Wrong function for this transaction!")
	#Extract required matches from the regular expression results
	matches = re.finditer(regex, str)
	for matchNum, match in enumerate(matches):
		if match.group(0):
			lisfOfActualMatchs.append(match.group(0))
		else:
			print('it did not work') 
	#Final extraction of required transaction details:
	if checkTypeOfSMS('received',str) ==True:	
		#Extract transaction number
		transactionNo=lisfOfActualMatchs[0].split()
		transactionNo = transactionNo[0]
		#Extract Amount
		amount = lisfOfActualMatchs[1].split()
		amount = amount[1]
		#Extract sender
		sender = lisfOfActualMatchs[2].split()
		sender = sender[1] + ' '+sender[2]
		#Extract timestamp
		timestamp = lisfOfActualMatchs[3].split()
		timestamp = timestamp[0] + ' '+timestamp[2]+' '+timestamp[3]
		#Extract timestamp
		balance = lisfOfActualMatchs[4].split()
		balance = balance[2]
	elif checkTypeOfSMS('sent',str) ==True:	
		#Extract transaction number
		transactionNo=lisfOfActualMatchs[0].split()
		transactionNo = transactionNo[0]
		#Extract Amount
		amount = lisfOfActualMatchs[1]
		#Extract sender
		reciever = lisfOfActualMatchs[2].split()
		reciever = reciever[2] + ' '+reciever[3]
		#Extract timestamp
		timestamp = lisfOfActualMatchs[3].split()
		timestamp = timestamp[0] + ' '+timestamp[2]+' '+timestamp[3]
		#Extract timestamp
		balance = lisfOfActualMatchs[4].split()
		balance = balance[2]
	if checkTypeOfSMS('airtime on',str) ==True & checkTypeOfSMS('bought',str) ==True:	
		#Extract transaction number
		transactionNo=lisfOfActualMatchs[0].split()
		transactionNo = transactionNo[0]
		#Extract Amount
		amount = lisfOfActualMatchs[1].split()
		amount = amount[1]
		#Extract timestamp
		timestamp = lisfOfActualMatchs[2].split()
		timestamp = timestamp[0] + ' '+timestamp[2]+' '+timestamp[3]
		#Extract timestamp
		balance = lisfOfActualMatchs[3].split()
		balance = balance[2]
	if checkTypeOfSMS('airtime for',str) ==True & checkTypeOfSMS('bought',str) ==True:	
		#Extract transaction number
		transactionNo=lisfOfActualMatchs[0].split()
		transactionNo = transactionNo[0]
		#Extract Amount
		amount = lisfOfActualMatchs[1]
		#amount = amount[1]
		#Extract reciever
		reciever = lisfOfActualMatchs[2].split()
		reciever = reciever[1]
		#Extract timestamp
		timestamp = lisfOfActualMatchs[3].split()
		timestamp = timestamp[0] + ' '+timestamp[2]+' '+timestamp[3]
		#Extract timestamp
		balance = lisfOfActualMatchs[4].split()
		balance = balance[2]
	#All the transactions details to the final list
	transactionDetails.append(transactionNo)    #add transaction number
	transactionDetails.append(amount)    #add amount
	transactionDetails.append(sender)    #add sender
	transactionDetails.append(reciever)    #add reciever
	transactionDetails.append(timestamp)    #add timestamp
	transactionDetails.append(balance)    #add balance
	return transactionDetails
	
print(recievedMPesa(example4))
