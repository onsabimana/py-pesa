"""
Executes unit tests for the parser.
"""
import re

import unittest

from base_transaction_info import TransactionInfo

import ghana
import tanzaniaMpesa


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


class TestTanzaniaTransactionMessages(unittest.TestCase):

    #-------------------- START OF MPESA TRANSACTIONS TESTS --------------------
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

        info = TransactionInfo(test_message, tanzaniaMpesa.tz_mpesa_buyairtime_money_notification_patterns)

        self.assertEqual(info.transaction_id, "Z92FP098")
        self.assertEqual(info.received_amount, "Tsh3,500")
        self.assertEqual(info.balance, "Tsh2,720")

    def testTzMpesaSendAirtimeMoneyNotification(self):
        test_message = 'Y24KU015 confirmed. You bought Tsh501 of airtime for 0765567959 on 1/1/14 at 10:09 PM New M-PESA balance is Tsh1,430'

        info = TransactionInfo(test_message, tanzaniaMpesa.tz_mpesa_sendairtime_money_notification_patterns)

        self.assertEqual(info.transaction_id, "Y24KU015")
        self.assertEqual(info.sent_amount, "Tsh501")
        self.assertEqual(info.receiver_account, "0765567959")
        self.assertEqual(info.balance, "Tsh1,430")

    def testTzMpesaBankdepositMoneyNotification(self):
        test_message = 'Z15EE301 Confirmed. Tsh212,000 sent to business Bank for account ACB-11567341482 on 28/1/14 at 11:30 PM New M-PESA balance is Tsh225.'

        info = TransactionInfo(test_message, tanzaniaMpesa.tz_mpesa_bankdeposit_money_notification_patterns)

        self.assertEqual(info.transaction_id, "Z15EE301")
        self.assertEqual(info.sent_amount, "Tsh212,000")
        self.assertEqual(info.receiver_account, "ACB-11567341482")
        self.assertEqual(info.balance, "Tsh225")

    def testTzMpesadepositMoneyNotification(self):
        test_message = 'BA35RS735 Confirmed. on 8/3/14 at 4:59 PM Give Tsh10,000 cash to Hilda Joseph Mushi. New M-PESA balance is Tsh10,015'

        info = TransactionInfo(test_message, tanzaniaMpesa.tz_mpesa_deposit_money_notification_patterns)

        self.assertEqual(info.transaction_id, "BA35RS735")
        self.assertEqual(info.sent_amount, "Tsh10,000")
        self.assertEqual(info.receiver_account, "Hilda Joseph Mushi")
        self.assertEqual(info.balance, "Tsh10,015")

    def testTzMpesaWithdrawMoneyNotification(self):
        test_message = 'BA35RT157 Confirmed. on 8/3/14 at 5:19 PM Withdraw Tsh6,000 from 128137 - EMANUEL SHANI New M-PESA balance is Tsh3,415'

        info = TransactionInfo(test_message, tanzaniaMpesa.tz_mpesa_withdraw_money_notification_patterns)

        self.assertEqual(info.transaction_id, "BA35RT157")
        self.assertEqual(info.received_amount, "Tsh6,000")
        self.assertEqual(info.sender_account, "128137 - EMANUEL SHANI")
        self.assertEqual(info.balance, "Tsh3,415")

    def testTzMpesaCheckBalanceMoneyNotification(self):
        test_message = 'BB43UB521 Confirmed. Your M-PESA balance was Tsh2,354 on 8/3/14 at 5:26 PM.'

        info = TransactionInfo(test_message, tanzaniaMpesa.tz_mpesa_checkbalance_money_notification_patterns)

        self.assertEqual(info.transaction_id, "BB43UB521")
        self.assertEqual(info.balance, "Tsh2,354")

    #-------------------- END OF MPESA TRANSACTIONS TESTS ----------------------


    #-------------------- START OF TIGO TRANSACTIONS TESTS ---------------------
    def testTztTigoRecievedMoneyNotification(self):
        test_message = 'New balance is Tsh 138,522. You have received Tsh 50,000 from CHARLES KOMBA, 0727666074. 31/01/2014 05:36 PM; with TxnId: PP141141.1843.D06413. Transact with...'

        info = TransactionInfo(test_message, tanzaniaMpesa.tz_tigo_recieved_money_notification_patterns)

        self.assertEqual(info.transaction_id, "PP141141.1843.D06413")
        self.assertEqual(info.received_amount, "Tsh 50,000")
        self.assertEqual(info.sender_account, "CHARLES KOMBA, 0727666074")
        self.assertEqual(info.balance, "Tsh 138,522")

    def testTzTigoSentMoneyNotification(self):
        test_message = 'New balance is Tsh 2,515. Money sent successfully to ANJELA KIRIA, 0745239044. Amount: Tsh 31,000. Fee: Tsh 350.TxnID: PP134304.0912.J02744. You can now send...'

        info = TransactionInfo(test_message, tanzaniaMpesa.tz_tigo_sent_money_notification_patterns)

        self.assertEqual(info.transaction_id, "PP134304.0912.J02744")
        self.assertEqual(info.sent_amount, "Tsh 31,000")
        self.assertEqual(info.receiver_account, "ANJELA KIRIA, 0745239044")
        self.assertEqual(info.balance, "Tsh 2,515")

    def testTzTigoBuyAirtimeMoneyNotification(self):
        test_message = 'New balance is Tsh 2,266. Your recharge request is successful for amount Tsh 3,501. TxnId : RC140320.1332.D09804. Transact with Tigo Pesa and win from Tshs...'

        info = TransactionInfo(test_message, tanzaniaMpesa.tz_tigo_buyairtime_money_notification_patterns)

        self.assertEqual(info.transaction_id, "RC140320.1332.D09804")
        self.assertEqual(info.received_amount, "Tsh 3,501")
        self.assertEqual(info.balance, "Tsh 2,266")

    def testTzTigoPayBillMoneyNotification(self):
        test_message = 'Bill Transaction has been sent to Tanesco.Please wait for confirmation TxnId: BP150143.1343.E03178, Bill Number:01343392423, transaction amount : 20,000 Tsh,new balance :71,073 Tsh, Company Tanesco.'

        info = TransactionInfo(test_message, tanzaniaMpesa.tz_mpesa_tigo_paybill_money_notification_patterns)

        self.assertEqual(info.transaction_id, "BP150143.1343.E03178")
        self.assertEqual(info.sent_amount, "20,000 Tsh")
        self.assertEqual(info.receiver_account, "Tanesco")                  # this is not really an account per se, maybe Bill number is the receiver_account
        self.assertEqual(info.sender_account, "01343392423")
        self.assertEqual(info.balance, "71,073 Tsh")

    def testTzTigoBankdepositMoneyNotification(self):
        test_message = 'Bank payment successfull. The details are : TxnId: BP150121.1337.C09085, Ref Number:10411342553, transaction amount : 111,000 Tsh , charges: 0 Tsh,new balance :2,323 Tsh, Bank Name : ACB'

        info = TransactionInfo(test_message, tanzaniaMpesa.tz_tigo_bankdeposit_money_notification_patterns)

        self.assertEqual(info.transaction_id, "BP150121.1337.C09085")
        self.assertEqual(info.sent_amount, "111,000 Tsh")
        self.assertEqual(info.receiver_account, "ACB")
        self.assertEqual(info.balance, "2,323 Tsh")

    def testTzTigoDepositMoneyNotification(self):
        test_message = 'New balance is Tsh 35,165. Cash-In of Tsh 35,000 successful. Agent HILDA MUSHI. TxnID: CI154303.0933.G03265. You can now send money from your CRDB account to...'

        info = TransactionInfo(test_message, tanzaniaMpesa.tz_tigo_deposit_money_notification_patterns)

        self.assertEqual(info.transaction_id, "CI154303.0933.G03265")
        self.assertEqual(info.sent_amount, "Tsh 35,000")
        self.assertEqual(info.receiver_account, "HILDA MUSHI")
        self.assertEqual(info.balance, "Tsh 35,165")

    def testTzTigoWithdrawMoneyNotification(self):
        test_message = 'New balance is Tsh 6,022. Cash-Out to EMANUEL KIULA was successful. Amount Tsh 130,000. Charges Tsh 2500.TxnID CO150121.3223.G00889. Transact with Tigo Pesa...'

        info = TransactionInfo(test_message, tanzaniaMpesa.tz_tigo_withdraw_money_notification_patterns)

        self.assertEqual(info.transaction_id, "CO150121.3223.G00889")
        self.assertEqual(info.received_amount, "Tsh 130,000")
        self.assertEqual(info.receiver_account, "EMANUEL KIULA")
        self.assertEqual(info.balance, "Tsh 6,022")

if __name__ == '__main__':
    unittest.main()
