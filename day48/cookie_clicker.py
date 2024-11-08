import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")


store = driver.find_element(By.CSS_SELECTOR, "#store")

all_item_divs = store.find_elements(By.TAG_NAME, "div")
all_item_divs.pop()

item_ids = [div.get_attribute("id") for div in all_item_divs]
# print(item_ids)

timeout = time.time() + 15
five_min = time.time() + 60 * 8

while True:
    cookie.click()

    if time.time() > timeout:
        all_prices = driver.find_elements(By.CSS_SELECTOR, "#store>div b")

        item_prices = []
        # Add error handling for each price
        for cost in all_prices:
            try:
                if cost.text:  # Check if there's any text
                    price = int(cost.text.split()[-1].replace(",", ""))
                    item_prices.append(price)
            except (IndexError, ValueError):
                continue
        # print(item_prices)

        money = int((driver.find_element(By.ID, "money").text).replace(",", ""))

        most_affordable = 0
        for i in range(len(item_prices)):
            if money > item_prices[i]:
                most_affordable = i

        # print(most_affordable)
        # print(item_ids)
        # print(item_ids[most_affordable])
        driver.find_element(By.CSS_SELECTOR, f"#{item_ids[most_affordable]}").click()

        timeout = time.time() + 15
