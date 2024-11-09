import os
import time

from dotenv import load_dotenv
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait

load_dotenv()

EMAIL = os.getenv("FAKE_EMAIL")
PASSWORD = os.getenv("FAKE_PASS")
driver = webdriver.Firefox()
# https://www.linkedin.com/jobs/search/?currentJobId=4061055333&f_AL=true&geoId=106215326&keywords=Python%20developer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&sortBy=R

went_in = False
while went_in is False:
    try:
        time.sleep(2)
        driver.get(
            "https://www.linkedin.com/jobs/search/?currentJobId=4061055333&f_AL=true&geoId=106215326&keywords=Python%20developer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&sortBy=R"
        )
        # wait = WebDriverWait(driver, 10)
        # wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".sign-in-modal__outlet-btn")))
        driver.find_element(By.CSS_SELECTOR, ".sign-in-modal__outlet-btn")
        went_in = True
        # time.sleep(2)
    except NoSuchElementException:
        continue
time.sleep(1)


def close():
    driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss").click()

    try:
        driver.find_element(By.CLASS_NAME, "artdeco-modal__confirm-dialog-btn").click()
    except NoSuchElementException:
        return


driver.find_element(By.CSS_SELECTOR, ".sign-in-modal__outlet-btn").click()
time.sleep(1)

email_input = driver.find_element(By.CSS_SELECTOR, "#base-sign-in-modal_session_key")
email_input.send_keys(EMAIL)

password_input = driver.find_element(
    By.CSS_SELECTOR, "#base-sign-in-modal_session_password"
)
password_input.send_keys(PASSWORD)

sign_in_btn = driver.find_element(
    By.CSS_SELECTOR, ".sign-in-form__submit-btn--full-width"
).click()
time.sleep(1)


try:
    verification = driver.find_element(By.XPATH, "/html/body/div/main/h1")
    if verification.text != "Let’s do a quick security check":
        raise NoSuchElementException
    time.sleep(10)
except NoSuchElementException:
    pass

time.sleep(7)
# jobs_section = driver.find_element(By.CSS_SELECTOR, ".jobs-search-results-list")

jobs_list = driver.find_elements(
    by=By.CSS_SELECTOR, value=".job-card-container--clickable"
)


def single_page():
    try:
        submit_application = driver.find_element(By.CSS_SELECTOR, "footer button")
        print("submit button found")
        print("single page apply")

        mobile_input = driver.find_element(
            By.CLASS_NAME,
            "artdeco-text-input--input",
        )
        mobile_input.clear()
        mobile_input.send_keys("012345678911")

        submit_application.click()
        time.sleep(2)
        close()
    except NoSuchElementException:
        close()


for job in jobs_list:
    job.click()
    time.sleep(1)

    try:
        easy_apply_btn = driver.find_element(By.CLASS_NAME, "jobs-apply-button").click()
        print("easy button found and clicked\n")
        time.sleep(1)
    except NoSuchElementException:
        print("easy button not found\n")
        continue

    try:
        next_btn = driver.find_element(By.CSS_SELECTOR, "footer button")
        if next_btn.text == "Submit Application":
            single_page()
            continue
        print("next button found")
        print("multi stage apply")

        mobile_input = driver.find_element(
            By.CLASS_NAME,
            "artdeco-text-input--input",
        )
        mobile_input.clear()
        mobile_input.send_keys("012345678911")

        next_btn.click()
        print("next clicked once")
        # time.sleep(1)
        try:
            next_btn.click()
            print("next clicked twice")
        except:
            raise NoSuchElementException
        # time.sleep(1)

        inputs = driver.find_elements(By.TAG_NAME, "input")
        print(len(inputs))

        age_input = inputs[0]
        age_input.send_keys("25")

        salary_expect_input = inputs[1]
        try:
            salary_expect_input.send_keys("15000")
        except:
            raise NoSuchElementException

        review_btn = driver.find_element(
            By.XPATH,
            "/html/body/div[4]/div/div/div[2]/div/div[2]/form/footer/div[2]/button[2]/span",
        ).click()
        print("review button clicked!")
        time.sleep(1)

        footer_btns = driver.find_elements(By.CSS_SELECTOR, "footer button")
        submit_application = footer_btns[1].click()
        print("submit button clicked")
        time.sleep(2)

        close()
        continue
    except NoSuchElementException:
        close()

    # try:
    #     submit_application = driver.find_element(By.CSS_SELECTOR, "footer button")
    #     print("submit button found")
    #     print("single page apply")

    #     mobile_input = driver.find_element(
    #         By.CLASS_NAME,
    #         "artdeco-text-input--input",
    #     )
    #     mobile_input.clear()
    #     mobile_input.send_keys("012345678911")

    #     submit_application.click()
    #     time.sleep(2)
    # except NoSuchElementException:
    #     close()
