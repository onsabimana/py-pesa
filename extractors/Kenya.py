import re

#----------------START OF KENYA AIRTEL TRANSACTION PATTERNS -------------------

# Notification when buy Airtime for yourself
ke_airtel_buyairtime_money_notification_patterns = {
    "transaction_id":  re.compile(r"Trans\.\s+ID:\s+([A-Z0-9]+)"),
    "sent_amount": None,
    "receiver_account": None,
    "balance": None,
    "sender_account": None,
    "received_amount": re.compile(r"Airtime\s+of\s+(\d+,\d+.\d+Ksh|\d+.\d+Ksh|\d+,\d+Ksh|\d+Ksh)")
}

#Notification when a Person is sending you money.
ke_airtel_received_money_notification_patterns = {
    "transaction_id":  re.compile(r"Trans\.\s+ID:\s+([A-Z0-9]+)"),
    "sent_amount": None,
    "receiver_account": None,
    "balance": re.compile(r"balance\s+is\s+(\d+,\d+.\d+Ksh|\d+.\d+Ksh|\d+,\d+Ksh|\d+Ksh)"),
    "sender_account": re.compile(r"from\s+(.+?)\."),
    "received_amount": re.compile(r"received\s+(\d+,\d+.\d+Ksh|\d+.\d+Ksh|\d+,\d+Ksh|\d+Ksh)")
}

#Notifications when you send another person money
ke_airtel_send_money_notification_patterns = {
    "transaction_id":  re.compile(r"Trans\.\s+ID:\s+([A-Z0-9]+)"),
    "sent_amount": re.compile(r"sent\s+(\d+,\d+.\d+Ksh|\d+.\d+Ksh|\d+,\d+Ksh|\d+Ksh)"),
    "receiver_account": re.compile(r"to\s+(.+?)\."),
    "balance": re.compile(r"balance\s+is\s+(\d+,\d+.\d+Ksh|\d+.\d+Ksh|\d+,\d+Ksh|\d+Ksh)"),
    "sender_account": None,
    "received_amount": None
}

#Notification when you pay to a paybill number
ke_airtel_paybill_money_notification_patterns = {
    "transaction_id":  re.compile(r"Trans\.\s+ID:\s+([A-Z0-9]+)"),
    "sent_amount": re.compile(r"sent\s+(\d+,\d+.\d+Ksh|\d+.\d+Ksh|\d+,\d+Ksh|\d+Ksh)"),
    "receiver_account": re.compile(r"to\s+(.+?)\s+?in\s+reference"),
    "balance": re.compile(r"balance\s+is\s+(\d+,\d+.\d+Ksh|\d+.\d+Ksh|\d+,\d+Ksh|\d+Ksh)"),
    "sender_account": None,
    "received_amount": None
}

#Notifications when depositing cash money into your account
ke_airtel_cashdeposit_money_notification_patterns = {
    "transaction_id":  re.compile(r"Trans\.\s+ID:\s+([A-Z0-9]+)"),
    "sent_amount": None,
    "receiver_account": None,
    "balance": re.compile(r"balance\s+is\s+(\d+,\d+.\d+Ksh|\d+.\d+Ksh|\d+,\d+Ksh|\d+Ksh)"),
    "sender_account": re.compile(r"from\s+(.+?)\."),
    "received_amount": re.compile(r"received\s+(\d+,\d+.\d+Ksh|\d+.\d+Ksh|\d+,\d+Ksh|\d+Ksh)")
}

#Notification when you do a balance request - DO WE NEED THIS ONE !!
ke_airtel_balancecheck_money_notification_patterns = {
    "transaction_id": None,
    "sent_amount": None,
    "receiver_account": None,
    "balance": re.compile(r"bal.\s+is\s+(Ksh\d+,\d+.\d+|Ksh\d+.\d+|Ksh\d+,\d+|Ksh\d+)"),
    "sender_account": None,
    "received_amount": None
}

#Notifications when an error occours. - NOT SURE IF WE NEED THIS, BUT MAYBE USEFUL FOR ANALYTICAL PURPOSES
ke_airtel_error_money_notification_patterns = {
    "transaction_id": None,
    "sent_amount": re.compile(r"amount\s+of\s+(\d+,\d+.\d+Ksh|\d+.\d+Ksh|\d+,\d+Ksh|\d+Ksh)"),
    "receiver_account": None,
    "balance": None,
    "sender_account": None,
    "received_amount": None
}
#----------------END OF KENYA AIRTEL TRANSACTION PATTERNS -------------------
