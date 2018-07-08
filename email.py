import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

your_addrs = "YourEmailAddress@gmail.com" # Later this would be input string of your email addresss
tothesent_addrs = "EmailAddressYouAreSendingThisTo@email.com"

msg = MIMEMultipart()
msg['From'] = your_addrs
msg['To'] = tothesent_addrs
msg['Subject'] = "Reminder:"


if ((datetime.date.today().strftime('%A') == 'Saturday') and (atetime.datetime.now().time() == '22:26:00.000000') ):
    body = "TESTING EMAIL"
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(your_addrs, "lahore101")
    text = msg.as_string()
    server.sendmail(your_addrs, tothesent_addrs, text)
    server.quit()
