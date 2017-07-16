import re
from dateutil.parser import parse

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
