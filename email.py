import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

your_addrs = "YourEmailAddress@gmail.com" # Later this would be input string of your email addresss
tothesent_addrs = "EmailAddressYouAreSendingThisTo@email.com"

msg = MIMEMultipart()
msg['From'] = your_addrs
msg['To'] = tothesent_addrs
msg['Subject'] = "Reminder:"


while True:
    if ((datetime.date.today().strftime('%A') == 'Sunday') and ((datetime.datetime.now().time().strftime('%H') == '23') and (datetime.datetime.now().time().strftime('%M') == '50') and (datetime.datetime.now().time().strftime('%S') == '01')) ):
        body = "TESTING EMAIL"
        msg.attach(MIMEText(body, 'plain'))
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(your_addrs, "YourPASSWORD")
        text = msg.as_string()
        server.sendmail(your_addrs, tothesent_addrs, text)
        server.quit()

