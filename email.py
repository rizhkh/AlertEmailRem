import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText


your_addrs = "YourEmailAddress@gmail.com" # Later this would be input string of your email addresss
tothesent_addrs = "EmailAddressYouAreSendingThisTo@email.com"


msg = MIMEMultipart()
msg['From'] = your_addrs
msg['To'] = tothesent_addrs
msg['Subject'] = "Reminder:"

body = "TESTING EMAIL"
msg.attach(MIMEText(body, 'plain'))

