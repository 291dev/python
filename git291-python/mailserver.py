from email import message
import smtplib

smtp_server = "smtp.gmail.com"
smtp_port = 587

from_email = '291dev@gmail.com'
to_email = '291dev@gmail.com'
username = '291dev'
password = 'f2914486'

msg = message.EmailMessage()
msg.set_content('Test email')
msg['Subject'] = 'Test email sub'
msg['From'] = from_email
msg['To'] = [to_email, 'yoshiharu.fu.1997@gmail.com']
server = smtplib.SMTP(smtp_server, smtp_port)
server.ehlo()
server.starttls()
server.ehlo()
server.login(username, password)
server.send_message(msg)
server.quit()