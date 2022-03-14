from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = "https://www.amazon.com/"

# Go to Amazon web site
driver.get(url)
driver.implicitly_wait(5)

# Go to Search input field
search_element = driver.find_element(by=By.CSS_SELECTOR, value="input[aria-label='Search']")
search_element.click()

# Search for Kindle
search_element.send_keys('Kindle')
search_submit_button_element = driver.find_element(by=By.ID, value='nav-search-submit-button')
search_submit_button_element.click()

# Look for all new kind paper white
all_new_kindle_paperwhite_element = driver.find_element(by=By.XPATH, value="//*[contains(text(), 'All-new Kindle Paperwhite')]")
all_new_kindle_paperwhite_element.click()

# Add the kindle to the cart
add_to_cart_element = driver.find_element(by=By.ID, value='add-to-cart-button')
add_to_cart_element.click()

# Dismiss the popup
no_thanks_button_element=driver.find_element(by=By.CSS_SELECTOR, value="span[class*='abb-intl-decline']")
no_thanks_button_element.click()

# Go to shopping cart
go_to_card_button_element = driver.find_element(by=By.XPATH, value="//*[contains(text(), 'Go to Cart')]")
go_to_card_button_element.click()

# Make sure the kindle is in the shopping cart
all_new_kindle_pw_in_cart_element = driver.find_element(by=By.XPATH, value="//*[contains(text(), 'All-new Kindle Paperwhite')]")

assert all_new_kindle_pw_in_cart_element
