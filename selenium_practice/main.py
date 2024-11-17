# do automative task
from selenium import webdriver
from selenium.webdriver.common.by import By
#keep chrome browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options= chrome_options)

driver.get("https://www.google.com")
gmail = driver.find_element(By.CLASS_NAME, value="gb_W")
print(gmail.text)
# test = driver.find_element(By.XPATH, value='//*[@id="addShortcut"]/div[2]/span')
driver.close()
#driver.quit()