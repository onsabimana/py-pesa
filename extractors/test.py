"""
Executes unit tests for the parser.
"""
import re

import unittest

from GhanaExtract import TransactionInfo


class TestGhanaTransactionMessages(unittest.TestCase):

    def testSentMoneyNotification(self):
        test_message = 'Trans. ID: 313821006060 You have sent 20GHS to 233261234567.  Your available balance is 250.67GHS.'


        ghana_sent_money_notification_patterns = {
            "transaction_id":  re.compile(r"Trans.\s+ID:\s+(\w+)"),
            "sent_amount": re.compile(r"sent\s+(\d+GHS)"),
            "receiver_account": re.compile(r"to\s+(\w+)"),
            "balance": re.compile(r"balance\s+is\s+(\d+.*\d*GHS)"),
            "sender_account": None,
            "received_amount": None
        }

        info = TransactionInfo(test_message, ghana_sent_money_notification_patterns)

        self.assertEqual(info.transaction_id, "313821006060")
        self.assertEqual(info.sent_amount, "20GHS")
        self.assertEqual(info.receiver_account, "233261234567")
        self.assertEqual(info.balance, "250.67GHS")

    def testReceivedMoneyNotifcation(self):
        pass


if __name__ == '__main__':
    unittest.main()
