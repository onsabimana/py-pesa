"""
Executes unit tests for the parser.
"""

import unittest

from GhanaExtract import SentMoneyNotification


class TestGhanaTransactionMessages(unittest.TestCase):

    def testSentMoneyNotification(self):
        test_message = 'Trans. ID: 313821006060 You have sent 20GHS to 233261234567.  Your available balance is 250.67GHS.'

        sent_notification = SentMoneyNotification(test_message)

        self.assertEqual(sent_notification.transaction_id, "313821006060")
        self.assertEqual(sent_notification.sent_amount, "20GHS")
        self.assertEqual(sent_notification.receiver_account, "233261234567")
        self.assertEqual(sent_notification.balance, "250.67GHS")


if __name__ == '__main__':
    unittest.main()
