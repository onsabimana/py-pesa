import re

#----------------START OF TANZANIA MPESA TRANSACTION PATTERNS -------------------

# Notification when a Person is sending you money.
tz_mpesa_recieved_money_notification_patterns = {
    "transaction_id":  re.compile(r"([A-Z0-9]+)\s+Confirmed."),
    "sent_amount": None,
    "receiver_account": None,
    "balance": re.compile(r"balance\s+is\s+(Tsh\d+,\d+|Tsh\d+)"),
    "sender_account": re.compile(r"from\s+(.+?)\s+?on"),
    "received_amount": re.compile(r"received\s+(Tsh\d+,\d+|Tsh\d+)")
}


# Notifications when you send another person money
tz_mpesa_sent_money_notification_patterns = {
    "transaction_id":  re.compile(r"([A-Z0-9]+)\s+Confirmed."),
    "sent_amount": re.compile(r"(Tsh\d+,\d+|Tsh\d+)\s+sent"),
    "receiver_account": re.compile(r"to\s+(.+?)\s+?on"),
    "balance": re.compile(r"balance\s+is\s+(Tsh\d+,\d+|Tsh\d+)"),
    "sender_account": None,
    "received_amount": None
}


# Notifications when you buy Airtime for yourself
tz_mpesa_buyairtime_money_notification_patterns = {
    "transaction_id":  re.compile(r"([A-Z0-9]+)\s+confirmed."),
    "sent_amount": None,
    "receiver_account":None,
    "balance": re.compile(r"balance\s+is\s+(Tsh\d+,\d+|Tsh\d+)"),
    "sender_account": None,
    "received_amount": re.compile(r"bought\s+(Tsh\d+,\d+|Tsh\d+)")
}


# Notifications when you buy Airtime for someone else
tz_mpesa_sendairtime_money_notification_patterns = {
    "transaction_id":  re.compile(r"([A-Z0-9]+)\s+confirmed."),
    "sent_amount": re.compile(r"bought\s+(Tsh\d+,\d+|Tsh\d+)"),
    "receiver_account": re.compile(r"for\s+(.+?)\s+?on"),
    "balance": re.compile(r"balance\s+is\s+(Tsh\d+,\d+|Tsh\d+)"),
    "sender_account": None,
    "received_amount": None
}


# Notifications when you deposit money into bank
tz_mpesa_bankdeposit_money_notification_patterns = {
    "transaction_id":  re.compile(r"([A-Z0-9]+)\s+Confirmed."),
    "sent_amount": re.compile(r"(Tsh\d+,\d+|Tsh\d+)\s+sent"),
    "receiver_account": re.compile(r"for\s+account\s+(.+?)\s+?on"),
    "balance": re.compile(r"balance\s+is\s+(Tsh\d+,\d+|Tsh\d+)"),
    "sender_account": None,
    "received_amount": None
}


# Notifications when you deposit money into your mpesa account
tz_mpesa_deposit_money_notification_patterns = {
    "transaction_id":  re.compile(r"([A-Z0-9]+)\s+Confirmed."),
    "sent_amount": re.compile(r"Give\s+(Tsh\d+,\d+|Tsh\d+)"),
    "receiver_account": re.compile(r"cash\s+to\s+(.+?)\."),
    "balance": re.compile(r"balance\s+is\s+(Tsh\d+,\d+|Tsh\d+)"),
    "sender_account": None,
    "received_amount": None
}


# Notifications when you withdraw money from your account at an agent
tz_mpesa_withdraw_money_notification_patterns = {
    "transaction_id":  re.compile(r"([A-Z0-9]+)\s+Confirmed."),
    "sent_amount": None,
    "receiver_account": None,
    "balance": re.compile(r"balance\s+is\s+(Tsh\d+,\d+|Tsh\d+)"),
    "sender_account": re.compile(r"from\s+(.+?)\s+?New"),
    "received_amount": re.compile(r"Withdraw\s+(Tsh\d+,\d+|Tsh\d+)")
}


# Notifications when do a balance check
tz_mpesa_checkbalance_money_notification_patterns = {
    "transaction_id":  re.compile(r"([A-Z0-9]+)\s+Confirmed."),
    "sent_amount": None,
    "receiver_account": None,
    "balance": re.compile(r"balance\s+was\s+(Tsh\d+,\d+|Tsh\d+)"),
    "sender_account": None,
    "received_amount": None
}
#------------------END OF TANZANIA MPESA TRANSACTION PATTERNS ------------------

#----------------START OF TANZANIA TIGO TRANSACTION PATTERNS -------------------

# Notification when a Person is sending you money.
tz_tigo_recieved_money_notification_patterns = {
    "transaction_id":  re.compile(r"TxnId:\s+([A-Z0-9]+.[A-Z0-9]+.[A-Z0-9]+)"),
    "sent_amount": None,
    "receiver_account": None,
    "balance": re.compile(r"balance\s+is\s+(Tsh\s+\d+,\d+|Tsh\s+\d+)"),
    "sender_account": re.compile(r"from\s+(.+?)\."),
    "received_amount": re.compile(r"received\s+(Tsh\s+\d+,\d+|Tsh\s+\d+)")
}
