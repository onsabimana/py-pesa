
#----------------START OF AIRTEL TRANSACTION PATTERNS -------------------

# Notification when buy Airtime
ke_airtel_buyairtime_money_notification_patterns = {
    "transaction_id":  re.compile(r"Trans\s+\.\s+ID:\s+([A-Z0-9]+)"),
    "sent_amount": None,
    "receiver_account": None,
    "balance": re.compile(r"balance\s+is\s+(Tsh\d+,\d+|Tsh\d+)"),
    "sender_account": re.compile(r"from\s+(.+?)\s+?on"),
    "received_amount": re.compile(r"Airtime\s+of\s+(\d+,\d+|Tsh\d+)")
}
