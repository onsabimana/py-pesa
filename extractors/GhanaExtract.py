import re

example = 'Trans. ID: 313821006060 You have sent 20GHS to 233261234567.  Your available balance is 250.67GHS.'
#function to extract transaction number only
def extractTransactionNo(str):
	transactionNo = re.findall("[A-z]{5}\.\s[A-Z]{2}\:\s\d+",str)
	transactionNo = re.findall("\d{12}",transactionNo[0])
	transactionNo = transactionNo[0]
	print (transactionNo)
	return
#function to extract amount sent
def extractAmountSent(str):
	allMoneyInString = re.findall("\d+\.\d+[A-Z]{3}|\d+[A-Z]{3}", example, re.I)
	actualSentAmount = allMoneyInString[0]
	print (actualSentAmount)
	return

#function to extract account number
def extractRecieverAccount(str):
	stringExact = re.findall("[a-z]{2}\s\d{12}\.", str)
	accountNo = transactionNo = re.findall("\d{12}",stringExact[0])
	accountNo = accountNo[0]
	print (accountNo)
	return
#Function to exact available balance#function to extract account number
def extractAvailableBal(str):
	allMoneys = re.findall("\d+\.\d+[A-Z]{3}|\d+[A-Z]{3}", str, re.I)
	currentBal = allMoneys[1]
	print (currentBal)
	return
#call my function
extractTransactionNo(example)
extractAmountSent(example)
extractRecieverAccount(example)
extractAvailableBal(example)
