#Monday Motivation Project
import datetime as dt
import random
from email.mime.text import MIMEText
import smtplib

MY_EMAIL = "leviwilsonestevez2017@gmail.com"
MY_PASSWORD = "l3viwils0nov99Xp19"

now = dt.datetime.now()
weekday = now.weekday()
if weekday != 1:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        html = open("Template.html")
        msg = MIMEText(html.read(), 'html')
        msg['From'] = MY_EMAIL
        msg['To'] = "leviwilsonestevez2017@gmail.com"
        msg['Subject'] = f"Subject:Monday Motivation\n\n{quote}"
        text = msg.as_string()
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=text
        )
        connection.quit()

## Sending Email with Python
# import smtplib
#
# my_email = "appbreweryinfo@gmail.com"
# password = "abcd1234()"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="appbrewerytesting@yahoo.com",
#         msg="Subject:Hello\n\nThis is the body of my email."
#     )


## Working with date and time in Python
# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)
#
# date_of_birth = dt.datetime(year=1995, month=12, day=15, hour=4)
# print(date_of_birth)
