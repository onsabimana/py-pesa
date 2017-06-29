import re
#this this file contains functions extract key important information from Tanzania MPesa payment sms

#examples
example ='''
Z10DN636 Confirmed.
You have received Tsh50,000 from
FREDRICK KIMARO
on 27/1/14 at 1:19 PM
New M-PESA balance is Tsh214,676
'''
#function to check which type of sms
def checkTypeOfSMS(word, str):
	if word in str:
		return True
	else:
		False
#function to function for recieved payment 
def recievedMPesa(str):
	if checkTypeOfSMS('received',str) ==True:		#check if this is for M-PESA recieved transaction
		#1 perform extraction of reference number
		refNo = str.partition(' ')[0]
		print(refNo)
		
		#2 perform extraction of amount recieved
		amountRecieved = re.findall('Tsh{1}[,0-9]{1,10}',str)
		print(amountRecieved[0])
		
		#3 perform extraction of Sender's name 
		nameString = re.search('from\s(.+?)\son', str)  #Extract the characters after "from" and space and before space and "on"
		fullName = nameString.group(1)
		firstName = fullName.partition(' ')[0];  	#Then extract only the first name from string which is the first
		lastName = fullName.partition(' ')[2] 		#Then extract only the last name from string which is the first
		print(fullName)
		print(firstName)
		print(lastName)
		#4 perform extraction of date recieved
		datestring = re.search('on\s(.+?)\s', str) 
		timestring = re.search('at\s(.+?)\s', str) 
		print(timestring.group(1))
		#5 perform extraction of new balance (note that this could just be the current amount in the database + recieved in step 2 )
	else:
		print("Wrong function call!")
	return
#call my function
recievedMPesa(example)
	