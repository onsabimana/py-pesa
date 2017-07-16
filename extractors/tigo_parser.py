from common_functions import extractDate
from common_functions import checkTypeOfSMS
import re

example1='''New balance is Tsh 138,522.
You have received Tsh 50,000
from CHARLES KOMBA,
0727666074. 31/01/2014 05:36 PM; with TxnId:
PP141141.1843.D06413.
Transact with...'''


def computeTanzTigo(str):
    lisfOfActualMatchs = [];
    transactionDetails = []
    regex = ''

    # Return is a array list of the following values
    # 0 - TransactionNo
    transactionNo = ''

    # 1 - Amount
    amount = ''

    # 2 - Sender
    sender = ''

    # 3 - Reciever
    reciever = ''

    # 4 - Timestamp
    timestamp = ''

    # 5 - Balance
    balance = ''
    transactionType = ''

    if checkTypeOfSMS('received', str) == True:  # check if this is for M-PESA recieved transaction
        regex = r"([A-Z0-9]+\s+Confirmed.)|(received\s+Tsh\d+,\d+|Tsh\d+)|(from\s+(.+?)\s+?on)|(\d{2}\/\d\/\d{2}\s+at\s+\d:\d{2}\s+(PM|AM))|(balance\s+is\s+Tsh\d+,\d+|Tsh\d+)"
    elif (checkTypeOfSMS('sent', str) == True) and (checkTypeOfSMS('business', str) == False):
        regex = ""
    else:
        print('None')

        # Extract required matches from the regular expression results
    matches = re.finditer(regex, str)
    for matchNum, match in enumerate(matches):
        if match.group(0):
            lisfOfActualMatchs.append(match.group(0))
        else:
            print('it did not work')
            # Final extraction of required transaction details:
    if checkTypeOfSMS('received', str) == True:
        # Extract transaction number
        #transactionNo = lisfOfActualMatchs[0].split()[0]

        # Extract Amount
        #amount = lisfOfActualMatchs[1].split()[1]

        # Extract sender
        #sender = lisfOfActualMatchs[2].split()
        #sender = " ".join(sender[1:3])

        # Extract timestamp
        timestamp = extractDate(str)

        # Extract balance
        #balance = lisfOfActualMatchs[4].split()[2]
    else:
        print('Invalid transaction')
        # All the transactions details to the final list
    transactionDetails.append(transactionNo)  # add transaction number

    transactionDetails.append(amount)  # add amount

    transactionDetails.append(sender)  # add sender

    transactionDetails.append(reciever)  # add reciever

    transactionDetails.append(timestamp)  # add timestamp

    transactionDetails.append(balance)  # add balance

    return transactionDetails

print(computeTanzTigo(example1))