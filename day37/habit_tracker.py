import os
from datetime import datetime

import requests
from dotenv import load_dotenv

load_dotenv()

TODAY = str(datetime.now().date()).replace("-", "")


PIXELA_TOKEN = os.getenv("PIXELA_TOKEN")

GRAPH_ID = "graph3"
USERNAME = "raf"

pixela_endpoint = "https://pixe.la/v1/users"

user_data = {
    "token": PIXELA_TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# new_user_res = requests.post(url=pixela_endpoint, json=user_data)
# print(new_user_res.json())

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Reading Quran",
    "unit": "Page",
    "type": "int",
    "color": "momiji",
}

token_header = {"X-USER-TOKEN": "bad"}

# graph_res = requests.post(url=graph_endpoint, json=graph_config, headers=token_header)
# # graph_res.raise_for_status()
# print(graph_res.json())

post_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

post_pixel_data = {"date": TODAY, "quantity": "4"}

# post_pixel_res = requests.post(
#     url=post_pixel_endpoint, json=post_pixel_data, headers=token_header
# )
# print(post_pixel_res.text)
# print(post_pixel_res.url)

upd_pixel_endp = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{TODAY}"

upd_pixel_data = {"quantity": "4"}

# upd_pixel_res = requests.put(
#     url=upd_pixel_endp, json=upd_pixel_data, headers=token_header
# )
# print(upd_pixel_res)
