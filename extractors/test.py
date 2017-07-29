"""
Executes unit tests for the parser.
"""
import re

import unittest

from base_transaction_info import TransactionInfo

import ghana
import tanzaniaMpesa

class TestGhanaTransactionMessages(unittest.TestCase):

#GHANA MONEY TESTS
#----------------------------------------------------------------------------------------------------------------------------
    def testSentMoneyNotification(self):
        test_message = 'Trans. ID: 313821006060 You have sent 20GHS to 233261234567.  Your available balance is 250.67GHS.'

        info = TransactionInfo(test_message, ghana.sent_money_notification_patterns)

        self.assertEqual(info.transaction_id, "313821006060")
        self.assertEqual(info.sent_amount, "20GHS")
        self.assertEqual(info.receiver_account, "233261234567")
        self.assertEqual(info.balance, "250.67GHS")

    def testReceivedMoneyNotifcation(self):
        pass
#TANZANIA MPESA TESTS
#------------------------------------------------------------------------------------------------------------------------------
    def testTzMpesaRecievedMoneyNotification(self):
        test_message = 'Z10DN636 Confirmed. You have received Tsh50,000 from FREDRICK KIMARO on 27/1/14 at 1:19 PM New M-PESA balance is Tsh214,676'

        info = TransactionInfo(test_message, tanzaniaMpesa.tz_mpesa_recieved_money_notification_patterns)

        self.assertEqual(info.transaction_id, "Z10DN636")
        self.assertEqual(info.received_amount, "Tsh50,000")
        self.assertEqual(info.sender_account, "FREDRICK KIMARO")
        self.assertEqual(info.balance, "Tsh214,676")

    def testTzMpesaSentMoneyNotification(self):
        test_message = 'X89IQ877 Confirmed. Tsh2,100 sent to MUSHI WILLIAM on 15/12/13 at 10:19 PM. New M-PESA balance is Tsh23,232.'

        info = TransactionInfo(test_message, tanzaniaMpesa.tz_mpesa_sent_money_notification_patterns)

        self.assertEqual(info.transaction_id, "X89IQ877")
        self.assertEqual(info.sent_amount, "Tsh2,100")
        self.assertEqual(info.receiver_account, "MUSHI WILLIAM")
        self.assertEqual(info.balance, "Tsh23,232")

    def testTzMpesaBuyAirtimeMoneyNotification(self):
        test_message = 'Z92FP098 confirmed. You bought Tsh3,500 of airtime on 22/2/14 at 8:12 PM New M-PESA balance is Tsh2,720'

        info = TransactionInfo(test_message, tanzaniaMpesa.tz_mpesa_buyAirtime_money_notification_patterns)

        self.assertEqual(info.transaction_id, "Z92FP098")
        self.assertEqual(info.received_amount, "Tsh3,500")
        self.assertEqual(info.balance, "Tsh2,720")

if __name__ == '__main__':
    unittest.main()
