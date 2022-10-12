from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support import expected_conditions as EC
import sys

class wait_for_text_to_equal(object):
    def __init__(self, locator, text_):
        self.locator = locator
        self.text = text_

    def __call__(self, driver):
        try:
            element_text = driver.find_element(*self.locator).text
            return element_text == self.text
        except StaleElementReferenceException:
            return False

list = []
with open("links_file.txt", "r") as f:
  for line in f:
    list.append(line.strip())

if len(list) == 0 or list[0] == "":
    print("\"links_file.txt\" is empty! Run again the program when you fill the file.")
    sys.exit(1)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://web.telegram.org/z/")
print("Log in to Telegram via QR code and immediately go to the Deezer Music Bot chat!")
try:
    WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#MiddleColumn > div.messages-layout > div.MiddleHeader > div.Transition.slide-fade > div > div > div > div.info > div")))
except:
    print("Waiting too long. Logout from Telegram and run the program again!")
    sys.exit(1)

print("Great! Now wait and make sure multiple downloading is enabled on your browser.")
message = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "message-input-text")))
action = ActionChains(driver).move_to_element(message).send_keys(list[0]).perform()
WebDriverWait(driver, 5).until(wait_for_text_to_equal((By.ID, "message-input-text"), list[0]))
action = ActionChains(driver).send_keys(Keys.RETURN).perform()
x = 0
y = 15
while y <= len(list):
    divs = driver.find_elements(By.CSS_SELECTOR, "div[class='Message message-list-item first-in-group last-in-group own open shown']")
    div = divs[len(divs) - 1]
    id = div.get_attribute('id')
    id_number = int(id[7:len(id)])
    id_number = id_number + 3
    id = "message" + str(id_number)
    for iterator in range(x, y):
        try:
            if(iterator >= len(list)):
                break
            link = list[iterator]
            action = ActionChains(driver).move_to_element(message).send_keys(link).perform()
            WebDriverWait(driver, 5).until(wait_for_text_to_equal((By.ID, "message-input-text"), link))
            action = ActionChains(driver).send_keys(Keys.RETURN).perform()
            time.sleep(2.8)
        except:
            print("Exception at typing links!")
            continue
    while True:
        try:
            WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, id)))
        except:
            print("If this line is repeating more than few times one after the other with no other lines in between, stop the program! " + id)
            break
        try:
            download = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                      "#" + id + " > div.message-content-wrapper > div > div.content-inner > div > button.Button.download-button.tiny.primary.round")))
            ActionChains(driver).move_to_element(download).perform()
            time.sleep(0.6)
            download.click()
            id_number = id_number + 1
            id = "message" + str(id_number)
        except:
            id_number = id_number + 1
            id = "message" + str(id_number)
            print("Finding new message: " + id)
            continue
    x = x + 15
    y = y + 15

if x < len(list):
    y = len(list)
    divs = driver.find_elements(By.CSS_SELECTOR, "div[class='Message message-list-item first-in-group last-in-group own open shown']")
    div = divs[len(divs) - 1]
    id = div.get_attribute('id')
    id_number = int(id[7:len(id)])
    id_number = id_number + 3
    id = "message" + str(id_number)
    for iterator in range(x, y):
        try:
            if iterator >= len(list):
                break
            link = list[iterator]
            action = ActionChains(driver).move_to_element(message).send_keys(link).perform()
            WebDriverWait(driver, 5).until(wait_for_text_to_equal((By.ID, "message-input-text"), link))
            action = ActionChains(driver).send_keys(Keys.RETURN).perform()
            time.sleep(2.8)
        except:
            print("Exception at typing links!")
            continue
    while True:
        try:
            WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, id)))
        except:
            print("If this line is repeating one after the other with no other lines in between, stop the program! " + id)
            break
        try:
            download = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                      "#" + id + " > div.message-content-wrapper > div > div.content-inner > div > button.Button.download-button.tiny.primary.round")))
            ActionChains(driver).move_to_element(download).perform()
            time.sleep(1)
            download.click()
            id_number = id_number + 1
            id = "message" + str(id_number)
        except:
            id_number = id_number + 1
            id = "message" + str(id_number)
            print("Finding new message: " + id)
            continue

print("Number of songs downloaded: " + str(len(list)))
print("You should log out from telegram.")
try:
    WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.ID, "auth-qr-form")))
    print("Successfully logged out.")
except:
    print("Waiting too long. Logout from Telegram additionally from your mobile phone.")
driver.quit()
print("Bye!")