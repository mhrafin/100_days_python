from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

# driver.get("https://en.wikipedia.org/wiki/Main_Page")

# total_articles = driver.find_element(By.CSS_SELECTOR, value="#articlecount a").text

# print(total_articles)

# driver.quit()

driver.get("http://secure-retreat-92358.herokuapp.com/")

fname = driver.find_element(By.NAME, "fName")

fname.send_keys("Rafin")

lname = driver.find_element(By.NAME, "lName")

lname.send_keys("Rafinlast")


email = driver.find_element(By.NAME, "email")

email.send_keys("Rafinlast@gmail.com")

sign_up_btn = driver.find_element(By.CSS_SELECTOR, ".btn")
sign_up_btn.click()

