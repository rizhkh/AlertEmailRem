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

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(your_addrs, "PASSWORD")
text = msg.as_string()
server.sendmail(your_addrs, tothesent_addrs, text)
server.quit()
