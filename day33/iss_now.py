import requests
from datetime import datetime
import smtplib

MY_LAT = 23.855249
MY_LONG = 90.382440


def iss_above_me():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()

    longitude = float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])

    if latitude > (MY_LAT - 5) or longitude < (MY_LAT + 5):
        if longitude > (MY_LONG - 5) or longitude < (MY_LONG + 5):
            return True

    return False


def night_now():
    parameters = {"lat": MY_LAT, "lng": MY_LONG, "formatted": 0, "tzid": "Asia/Dhaka"}

    res_sun = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    res_sun.raise_for_status()

    sun_data = res_sun.json()["results"]

    sunrise = sun_data["sunrise"].split("T")[1].split(":")[0]
    sunset = sun_data["sunset"].split("T")[1].split(":")[0]

    current_hour = datetime.now().hour

    if current_hour < sunrise or current_hour > sunset:
        return True

    return False


def main():
    if iss_above_me and night_now:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user="", password="")
            connection.sendmail(from_addr="", to_addrs="", msg="")


if __name__ == "__main__":
    main()
