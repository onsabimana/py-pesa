import re

sent_money_notification_patterns = {
    "transaction_id":  re.compile(r"Trans.\s+ID:\s+(\w+)"),
    "sent_amount": re.compile(r"sent\s+(\d+GHS)"),
    "receiver_account": re.compile(r"to\s+(\w+)"),
    "balance": re.compile(r"balance\s+is\s+(\d+.*\d*GHS)"),
    "sender_account": None,
    "received_amount": None
}
