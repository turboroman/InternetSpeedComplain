from time import sleep

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

SPEEDTEST_URL = 'https://www.speedtest.net/'
TWEETER_URL = 'https://twitter.com/'


class InternetSpeedTwitterBot:
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(options=self.options)

    def get_internet_speed(self):
        self.driver.get(SPEEDTEST_URL)
        sleep(2)
        accept_btn = self.driver.find_element(By.XPATH, '/html/body/div[5]/div[2]/div/div/div[2]/div/div/button[2]')
        accept_btn.click()
        sleep(2)

        go_btn = self.driver.find_element(By.CLASS_NAME, 'js-start-test')
        go_btn.click()
        sleep(50)

        down_speed = float(self.driver.find_element(By.CLASS_NAME, 'download-speed').text)
        up_speed = float(self.driver.find_element(By.CLASS_NAME, 'upload-speed').text)
        return {'down': down_speed, 'up': up_speed}

    def login_twitter(self, tw_email, tw_password, tw_username):
        self.driver.get(TWEETER_URL)
        sleep(10)

        login_btn = self.driver.find_element(By.XPATH,
                                             '/html/body/div[1]/div/div/div[1]/div/div[1]/div/div/div/div[2]/div[2]/div/div/div[1]/a')
        login_btn.click()
        sleep(2)

        email = self.driver.find_element(By.XPATH,
                                         '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        email.send_keys(tw_email)
        email.send_keys(Keys.ENTER)
        sleep(2)
        try:
            username = self.driver.find_element(By.NAME, 'text')
            username.send_keys(tw_username)
            username.send_keys(Keys.ENTER)
            sleep(2)
            password = self.driver.find_element(By.NAME, 'password')
            password.send_keys(tw_password)
            password.send_keys(Keys.ENTER)
        except NoSuchElementException:
            password = self.driver.find_element(By.NAME, 'password')
            password.send_keys(tw_password)
            password.send_keys(Keys.ENTER)
        sleep(10)

    def write_tweet(self, down_speed, up_speed):
        tweet_input = self.driver.find_element(By.CLASS_NAME, 'public-DraftStyleDefault-block')
        tweet_input.click()
        tweet_input.send_keys(f"internet is shit. it is not 200/20, it's just {down_speed}/{up_speed}")
        tweet_btn = self.driver.find_element(By.XPATH,
                                             '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]')
        tweet_btn.click()
