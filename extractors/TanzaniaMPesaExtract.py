import re
#this this file contains functions extract key important information from Tanzania MPesa payment sms

#Recieving transaction example
example ='''
Z10DN636 Confirmed.
You have received Tsh50,000 from
FREDRICK KIMARO
on 27/1/14 at 1:19 PM
New M-PESA balance is Tsh214,676
'''
#-----------------------------------------------------GOMMON FUNCTIONS-----------------------------------------------------------------
#function to check which type of sms
def checkTypeOfSMS(word, str):
	if word in str:
		return True
	else:
		return False
#--------------------------------------------------------------------------------------------------------------------------------------
	#function to extract transaction number
def extractTransactionNo(str):
	refNo = str.partition(' ')[0]
	print(refNo)		#this is just for testing/Debugging
	return 
#--------------------------------------------------------------------------------------------------------------------------------------
#function to extract names
def extractName(str):
	fullName =' '
	firstName=' '
	lastName=' '
	nameString=' '
	if checkTypeOfSMS('received',str) ==True:		#check if this is for M-PESA recieved transaction
		#3 perform extraction of Sender's name 
		nameString = re.search('from\s(.+?)\son', str)  #Extract the characters after "from" and space and before space and "on"
	elif checkTypeOfSMS('sent',str) ==True:		#check if this is for M-PESA recieved transaction 
	nameString = re.search('to\s(.+?)\son', str)  #Extract the characters after "to" and space and before space and "on"
	fullName = nameString.group(1)
	firstName = fullName.partition(' ')[0];  	#Then extract only the first name from string which is the first
	lastName = fullName.partition(' ')[2] 		#Then extract only the last name from string which is the first
	print(fullName) #this is just for testing/Debugging
	return 
#--------------------------------------------------------------------------------------------------------------------------------------

#function to extract amount sent or recieved 
def extractAmountSentRecieved(str):
	amount = re.findall('Tsh{1}[,0-9]{1,10}',str)
	print(amount[0])
	return
#--------------------------------------------------------------------------------------------------------------------------------------
def extractBalance(str):
	#balString = re.search('balance is\s(.+?)\s|balance is\s(.+?)\.', str,re.I)
	#print(balString.group(1))
	balString = str.split("balance",1)[1] 
	balance= re.findall("[A-Z]{3}\d+\,\d+|[A-Z]{3}\d+", balString, re.I)
	balance = balance[0]
	print(balance)
def extractDateTime(str):
	datestring = re.search('on\s(.+?)\s', str) 
	timestring = re.search('at\s(.+?)\s', str) 
	if 'PM' in str:
		timestring = timestring.group(1) + ' PM'
		#print(timestring)
	else:
		timestring = timestring.group(1) + ' AM'
		#print(timestring)
	fulldatetime = datestring.group(1) + ' '+timestring
	print(fulldatetime)
	return
#--------------------------------------------------------------------------------------------------------------------------------------
#SPECIFIC FUNCTIONS
	#function to function for recieved payment 
def recievedMPesa(str):
	if checkTypeOfSMS('received',str) ==True:		#check if this is for M-PESA recieved transaction
		#1 perform extraction of reference number using common function
		extractTransactionNo(str)
		#2 perform extraction of amount recieved
		extractAmountSentRecieved(str)
		#3 perform extraction of Sender's name using common function
		extractName(str)
		#4 perform extraction of date and time recieved
		extractDateTime(str)
		#5 perform extraction of new balance (note that this could just be the current amount in the database + recieved in step 2 )
		extractBalance(str)
	else:
		print("Wrong function call!")
	return
#call recieving function
print("-----------------------------------------------------------------------")
recievedMPesa(example)
print("-----------------------------------------------------------------------")
#Sending transaction example
example2='X89IQ877 Confirmed. Tsh2,100 sent to MUSHI WILLIAM on 15/12/13 at 10:19 PM. New M-PESA balance is Tsh23,232.'
def sendMPesa(str):
	if checkTypeOfSMS('sent',str) ==True:		#check if this is for M-PESA recieved transaction
		#1 perform extraction of reference number
		extractTransactionNo(str)
		#2 perform extraction of amount sent using common function
		extractAmountSentRecieved(str)
		#3 perform extraction of reciever's name using common function
		extractName(str)
		#4 perform extraction of date and time recieved
		extractDateTime(str)
		#5) Extract current balance
		extractBalance(str)
	else:
		print("Wrong function call!")
	return
#Bought AIRTIME-------------------------------------------
def buyAirtime(str):
	transactionList =[]
	if checkTypeOfSMS('bought',str) ==True and checkTypeOfSMS('airtime',str) ==True:		#check if this is for M-PESA buy AIRTIME transaction
		#1 perform extraction of reference number
		extractTransactionNo(str)
		#2 perform extraction of amount sent using common function
		extractAmountSentRecieved(str)
		#3 perform extraction of date and time recieved
		extractDateTime(str)
		#4) Extract current balance
		extractBalance(str)
	else:
		print("Wrong function call!")
	return

#Function for you buy Airtime for someone else
def buyAirtime4someone(str):
	if checkTypeOfSMS('airtime',str) ==True and checkTypeOfSMS('for',str) ==True:
		#1 perform extraction of reference number
		extractTransactionNo(str)
		#2 perform extraction of amount sent using common function
		extractAmountSentRecieved(str)
		#3 perform extraction of date and time recieved
		extractDateTime(str)
		#extract reciver's number
		recieverNo = re.findall(r'(0\d{9})',str)
		print(recieverNo)
		#5) Extract current balance
		extractBalance(str)
	else:
		print("Wrong function call!")
	return
#call sending function
print("-----------------------------------------------------------------------")
sendMPesa(example2)
print("-----------------------------------------------------------------------")
example3='''Z92FP098 confirmed. You bought Tsh3,500 of airtime on 22/2/14 at 8:12 PM
New M-PESA balance is Tsh2,720'''
example4='''Y24KU015 confirmed. You bought Tsh501 of airtime for 0765567959 on 1/1/14 at 10:09 PM
New M-PESA balance is Tsh1,430'''
print("----------------------------YOU BOUGHT AIRTIME-------------------------------------------")
buyAirtime(example3)
print("-----------------------------------------------------------------------")
buyAirtime4someone(example4)
print("-----------------------------------------------------------------------")

#SIMPLE UNIT TESTS FOR THE COMMMON FUNCTIONS
tranNo = extractTransactionNo(example3)
print(tranNo)
fullName = extractName(example2)
print(fullName)
