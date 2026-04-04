# import smtplib
# from _datetime import datetime as dt
# import random
#
# FROM = "jrbahoutest@yahoo.com"
# TO = ["jrbahoutest@gmail.com", "rob-bastow@hotmail.com", "nbahou@rocketmail.com", "maddiecrockett@hotmail.co.uk", "calisebahou@hotmail.co.uk", "adambahou@googlemail.com", "kimmybahou@googlemail.com"]
# PASS = "uglquukxtfrvqyct"
#
# with open("quotes.txt") as f:
#     quotes_list = f.readlines()
#     random_quote = random.choice(quotes_list)
#
#
# if dt.now().weekday() == 0:
#
#     with smtplib.SMTP("smtp.mail.yahoo.com", port=587) as connection:
#         connection.ehlo()
#         connection.starttls()
#         connection.ehlo()
#         connection.login(user=FROM, password=PASS)
#         connection.sendmail(from_addr=FROM, to_addrs=TO, msg="\n"+random_quote)
#         print("\n" + random_quote)

import smtplib
from _datetime import datetime as dt

FROM = "jrbahoutest@gmail.com"
TO = "jrbahoutest@yahoo.com"
PASS = "cvjnldipskqhuxgj"


if dt.now().weekday() == 1:

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.ehlo()
        connection.starttls()
        connection.ehlo()
        connection.login(user=FROM, password=PASS)
        connection.sendmail(from_addr=FROM, to_addrs=TO, msg="\n\n\nSCHLAAAAG")
        print("email_sent")


