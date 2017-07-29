import re

#Notification when a Person is sending you money.
tz_mpesa_recieved_money_notification_patterns = {
    "transaction_id":  re.compile(r"([A-Z0-9]+)\s+Confirmed."),
    "sent_amount": None,
    "receiver_account": None,
    "balance": re.compile(r"balance\s+is\s+(Tsh\d+,\d+|Tsh\d+)"),
    "sender_account": re.compile(r"from\s+(.+?)\s+?on"),
    "received_amount": re.compile(r"received\s+(Tsh\d+,\d+|Tsh\d+)")
}
#Notifications when you send another person money
tz_mpesa_sent_money_notification_patterns = {
    "transaction_id":  re.compile(r"([A-Z0-9]+)\s+Confirmed."),
    "sent_amount": re.compile(r"(Tsh\d+,\d+|Tsh\d+)\s+sent"),
    "receiver_account": re.compile(r"to\s+(.+?)\s+?on"),
    "balance": re.compile(r"balance\s+is\s+(Tsh\d+,\d+|Tsh\d+)"),
    "sender_account": None,
    "received_amount": None
}
#Notifications when you buy Airtime for yourself
tz_mpesa_buyAirtime_money_notification_patterns = {
    "transaction_id":  re.compile(r"([A-Z0-9]+)\s+confirmed."),
    "sent_amount": None,
    "receiver_account":None,
    "balance": re.compile(r"balance\s+is\s+(Tsh\d+,\d+|Tsh\d+)"),
    "sender_account": None,
    "received_amount": re.compile(r"bought\s+(Tsh\d+,\d+|Tsh\d+)")
}
