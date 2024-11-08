from pprint import pp

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("https://www.python.org/")

event_widget = driver.find_element(By.CSS_SELECTOR, value=".event-widget")

events = event_widget.find_elements(by=By.TAG_NAME, value="li")

print(events)

events_dict = {}
for i, event in enumerate(events):
    time = event.find_element(By.TAG_NAME, value="time").text
    event_name = event.find_element(By.TAG_NAME, value="a").text
    events_dict[i] = {"time": f"{time}", "name": f"{event_name}"}

pp(events_dict)
driver.quit()
