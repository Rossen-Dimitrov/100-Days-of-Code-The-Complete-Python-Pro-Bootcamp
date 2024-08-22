from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)
driver.get('https://www.python.org/')

upcoming = driver.find_elements(By.CSS_SELECTOR, value=".event-widget .shrubbery .menu li")

events_dict = {}
count = 0
for el in upcoming:
    time_tag = el.find_element(By.TAG_NAME, "time")
    a_tag = el.find_element(By.TAG_NAME, "a")

    events_dict[count] = {
        'time': time_tag.text,
        'name': a_tag.text
    }

    count += 1

# driver.close()  # closes only current tab
driver.quit()  # close entire browser
print(events_dict)


# price = driver.find_element(By.CLASS_NAME, value="some-class-name")
# print(price.text)
# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.get_attribute("placeholder"))
# button = driver.find_element(By.ID, value="submit")
# by_css = driver.find_element(By.CSS_SELECTOR, value='.class p')
# by_xpath = driver.find_element(By.XPATH, value='//*[@id="tabs--1-content-1"]/div/div/div/div/div[1]/div[4]/div[1]')
# driver.close()
driver.quit()