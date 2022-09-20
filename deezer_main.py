from selenium.common import StaleElementReferenceException
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

class wait_for_value_to_start_with(object):
    def __init__(self, locator, text_):
        self.locator = locator
        self.text = text_

    def __call__(self, driver):
        try:
            element_text = driver.find_element(*self.locator).get_attribute('value')
            return element_text.startswith(self.text)
        except StaleElementReferenceException:
            return False
playlist = ""
while True:
    print("Enter the link of your playlist you want to download: ")
    playlist = str(input())
    if not playlist.startswith("https://www.deezer.com/") or "/playlist/" not in playlist:
        print("You entered the wrong link")
        continue
    else:
        break
open('links_file.txt', 'w').close()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(playlist)
listoflinks = []
print("Links to every track from playlist: ")
try:
    refuse_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "gdpr-btn-refuse-all"))
    )
    refuse_button.click()
    numberoftracks = driver.find_element(By.CSS_SELECTOR, "#page_naboo_playlist > div.catalog-content > div > div._5BJsj > div > div._2yyo6 > ul > li:nth-child(1)").text
    numberoftracks = numberoftracks[0:len(numberoftracks)-7]
    numberoftracks = int(numberoftracks)
    for x in range(1, numberoftracks + 1):
        button = driver.find_element(By.CSS_SELECTOR, "div._2OACy[aria-rowindex=\'" + str(x) +"\'] .popper-wrapper button")
        button.click()
        div = WebDriverWait(driver, 10).until(
           EC.presence_of_element_located((By.CLASS_NAME, "_2ZkBf"))
        )
        share_button = div.find_element(By.XPATH, "//*[contains(text(), 'Share')]")
        share_button.click()
        WebDriverWait(driver, 10).until(wait_for_value_to_start_with((By.CSS_SELECTOR, "#modal_sharebox > div.modal-body > div.share-content.share-infos > div.share-thumbnail-infos > div.share-action > div > div.control-input > input"), "https:"))
        input = driver.find_element(By.CSS_SELECTOR, "#modal_sharebox > div.modal-body > div.share-content.share-infos > div.share-thumbnail-infos > div.share-action > div > div.control-input > input")
        link = input.get_attribute('value')
        listoflinks.append(link)
        print(str(x) + ": " + link)
        close_button = driver.find_element(By.CLASS_NAME, "modal-close")
        close_button.click()
        driver.execute_script("document.querySelector(\"div._2OACy[aria-rowindex=\'" + str(x) +"\']\").scrollIntoView()")
except Exception as e:
    print(e)
    driver.quit()

driver.quit()

with open("links_file.txt", "w") as f:
    for element in listoflinks:
        f.write(str(element) +"\n")

print("Links to all " + str(numberoftracks) + " tracks are in the \"links_file.txt\"")