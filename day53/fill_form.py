import time

from get_data import DataFromZillow
from selenium import webdriver
from selenium.webdriver.common.by import By


class FormFillup:
    def __init__(self) -> None:
        self.data = DataFromZillow()

        self.driver = webdriver.Firefox()

        self.driver.get("https://forms.gle/57D6wCawfBcxdZyVA")

        self.fill_entry()

        # self.inputs[0].find_element(By.TAG_NAME, "input").send_keys(self.data.addresses[0])
        # self.inputs[1].find_element(By.TAG_NAME, "input").send_keys(self.data.prices[0])
        # self.inputs[2].find_element(By.TAG_NAME, "input").send_keys(self.data.links_to[0])

        # submit_btn = self.driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div")
        # submit_btn.click()
        # time.sleep(3)

        # again_btn = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div[4]/a")
        # again_btn.click()

        # print(inputs)

    def fill_entry(self):
        for n in range(len(self.data.addresses)):
            self.inputs = self.driver.find_elements(By.CLASS_NAME, "AgroKb")
            self.inputs[0].find_element(By.TAG_NAME, "input").send_keys(
                self.data.addresses[n]
            )
            self.inputs[1].find_element(By.TAG_NAME, "input").send_keys(
                self.data.prices[n]
            )
            self.inputs[2].find_element(By.TAG_NAME, "input").send_keys(
                self.data.links_to[n]
            )

            submit_btn = self.driver.find_element(
                By.XPATH,
                "/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div",
            )
            submit_btn.click()
            time.sleep(3)

            again_btn = self.driver.find_element(
                By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div[4]/a"
            )
            again_btn.click()
            time.sleep(3)


form_fillup = FormFillup()
