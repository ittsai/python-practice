# do automative task
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#keep chrome browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options= chrome_options)

driver.get("https://secure-retreat-92358.herokuapp.com/")
first_name = driver.find_element(By.NAME, value="fName")
last_name = driver.find_element(By.NAME, value="lName")
email = driver.find_element(By.NAME, value="email")
button = driver.find_element(By.CSS_SELECTOR, value="button")
first_name.send_keys("Test First")
last_name.send_keys("Test Last")
email.send_keys("test@test.com")
button.send_keys(Keys.ENTER)

# test = driver.find_element(By.XPATH, value='//*[@id="addShortcut"]/div[2]/span')
# driver.close()
# driver.quit()