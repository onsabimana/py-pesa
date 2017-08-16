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

#----------------START OF KENYA MPESA TRANSACTION PATTERNS -------------------

#Notification for when you transfer money to MPESA from your bank account
#(suspected to be a general B2C status message-REVIEW).
ke_mpesa_transfer_money_notification_patterns = {
    "transaction_id":  re.compile(r"([A-Z0-9]+)\s+Confirmed"),
    "sent_amount": None,
    "receiver_account": None,
    "balance": re.compile(r"balance\s+is\s+(Ksh\d+,\d+.\d+|Ksh\d+.\d+|Ksh\d+,\d+|Ksh\d+)"),
    "sender_account": re.compile(r"from\s+(.+?)\s+?on"),
    "received_amount": re.compile(r"received\s+(Ksh\d+,\d+.\d+|Ksh\d+.\d+|Ksh\d+,\d+|Ksh\d+)")
}

#Notification when a Person is sending you money- REVIEW
ke_mpesa_received_money_notification_patterns = {
    "transaction_id":  re.compile(r"([A-Z0-9]+)\s+Confirmed"),
    "sent_amount": None,
    "receiver_account": None,
    "balance": re.compile(r"balance\s+is\s+(Ksh\d+,\d+.\d+|Ksh\d+.\d+|Ksh\d+,\d+|Ksh\d+)"),
    "sender_account": re.compile(r"from\s+(.+?)\s+?on"),
    "received_amount": re.compile(r"received\s+(Ksh\d+,\d+.\d+|Ksh\d+.\d+|Ksh\d+,\d+|Ksh\d+)")
}

#Notifications when an error occours.
#Not sure how to capture these - REVIEW

#Notifications when depositing cash money into your mpesa account
ke_mpesa_cashdeposit_money_notification_patterns = {
    "transaction_id":  re.compile(r"([A-Z0-9]+)\s+Confirmed"),
    "sent_amount": re.compile(r"Give\s+(Ksh\d+,\d+.\d+|Ksh\d+.\d+|Ksh\d+,\d+|Ksh\d+)"),
    "receiver_account": re.compile(r"cash\s+to\s+(.+?)\s+?New"),
    "balance": re.compile(r"balance\s+is\s+(Ksh\d+,\d+.\d+|Ksh\d+.\d+|Ksh\d+,\d+|Ksh\d+)"),
    "sender_account": None,
    "received_amount": None
}

#Notifications when withdrawing money from you account at an agent
ke_mpesa_withdraw_money_notification_patterns = {
    "transaction_id":  re.compile(r"([A-Z0-9]+)\s+Confirmed"),
    "sent_amount": re.compile(r"Withdraw\s+(Ksh\d+,\d+.\d+|Ksh\d+.\d+|Ksh\d+,\d+|Ksh\d+)"),
    "receiver_account": re.compile(r"from\s+(.+?)\s+?New"),
    "balance": re.compile(r"balance\s+is\s+(Ksh\d+,\d+.\d+|Ksh\d+.\d+|Ksh\d+,\d+|Ksh\d+)"),
    "sender_account": None,
    "received_amount": None
}

#Notifications when you send another person money
ke_mpesa_send_money_notification_patterns = {
    "transaction_id":  re.compile(r"([A-Z0-9]+)\s+Confirmed"),
    "sent_amount": re.compile(r"(Ksh\d+,\d+.\d+|Ksh\d+.\d+|Ksh\d+,\d+|Ksh\d+)\s+sent"),
    "receiver_account": re.compile(r"to\s+(.+?)\s+?on"),
    "balance": re.compile(r"balance\s+is\s+(Ksh\d+,\d+.\d+|Ksh\d+.\d+|Ksh\d+,\d+|Ksh\d+)"),
    "sender_account": None,
    "received_amount": None
}

#Notifications when you buy Airtime for yourself
ke_mpesa_buyairtime_money_notification_patterns = {
    "transaction_id":  re.compile(r"([A-Z0-9]+)\s+confirmed"),
    "sent_amount": None,
    "receiver_account": None,
    "balance": re.compile(r"balance\s+is\s+(Ksh\d+,\d+.\d+|Ksh\d+.\d+|Ksh\d+,\d+|Ksh\d+)"),
    "sender_account": re.compile(r"from\s+([A-Z0-9]+)"),
    "received_amount": re.compile(r"bought\s+(Ksh\d+,\d+.\d+|Ksh\d+.\d+|Ksh\d+,\d+|Ksh\d+)")
}

