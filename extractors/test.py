"""
Executes unit tests for the parser.
"""
import re

import unittest

from base_transaction_info import TransactionInfo

import ghana
import tanzania
import kenya


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

        info = TransactionInfo(test_message, tanzania.tz_mpesa_recieved_money_notification_patterns)

        self.assertEqual(info.transaction_id, "Z10DN636")
        self.assertEqual(info.received_amount, "Tsh50,000")
        self.assertEqual(info.sender_account, "FREDRICK KIMARO")
        self.assertEqual(info.balance, "Tsh214,676")

    def testTzMpesaSentMoneyNotification(self):
        test_message = 'X89IQ877 Confirmed. Tsh2,100 sent to MUSHI WILLIAM on 15/12/13 at 10:19 PM. New M-PESA balance is Tsh23,232.'

        info = TransactionInfo(test_message, tanzania.tz_mpesa_sent_money_notification_patterns)

        self.assertEqual(info.transaction_id, "X89IQ877")
        self.assertEqual(info.sent_amount, "Tsh2,100")
        self.assertEqual(info.receiver_account, "MUSHI WILLIAM")
        self.assertEqual(info.balance, "Tsh23,232")

    def testTzMpesaBuyAirtimeMoneyNotification(self):
        test_message = 'Z92FP098 confirmed. You bought Tsh3,500 of airtime on 22/2/14 at 8:12 PM New M-PESA balance is Tsh2,720'

        info = TransactionInfo(test_message, tanzania.tz_mpesa_buyairtime_money_notification_patterns)

        self.assertEqual(info.transaction_id, "Z92FP098")
        self.assertEqual(info.received_amount, "Tsh3,500")
        self.assertEqual(info.balance, "Tsh2,720")

    def testTzMpesaSendAirtimeMoneyNotification(self):
        test_message = 'Y24KU015 confirmed. You bought Tsh501 of airtime for 0765567959 on 1/1/14 at 10:09 PM New M-PESA balance is Tsh1,430'

        info = TransactionInfo(test_message, tanzania.tz_mpesa_sendairtime_money_notification_patterns)

        self.assertEqual(info.transaction_id, "Y24KU015")
        self.assertEqual(info.sent_amount, "Tsh501")
        self.assertEqual(info.receiver_account, "0765567959")
        self.assertEqual(info.balance, "Tsh1,430")

    def testTzMpesaBankdepositMoneyNotification(self):
        test_message = 'Z15EE301 Confirmed. Tsh212,000 sent to business Bank for account ACB-11567341482 on 28/1/14 at 11:30 PM New M-PESA balance is Tsh225.'

        info = TransactionInfo(test_message, tanzania.tz_mpesa_bankdeposit_money_notification_patterns)

        self.assertEqual(info.transaction_id, "Z15EE301")
        self.assertEqual(info.sent_amount, "Tsh212,000")
        self.assertEqual(info.receiver_account, "ACB-11567341482")
        self.assertEqual(info.balance, "Tsh225")

    def testTzMpesadepositMoneyNotification(self):
        test_message = 'BA35RS735 Confirmed. on 8/3/14 at 4:59 PM Give Tsh10,000 cash to Hilda Joseph Mushi. New M-PESA balance is Tsh10,015'

        info = TransactionInfo(test_message, tanzania.tz_mpesa_deposit_money_notification_patterns)

        self.assertEqual(info.transaction_id, "BA35RS735")
        self.assertEqual(info.sent_amount, "Tsh10,000")
        self.assertEqual(info.receiver_account, "Hilda Joseph Mushi")
        self.assertEqual(info.balance, "Tsh10,015")

    def testTzMpesaWithdrawMoneyNotification(self):
        test_message = 'BA35RT157 Confirmed. on 8/3/14 at 5:19 PM Withdraw Tsh6,000 from 128137 - EMANUEL SHANI New M-PESA balance is Tsh3,415'

        info = TransactionInfo(test_message, tanzania.tz_mpesa_withdraw_money_notification_patterns)

        self.assertEqual(info.transaction_id, "BA35RT157")
        self.assertEqual(info.received_amount, "Tsh6,000")
        self.assertEqual(info.sender_account, "128137 - EMANUEL SHANI")
        self.assertEqual(info.balance, "Tsh3,415")

    def testTzMpesaCheckBalanceMoneyNotification(self):
        test_message = 'BB43UB521 Confirmed. Your M-PESA balance was Tsh2,354 on 8/3/14 at 5:26 PM.'

        info = TransactionInfo(test_message, tanzania.tz_mpesa_checkbalance_money_notification_patterns)

        self.assertEqual(info.transaction_id, "BB43UB521")
        self.assertEqual(info.balance, "Tsh2,354")

    #-------------------- END OF MPESA TRANSACTIONS TESTS ----------------------


    #-------------------- START OF TIGO TRANSACTIONS TESTS ---------------------
    def testTztTigoRecievedMoneyNotification(self):
        test_message = 'New balance is Tsh 138,522. You have received Tsh 50,000 from CHARLES KOMBA, 0727666074. 31/01/2014 05:36 PM; with TxnId: PP141141.1843.D06413. Transact with...'

        info = TransactionInfo(test_message, tanzania.tz_tigo_recieved_money_notification_patterns)

        self.assertEqual(info.transaction_id, "PP141141.1843.D06413")
        self.assertEqual(info.received_amount, "Tsh 50,000")
        self.assertEqual(info.sender_account, "CHARLES KOMBA, 0727666074")
        self.assertEqual(info.balance, "Tsh 138,522")

    def testTzTigoSentMoneyNotification(self):
        test_message = 'New balance is Tsh 2,515. Money sent successfully to ANJELA KIRIA, 0745239044. Amount: Tsh 31,000. Fee: Tsh 350.TxnID: PP134304.0912.J02744. You can now send...'

        info = TransactionInfo(test_message, tanzania.tz_tigo_sent_money_notification_patterns)

        self.assertEqual(info.transaction_id, "PP134304.0912.J02744")
        self.assertEqual(info.sent_amount, "Tsh 31,000")
        self.assertEqual(info.receiver_account, "ANJELA KIRIA, 0745239044")
        self.assertEqual(info.balance, "Tsh 2,515")

    def testTzTigoBuyAirtimeMoneyNotification(self):
        test_message = 'New balance is Tsh 2,266. Your recharge request is successful for amount Tsh 3,501. TxnId : RC140320.1332.D09804. Transact with Tigo Pesa and win from Tshs...'

        info = TransactionInfo(test_message, tanzania.tz_tigo_buyairtime_money_notification_patterns)

        self.assertEqual(info.transaction_id, "RC140320.1332.D09804")
        self.assertEqual(info.received_amount, "Tsh 3,501")
        self.assertEqual(info.balance, "Tsh 2,266")

    def testTzTigoPayBillMoneyNotification(self):
        test_message = 'Bill Transaction has been sent to Tanesco.Please wait for confirmation TxnId: BP150143.1343.E03178, Bill Number:01343392423, transaction amount : 20,000 Tsh,new balance :71,073 Tsh, Company Tanesco.'

        info = TransactionInfo(test_message, tanzania.tz_mpesa_tigo_paybill_money_notification_patterns)

        self.assertEqual(info.transaction_id, "BP150143.1343.E03178")
        self.assertEqual(info.sent_amount, "20,000 Tsh")
        self.assertEqual(info.receiver_account, "Tanesco")                  # this is not really an account per se, maybe Bill number is the receiver_account
        self.assertEqual(info.sender_account, "01343392423")
        self.assertEqual(info.balance, "71,073 Tsh")

    def testTzTigoBankdepositMoneyNotification(self):
        test_message = 'Bank payment successfull. The details are : TxnId: BP150121.1337.C09085, Ref Number:10411342553, transaction amount : 111,000 Tsh , charges: 0 Tsh,new balance :2,323 Tsh, Bank Name : ACB'

        info = TransactionInfo(test_message, tanzania.tz_tigo_bankdeposit_money_notification_patterns)

        self.assertEqual(info.transaction_id, "BP150121.1337.C09085")
        self.assertEqual(info.sent_amount, "111,000 Tsh")
        self.assertEqual(info.receiver_account, "ACB")
        self.assertEqual(info.balance, "2,323 Tsh")

    def testTzTigoDepositMoneyNotification(self):
        test_message = 'New balance is Tsh 35,165. Cash-In of Tsh 35,000 successful. Agent HILDA MUSHI. TxnID: CI154303.0933.G03265. You can now send money from your CRDB account to...'

        info = TransactionInfo(test_message, tanzania.tz_tigo_deposit_money_notification_patterns)

        self.assertEqual(info.transaction_id, "CI154303.0933.G03265")
        self.assertEqual(info.sent_amount, "Tsh 35,000")
        self.assertEqual(info.receiver_account, "HILDA MUSHI")
        self.assertEqual(info.balance, "Tsh 35,165")

    def testTzTigoWithdrawMoneyNotification(self):
        test_message = 'New balance is Tsh 6,022. Cash-Out to EMANUEL KIULA was successful. Amount Tsh 130,000. Charges Tsh 2500.TxnID CO150121.3223.G00889. Transact with Tigo Pesa...'

        info = TransactionInfo(test_message, tanzania.tz_tigo_withdraw_money_notification_patterns)

        self.assertEqual(info.transaction_id, "CO150121.3223.G00889")
        self.assertEqual(info.received_amount, "Tsh 130,000")
        self.assertEqual(info.receiver_account, "EMANUEL KIULA")
        self.assertEqual(info.balance, "Tsh 6,022")

    #-------------------- END OF TIGO TRANSACTIONS TESTS ----------------------

