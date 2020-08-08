import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os.path
email = 'taskmessage.21@gmail.com'
password = 'prakash.s@123'
send_to_email = 'rajpurohitprakash04@gmail.com'
subject = '!!! Testing Server Report !!!'
message = "Server is not working,please debug the code"

msg = MIMEMultipart()

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email, password)
text = msg.as_string()
server.sendmail(email, send_to_email, text)
server.quit()
