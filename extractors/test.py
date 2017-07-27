"""
Executes unit tests for the parser.
"""
import re

import unittest

from base_transaction_info import TransactionInfo

import ghana

class TestGhanaTransactionMessages(unittest.TestCase):

    def testSentMoneyNotification(self):
        test_message = 'Trans. ID: 313821006060 You have sent 20GHS to 233261234567.  Your available balance is 250.67GHS.'

        info = TransactionInfo(test_message, ghana.sent_money_notification_patterns)

        self.assertEqual(info.transaction_id, "313821006060")
        self.assertEqual(info.sent_amount, "20GHS")
        self.assertEqual(info.receiver_account, "233261234567")
        self.assertEqual(info.balance, "250.67GHS")

    def testReceivedMoneyNotifcation(self):
        pass


if __name__ == '__main__':
    unittest.main()
