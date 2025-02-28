import  smtplib, ssl

host = "smtp.gmail.com"
port = 465

username = "test@test.com"
password = "1234"

receiver = "test2@test.com"
context = ssl.create_default_context()

message =""" Hi """

with smtplib.SMTP_SSL(host, port, context=context) as sever:
    sever.login(username, password)
    sever.sendmail(username, receiver, message)