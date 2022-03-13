from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = "https://www.amazon.com/"

driver.get(url)
driver.implicitly_wait(5)

search_element = driver.find_element(by=By.CSS_SELECTOR, value="input[aria-label='Search']")
search_element.click()

search_element.send_keys('Kindle')
search_submit_button_element = driver.find_element(by=By.ID, value='nav-search-submit-button')
search_submit_button_element.click()

all_new_kindle_paperwhile_element = driver.find_element(by=By.XPATH, value="//*[contains(text(), 'All-new Kindle Paperwhite')]")
all_new_kindle_paperwhile_element.click()

add_to_cart_element = driver.find_element(by=By.ID, value='add-to-cart-button')
add_to_cart_element.click()

no_thanks_button_element=driver.find_element(by=By.CSS_SELECTOR, value="span[class*='abb-intl-decline']")
no_thanks_button_element.click()

go_to_card_button_element = driver.find_element(by=By.XPATH, value="//*[contains(text(), 'Go to Cart')]")
go_to_card_button_element.click()

all_new_kindle_pw_in_cart_element = driver.find_element(by=By.XPATH, value="//*[contains(text(), 'All-new Kindle Paperwhite')]")

assert all_new_kindle_pw_in_cart_element
