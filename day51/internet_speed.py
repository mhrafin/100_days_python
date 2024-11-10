import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class InternetSpeedTwitterBot:
    def __init__(self) -> None:
        self.driver = webdriver.Firefox()
        self.down = None
        self.up = None

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        self.driver.find_element(By.CSS_SELECTOR, ".start-text").click()

        time.sleep(60)
        # wait = WebDriverWait(self.driver, 40)
        # wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "close-btn")))

        self.driver.find_element(
            By.XPATH,
            "/html/body/div[3]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/div/div[2]/a",
        ).click()

        self.down = self.driver.find_element(By.CSS_SELECTOR, ".download-speed").text
        self.up = self.driver.find_element(By.CSS_SELECTOR, ".upload-speed").text

    def tweet_at_provider(self):
        self.driver.get("https://x.com/")
        self.driver.find_element(By.LINK_TEXT, "Sign in").click()
        time.sleep(3)
        email = self.driver.find_element(By.TAG_NAME, "input")
        email.send_keys("@gmail.com")

        self.driver.find_element(
            By.XPATH,
            "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]",
        ).click()
        
        time.sleep(3)
        username = self.driver.find_element(By.TAG_NAME, "input")
        username.send_keys("")

        self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/button").click()


        time.sleep(3)
        password = self.driver.find_element(
            By.XPATH,
            "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input",
        )
        password.send_keys('')

        self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button").click()
        time.sleep(10)

        post_input = self.driver.find_element(By.CSS_SELECTOR, ".notranslate")

        post_input.send_keys(f"{self.down}/{self.up}")
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button").click()


bot = InternetSpeedTwitterBot()

bot.get_internet_speed()
bot.tweet_at_provider()

print(bot.down)
print(bot.up)

