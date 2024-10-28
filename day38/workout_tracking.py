import os
from datetime import datetime

import requests
from dotenv import load_dotenv

load_dotenv()

TODAY = datetime.now().strftime("%d/%m/%Y")
TIME = datetime.now().strftime("%H:%M:%S")


NUTRI_API_KEY = os.getenv("NUTRI_API_KEY")
NUTRI_API_ID = os.getenv("NUTRI_API_ID")

nutri_headers = {"x-app-id": NUTRI_API_ID, "x-app-key": NUTRI_API_KEY}

nutri_endpoint = "https://trackapi.nutritionix.com"


def main():
    nl_exercise_end = f"{nutri_endpoint}/v2/natural/exercise"

    nl_exercise_data = {"query": "ran 5k and cycled for 20 minutes."}

    nl_exercise_res = requests.post(
        url=nl_exercise_end, json=nl_exercise_data, headers=nutri_headers
    )

    data = nl_exercise_res.json()["exercises"]
    # print(nl_exercise_res.url)
    # print(data)

    for exercise in data:
        sheety_data = {
            "workout": {
                "date": TODAY,
                "time": TIME,
                "exercise": exercise["name"],
                "duration": exercise["duration_min"],
                "calories": exercise["nf_calories"],
            }
        }
        print(sheety_data)
        # print()

        sheety_res = requests.post(
            url="https://api.sheety.co/277de229be71c56ad43922d159436bac/copyOfMyWorkouts/workouts",
            json=sheety_data,
        )

        # print(sheety_res.text)
        # for e in exercise:
        #     print(e)
        #     print()


if __name__ == "__main__":
    main()