class TestKenyaTransactionMessages(unittest.TestCase):
    #-------------------- START OF KENYA AIRTEL PRIVATE TRANSACTIONS TESTS-------
    def testKeAirtelBuyMoneyNotification(self):
        test_message = 'Trans. ID: 7740224211672. You have received Airtime of 10.00Ksh from your OWN account.'

        info = TransactionInfo(test_message, kenya.ke_airtel_buyairtime_money_notification_patterns)

        self.assertEqual(info.transaction_id, "7740224211672")
        self.assertEqual(info.received_amount, "10.00Ksh")

    def testKeAirtelReceiveMoneyNotification(self):
        test_message = 'Trans. ID: 1440225031704 You have received 50.00Ksh from ANGELA NZIOKI. Your available balance is 155.00Ksh.'

        info = TransactionInfo(test_message, kenya.ke_airtel_received_money_notification_patterns)

        self.assertEqual(info.transaction_id, "1440225031704")
        self.assertEqual(info.received_amount, "50.00Ksh")
        self.assertEqual(info.sender_account, "ANGELA NZIOKI")
        self.assertEqual(info.balance, "155.00Ksh")

    def testKeAirtelSendMoneyNotification(self):
        test_message = 'Trans. ID: 1450335211705 You have sent 50.00Ksh to JOSEPH KARANJA. Your available balance is 10.00Ksh.'

        info = TransactionInfo(test_message, kenya.ke_airtel_send_money_notification_patterns)

        self.assertEqual(info.transaction_id, "1450335211705")
        self.assertEqual(info.sent_amount, "50.00Ksh")
        self.assertEqual(info.receiver_account, "JOSEPH KARANJA")
        self.assertEqual(info.balance, "10.00Ksh")

    def testKeAirtelPayBillMoneyNotification(self):
        test_message = 'Trans. ID: 2240545115618 You have sent 50.00Ksh to UHASIBU in reference to TEST. Your available balance is 105.00Ksh.'

        info = TransactionInfo(test_message, kenya.ke_airtel_paybill_money_notification_patterns)

        self.assertEqual(info.transaction_id, "2240545115618")
        self.assertEqual(info.sent_amount, "50.00Ksh")
        self.assertEqual(info.receiver_account, "UHASIBU")
        self.assertEqual(info.balance, "105.00Ksh")

    def testKeAirtelCashDepositMoneyNotification(self):
        test_message = 'Trans. ID: 0231412250320 You have received 200Ksh from ART111. Your available balance is 200.00Ksh.'

        info = TransactionInfo(test_message, kenya.ke_airtel_cashdeposit_money_notification_patterns)

        self.assertEqual(info.transaction_id, "0231412250320")
        self.assertEqual(info.received_amount, "200Ksh")
        self.assertEqual(info.sender_account, "ART111")
        self.assertEqual(info.balance, "200.00Ksh")

    def testKeAirtelBalanceCheckMoneyNotification(self):
        test_message = 'Your available bal. is Ksh60.00.'

        info = TransactionInfo(test_message, kenya.ke_airtel_balancecheck_money_notification_patterns)

        self.assertEqual(info.balance, "Ksh60.00")

    def testKeAirtelErrorMoneyNotification(self):
        test_message = 'The amount you are trying to transfer is less than the minimum amount of 50.00Ksh allowed.'

        info = TransactionInfo(test_message, kenya.ke_airtel_error_money_notification_patterns)

        self.assertEqual(info.sent_amount, "50.00Ksh")

    #-------------------- START OF MPESA PRIVATE TRANSACTIONS TESTS ---------------------
    def testKeMpesaTransferMoneyNotification(self):
        test_message = 'DT85TH896 Confirmed. You have received Ksh3,500.00 from 501901 - KCB Money Transfer Services on 31/7/13 at 6:43 PM New M-PESA balance is Ksh11,312.00.Save & get a loan on Mshwari'

        info = TransactionInfo(test_message, kenya.ke_mpesa_transfer_money_notification_patterns)

        self.assertEqual(info.transaction_id, "DT85TH896")
        self.assertEqual(info.received_amount, "Ksh3,500.00")
        self.assertEqual(info.sender_account, "501901 - KCB Money Transfer Services")
        self.assertEqual(info.balance, "Ksh11,312.00")

    def testKeMpesaReceivedMoneyNotification(self):
        test_message = 'BS49OR201 Confirmed. You have received Ksh50.00 from MICHAEL FEDERSEN 254729901555 on 15/10/11 at 11:52 AM New M-PESA balance is Ksh100.00'

        info = TransactionInfo(test_message, kenya.ke_mpesa_received_money_notification_patterns)

        self.assertEqual(info.transaction_id, "BS49OR201")
        self.assertEqual(info.received_amount, "Ksh50.00")
        self.assertEqual(info.sender_account, "MICHAEL FEDERSEN 254729901555")
        self.assertEqual(info.balance, "Ksh100.00")

    def testKeMpesaCashDepositMoneyNotification(self):
        test_message = 'DQ94ZE762 Confirmed. on 3/7/13 at 9:07 AM Give Ksh1,000.00 cash to Digital Africa Services Jolet Supermarket New M-PESA balance is Ksh1,338.00'

        info = TransactionInfo(test_message, kenya.ke_mpesa_cashdeposit_money_notification_patterns)

        self.assertEqual(info.transaction_id, "DQ94ZE762")
        self.assertEqual(info.sent_amount, "Ksh1,000.00")
        self.assertEqual(info.receiver_account, "Digital Africa Services Jolet Supermarket")
        self.assertEqual(info.balance, "Ksh1,338.00")

    def testKeMpesaWidrawMoneyNotification(self):
        test_message = 'ET04TG335 Confirmed. on 20/2/14 at 2:44 PM Withdraw Ksh16,000.00 from 129324 - Brothers Link Agency Vetngong Road New M-PESA balance is Ksh570.00.Save & get a loan on MShwari'

        info = TransactionInfo(test_message, kenya.ke_mpesa_withdraw_money_notification_patterns)

        self.assertEqual(info.transaction_id, "ET04TG335")
        self.assertEqual(info.sent_amount, "Ksh16,000.00")
        self.assertEqual(info.receiver_account, "129324 - Brothers Link Agency Vetngong Road")
        self.assertEqual(info.balance, "Ksh570.00")

    def testKeMpesaSendMoneyNotification(self):
        test_message = 'DZ12GX874 Confirmed. Ksh2,100.00 sent to BRIAN MBUGUA 0723447655 on 17/9/13 at 3:16 PM New M-PESA balance is Ksh106.00.PIN YAKO SIRI YAKO'

        info = TransactionInfo(test_message, kenya.ke_mpesa_send_money_notification_patterns)

        self.assertEqual(info.transaction_id, "DZ12GX874")
        self.assertEqual(info.sent_amount, "Ksh2,100.00")
        self.assertEqual(info.receiver_account, "BRIAN MBUGUA 0723447655")
        self.assertEqual(info.balance, "Ksh106.00")

    def testKeMpesaBuyAirtimeMoneyNotification(self):
        test_message = 'DZ55IX312 confirmed. You bought Ksh100.00 of airtime on 21/9/13 at 5:51 PM New M-PESA balance is Ksh6.00.Safaricom only calls you from 0722000000'

        info = TransactionInfo(test_message, kenya.ke_mpesa_buyairtime_money_notification_patterns)

        self.assertEqual(info.transaction_id, "DZ55IX312")
        self.assertEqual(info.received_amount, "Ksh100.00")
        self.assertEqual(info.sender_account, "0722000000")
        self.assertEqual(info.balance, "Ksh6.00")

    def testKeMpesaBalanceCheckMoneyNotification(self):
        test_message = 'DQ91IB986 Confirmed. Your M-PESA balance was Ksh339.00 on 2/7/13 at 6:46 PM.Safaricom only calls you from 0722000000'

        info = TransactionInfo(test_message, kenya.ke_mpesa_balancecheck_money_notification_patterns)

        self.assertEqual(info.transaction_id, "DQ91IB986")
        self.assertEqual(info.sender_account, "0722000000")
        self.assertEqual(info.balance, "Ksh339.00")

    def testKeMpesaPayBillMoneyNotification(self):
        test_message = 'DY28XV679 Confirmed. Ksh4,000.00 sent to KCB Paybill AC for account 1137238445 on 9/9/13 at 11:31 PM New M-PESA balance is Ksh22.00.'

        info = TransactionInfo(test_message, kenya.ke_mpesa_paybill_money_notification_patterns)

        self.assertEqual(info.transaction_id, "DY28XV679")
        self.assertEqual(info.sent_amount, "Ksh4,000.00")
        self.assertEqual(info.receiver_account, "1137238445")
        self.assertEqual(info.balance, "Ksh22.00")

    def testKeMpesaBuygoodsReceiveMoneyNotification(self):
        test_message = 'EA54HY643 Confirmed. on 28/9/13 at 1:14 PM Ksh50.00 received from 254729639024 MORRIS M. New Account balance is Ksh54.00'

        info = TransactionInfo(test_message, kenya.ke_mpesa_buygoodsreceieve_money_notification_patterns)

        self.assertEqual(info.transaction_id, "EA54HY643")
        self.assertEqual(info.received_amount, "Ksh50.00")
        self.assertEqual(info.sender_account, "254729639024 MORRIS M")
        self.assertEqual(info.balance, "Ksh54.00")

    def testKeMpesaMshwariTransferMoneyNotification(self):
        test_message = 'EB97SA431 Confirmed. Ksh50.00 transferred to M-Shwari account on 13/10/13 at 2:13 AM. M-PESA balance is Ksh4,265.00, new M-Shwari account balance is Ksh20,087.69'

        info = TransactionInfo(test_message, kenya.ke_mpesa_mshwaritransfer_money_notification_patterns)

        self.assertEqual(info.transaction_id, "EB97SA431")
        self.assertEqual(info.sent_amount, "Ksh50.00")
        self.assertEqual(info.receiver_account, "M-Shwari")
        self.assertEqual(info.balance, "Ksh4,265.00")

    def testKeMpesaMshwariReceiveMoneyNotification(self):
        test_message = 'EB87ST824 Confirmed. You have transferred Ksh50.00 from your M-Shwari account on 13/10/13 at 2:14 AM. M-Shwari balance is Ksh20,037.69. M-PESA balance is Ksh4,315.00.'

        info = TransactionInfo(test_message, kenya.ke_mpesa_mshwarireceive_money_notification_patterns)

        self.assertEqual(info.transaction_id, "EB87ST824")
        self.assertEqual(info.received_amount, "Ksh50.00")
        self.assertEqual(info.sender_account, "M-Shwari")
        self.assertEqual(info.balance, "Ksh4,315.00")

    def testKeMpesaLipaMpesaReceivedRefundMoneyNotification(self):
        test_message = 'EE56TY519 confirmed. Your Pay Shop transaction EE56TT315 of 10Ksh has been refunded by 971577 - JUKKA ENTERPRISES. Please contact 971577 - JUKKA ENTERPRISES for more information.  Your account balance is now 47Ksh.'

        info = TransactionInfo(test_message, kenya.ke_mpesa_lipampesareceiverefund_money_notification_patterns)

        self.assertEqual(info.transaction_id, "EE56TY519")
        self.assertEqual(info.received_amount, "10Ksh")
        self.assertEqual(info.sender_account, "971577 - JUKKA ENTERPRISES")
        self.assertEqual(info.balance, "47Ksh")

    def testKeMpesaSafaricomReverseMoneyNotification(self):
        test_message = 'ER30SR746 Confirmed. Transaction EQ47FM754 has been reversed.  Your account balance is now Ksh5,987.00.'

        info = TransactionInfo(test_message, kenya.ke_mpesa_safaricomreverse_money_notification_patterns)

        self.assertEqual(info.transaction_id, "EQ47FM754")
        self.assertEqual(info.balance, "Ksh5,987.00")

if __name__ == '__main__':
    unittest.main()
