import re


class TransactionInfo(object):
    """
        key information to extract from a transaction message:

        - transaction_id
        - sent_mount
        - sender_account
        - received_amount
        - receiver_account
        - balance

        :param transaction_message:
        :type string:
    """

    def __init__(self, transaction_message):
        super(TransactionInfo, self).__init__()
        self.transaction_message = transaction_message

    @property
    def transaction_id(self):
        raise NotImplementedError

    @property
    def sent_amount(self):
        raise NotImplementedError

    @property
    def sender_account(self):
        raise NotImplementedError

    @property
    def received_amount(self):
        raise NotImplementedError

    @property
    def receiver_account(self):
        raise NotImplementedError

    @property
    def balance(self):
        raise NotImplementedError


class SentMoneyNotification(TransactionInfo):
    def __init__(self, transaction_message):
        super(SentMoneyNotification, self).__init__(transaction_message)

        self.info_patterns = {
            "transaction_id":  re.compile(r"Trans.\s+ID:\s+(\w+)"),
            "sent_amount": re.compile(r"sent\s+(\d+GHS)"),
            "receiver_account": re.compile(r"to\s+(\w+)"),
            "balance": re.compile(r"balance\s+is\s+(\d+.*\d*GHS)")
        }

    def extract_info_from_transaction(self, info_key):
        info = self.info_patterns[info_key].findall(self.transaction_message)
        return info[0] if info else ""

    @property
    def transaction_id(self):
        return self.extract_info_from_transaction("transaction_id")

    @property
    def sent_amount(self):
        return self.extract_info_from_transaction("sent_amount")

    @property
    def sender_account(self):
        return ""

    @property
    def received_amount(self):
        return ""

    @property
    def receiver_account(self):
        return self.extract_info_from_transaction("receiver_account")

    @property
    def balance(self):
        return self.extract_info_from_transaction("balance")
