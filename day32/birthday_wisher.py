import datetime as dt
import random as rd
import smtplib

import pandas as pd

LETTER_PATHS = [
    "day32/letter_templates/letter_1.txt",
    "day32/letter_templates/letter_2.txt",
    "day32/letter_templates/letter_3.txt",
]
EMAIL = ""
PASSWORD = ""
# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
birthdays = pd.read_csv("day32/birthdays.csv")
b_info = {
    row["name"]: {"email": row.email, "month": row.month, "day": row.day}
    for index, row in birthdays.iterrows()
}

today = dt.datetime.now()
t_day = today.day
t_month = today.month


for name in b_info:
    if b_info[name]["month"] == t_month and b_info[name]["day"] == t_day:
        with open(rd.choice(LETTER_PATHS)) as letter:
            letter.seek(0)
            message = letter.readlines()
            message[0] = message[0].replace("[NAME]", f"{name}")
            letter.seek(0)
            m_formatted = ""
            for ltr in message:
                m_formatted += ltr

            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=EMAIL, password=PASSWORD)
                connection.sendmail(
                    from_addr=EMAIL,
                    to_addrs="",
                    msg=f"Subject:Motivation From Bro!\n\n{m_formatted}",
                )


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
