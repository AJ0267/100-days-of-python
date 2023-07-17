# import smtplib

# gmail = smtp.gmail.com
# hotmail = smtp.live.com
# yahoo = smtp.mail.yahoo.com

# my_email = ""
# password = ""


# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user= my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="xyz@gmail.com", msg="hello")
#add \n\n to access body of email.
#connection.close() avoid using this with help of "With".

# import datetime as dt
# now = dt.datetime.now()
# print(now.day) #year, month, week, day, hour, minute, seconds, 
# day_of_week = now.weekday()
# print(day_of_week)

# date_of_birth = dt.datetime(year=2002, month=7, day=26)
# print(date_of_birth)