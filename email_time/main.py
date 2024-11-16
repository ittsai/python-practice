import smtplib
import datetime as dt

my_email = "test@gmail.com"
password = "1234"
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="test2@gmail.com", msg="Subject:test\n\nThis is the body")

now = dt.datetime.now()
