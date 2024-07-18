from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', value=True)

driver = webdriver.Chrome(chrome_options)
driver.get('https://orteil.dashnet.org/cookieclicker/')

wait = WebDriverWait(driver, 10)
consent = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'fc-button-label')))
consent.click()
engilsh_btn = wait.until(EC.element_to_be_clickable((By.ID, 'langSelect-EN')))
engilsh_btn.click()
cookie = driver.find_element(By.ID, 'bigCookie')

timeout = time.time() + 5
five_min = time.time() + 60*5  # 5 minutes


while True:
    cookie.click()

    if time.time() > timeout:
        items = driver.find_elements(By.CSS_SELECTOR, '.product.unlocked.enabled')
        item_ids = [item.get_attribute("id") for item in items]
        for cur_id in item_ids:
            item = driver.find_element(By.ID, cur_id)
            item.click()
        timeout = time.time() + 5

    if time.time() > five_min:
        break

