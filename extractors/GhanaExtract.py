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

    def __init__(self, transaction_message, patterns):
        super(TransactionInfo, self).__init__()
        self.transaction_message = transaction_message
        self.keys = (
            "transaction_id",
            "sent_amount",
            "sender_account",
            "received_amount",
            "receiver_account",
            "balance",
        )

        for k in self.keys:
            if k not in patterns:
                raise ValueError("{0} must be keys to your pattern. Missing {1}".format(self.keys, k))

        self.info_patterns = patterns

    def extract_info_from_message(self, info_key):
        if self.info_patterns[info_key] is not None:
            info = self.info_patterns[info_key].findall(self.transaction_message)
            return info[0] if info else ""
        else:
            return ""

    @property
    def transaction_id(self):
        return self.extract_info_from_message("transaction_id")

    @property
    def sent_amount(self):
        return self.extract_info_from_message("sent_amount")

    @property
    def sender_account(self):
        return self.extract_info_from_message("sender_account")

    @property
    def received_amount(self):
        return self.extract_info_from_message("received_amount")

    @property
    def receiver_account(self):
        return self.extract_info_from_message("receiver_account")

    @property
    def balance(self):
        return self.extract_info_from_message("balance")

