from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

PROMISED_DOWN = 100
PROMISED_UP = 100
CHROME_DRIVER_PATH = r"<chromedriver.exe directory>"
TWITTER_EMAIL = "registered_email_id"
TWITTER_PASSWORD = "registered_password"

class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(service = Service(CHROME_DRIVER_PATH))
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        t = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        t.click()
        time.sleep(40)
        self.down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        return f"{self.up},{self.down}"

    def tweet_at_provider(self,a,b):
        self.driver.get("https://twitter.com")
        message = f"@airtelindia, I am getting Upload Speed of {a} and Download Speed of {b}. Promised speeds were around 100 Mbpsl Why am I getting low speed internet?"
        time.sleep(2)
        login_using_google = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div')
        login_using_google.click()
        time.sleep(2)
        mail = self.driver.find_element(By.CSS_SELECTOR, 'input[type="text"]')
        mail.send_keys(TWITTER_EMAIL)
        mail.send_keys(Keys.ENTER)
        # time.sleep(2)             #IF IT ASKS FOR USERNAME
        # nib = self.driver.find_element(By.NAME, 'text')
        # nib.send_keys("username")
        # nib.send_keys(Keys.ENTER)
        time.sleep(2)
        pwd = self.driver.find_element(By.NAME, 'password')
        pwd.send_keys(TWITTER_PASSWORD)
        pwd.send_keys(Keys.ENTER)
        time.sleep(6)
        entry = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')
        entry.click()
        time.sleep(2)
        #x = self.driver.find_element(By.CSS_SELECTOR, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[3]/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[1]')
        element = WebDriverWait(self.driver, 3).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'public-DraftEditorPlaceholder-root')))
        ActionChains(self.driver).move_to_element(element).send_keys(message).perform()
        time.sleep(2)
        tweet = self.driver.find_element(By.CSS_SELECTOR, 'div[data-testid="tweetButton"]')
        tweet.click()


bot = InternetSpeedTwitterBot()
SPEED = bot.get_internet_speed().split(',')
UP = float(SPEED[0])
DOWN = float(SPEED[1])
if (UP < PROMISED_UP) or (DOWN < PROMISED_DOWN):
    bot.tweet_at_provider(UP, DOWN)
else:
    print("It\'s OK baby. No need to tweet.")       # JUST FOR FUN 😁