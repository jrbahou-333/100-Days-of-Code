##################### Extra Hard Starting Project ######################
import pandas
import datetime as dt
import smtplib

FROM = "jrbahoutest@yahoo.com"
TO = "jrbahou@gmail.com"
PASS = "uglquukxtfrvqyct"

target_date = dt.datetime.now() + dt.timedelta(days=5)
target_date_UTC = target_date.
print(target_date_UTC)
target_month = target_date
target_day = target_date.day
target_year = target_date.year

letter_text = ""


def gen_letter():
    with open("letter_templates/letter_1.txt", mode="r") as f:
        global letter_text
        letter_text = f.read()
        letter_text = letter_text.replace("[NAME]", record["name"])
        letter_text = letter_text.replace("[DATE]", f"{str(record['day'])}/{str(record['month'])}")
        letter_text = letter_text.replace("[AGE]", str(target_year - record['year']))



def send_letter():
    with smtplib.SMTP("smtp.mail.yahoo.com", port=587) as connection:
        connection.ehlo()
        connection.starttls()
        connection.ehlo()
        connection.login(user=FROM, password=PASS)
        connection.sendmail(from_addr=FROM, to_addrs=TO, msg=f"Subject: Birthday Reminder \n\n\n {letter_text}")
        print("Letter sent")


birthdays = pandas.read_csv("birthdays.csv")
birthday_dict = birthdays.to_dict(orient="records")
print(birthday_dict)

for record in birthday_dict:
    if record["month"] == target_month and record["day"] == target_day:
        gen_letter()
        send_letter()