#Notification when you do a balance request
ke_mpesa_balancecheck_money_notification_patterns = {
    "transaction_id":  re.compile(r"([A-Z0-9]+)\s+Confirmed"),
    "sent_amount": None,
    "receiver_account": None,
    "balance": re.compile(r"balance\s+was\s+(Ksh\d+,\d+.\d+|Ksh\d+.\d+|Ksh\d+,\d+|Ksh\d+)"),
    "sender_account": re.compile(r"from\s+([A-Z0-9]+)"),
    "received_amount": None,
}

#Notification when you pay to a paybill number
ke_mpesa_paybill_money_notification_patterns = {
    "transaction_id":  re.compile(r"([A-Z0-9]+)\s+Confirmed"),
    "sent_amount": re.compile(r"(Ksh\d+,\d+.\d+|Ksh\d+.\d+|Ksh\d+,\d+|Ksh\d+)\s+sent"),
    "receiver_account": re.compile(r"for\s+account\s+(.+?)\s+?on"),
    "balance": re.compile(r"balance\s+is\s+(Ksh\d+,\d+.\d+|Ksh\d+.\d+|Ksh\d+,\d+|Ksh\d+)"),
    "sender_account":None,
    "received_amount": None
}

#Notification when a buygoods number receives a payment.
ke_mpesa_buygoodsreceieve_money_notification_patterns = {
    "transaction_id":  re.compile(r"([A-Z0-9]+)\s+Confirmed"),
    "sent_amount": None,
    "receiver_account": None,
    "balance": re.compile(r"balance\s+is\s+(Ksh\d+,\d+.\d+|Ksh\d+.\d+|Ksh\d+,\d+|Ksh\d+)"),
    "sender_account":re.compile(r"from\s+(.+?)\."),
    "received_amount": re.compile(r"(Ksh\d+,\d+.\d+|Ksh\d+.\d+|Ksh\d+,\d+|Ksh\d+)\s+received")
}

#Notification when you transfer to your M-Shwari account.
ke_mpesa_mshwaritransfer_money_notification_patterns = {
    "transaction_id":  re.compile(r"([A-Z0-9]+)\s+Confirmed"),
    "sent_amount": re.compile(r"(Ksh\d+,\d+.\d+|Ksh\d+.\d+|Ksh\d+,\d+|Ksh\d+)\s+transferred"),
    "receiver_account": re.compile(r"to\s+(.+?)\s+?account"),
    "balance": re.compile(r"M-PESA\s+balance\s+is\s+(Ksh\d+,\d+.\d+|Ksh\d+.\d+|Ksh\d+,\d+|Ksh\d+)"),
    "sender_account":None,
    "received_amount": None
}

#Notification when you transfer from your M-Shwari account.
ke_mpesa_mshwarireceive_money_notification_patterns = {
    "transaction_id":  re.compile(r"([A-Z0-9]+)\s+Confirmed"),
    "sent_amount": None,
    "receiver_account": None,
    "balance": re.compile(r"M-PESA\s+balance\s+is\s+(Ksh\d+,\d+.\d+|Ksh\d+.\d+|Ksh\d+,\d+|Ksh\d+)"),
    "sender_account":re.compile(r"from\s+your\s+(.+?)\s+?account"),
    "received_amount": re.compile(r"transferred\s+(Ksh\d+,\d+.\d+|Ksh\d+.\d+|Ksh\d+,\d+|Ksh\d+)")
}

#Notification when you receive a refund for a transaction you had paid to a "lipa na mpesa" account.
ke_mpesa_lipampesareceiverefund_money_notification_patterns = {
    "transaction_id":  re.compile(r"([A-Z0-9]+)\s+confirmed"),
    "sent_amount": None,
    "receiver_account": None,
    "balance": re.compile(r"balance\s+is\s+now\s+(\d+,\d+.\d+Ksh|\d+.\d+Ksh|\d+,\d+Ksh|\d+Ksh)"),
    "sender_account":re.compile(r"refunded\s+by\s+(.+?)\."),
    "received_amount": re.compile(r"[A-Z0-9]+\s+of\s+(\d+,\d+.\d+Ksh|\d+.\d+Ksh|\d+,\d+Ksh|\d+Ksh)")
}

#Notification when safaricom reverses a transaction that came to your account.
ke_mpesa_safaricomreverse_money_notification_patterns = {
    "transaction_id":  re.compile(r"Transaction\s+([A-Z0-9]+)"),
    "sent_amount": None,
    "receiver_account": None,
    "balance": re.compile(r"balance\s+is\s+now\s+(Ksh\d+,\d+.\d+|Ksh\d+.\d+|Ksh\d+,\d+|Ksh\d+)"),
    "sender_account":None,
    "received_amount": None
}
