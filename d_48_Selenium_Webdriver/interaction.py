from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', value=True)

driver = webdriver.Chrome(chrome_options)
# driver.get('https://en.wikipedia.org/wiki/Main_Page')
driver.get('https://secure-retreat-92358.herokuapp.com/')

# article_count = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/a[1]')
# article_count.click()

# content_portal = driver.find_element(By.LINK_TEXT, value='Content portals')
# content_portal.click()
wait = WebDriverWait(driver, 10)
# search_bar = wait.until(EC.element_to_be_clickable((By.NAME, "search")))
# search_bar.clear()
# search_bar.send_keys("Python", Keys.ENTER)

button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button')))
first_name = driver.find_element(By.NAME, 'fName')
first_name.send_keys('Ross')
last_name = driver.find_element(By.NAME, 'lName')
last_name.send_keys('Dim')
email = driver.find_element(By.NAME, 'email')
email.send_keys('rosty_d@abv.bg')

button.click()

# driver.quit()

