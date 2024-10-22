import random as rd
import smtplib

EMAIL = ""
PASSWORD = ""

emails = [
    
]

with open("day32/quotes.txt") as quotes_file:
    quotes_list = [line.replace("\n", "") for line in quotes_file.readlines()]

with open("day32/day.txt") as day_file:
    day = int(day_file.read())


for em in emails:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=em,
            msg=f"Subject:Motivation From Bro!\n\nDaily Motivation For The Next {day} days!\n{rd.choice(quotes_list)}",
        )

day -= 1

with open("day32/day.txt", mode="w") as day_file:
    day_file.write(str(day))
