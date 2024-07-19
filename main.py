from selenium import webdriver
from selenium.webdriver.common.by import By
import time

cService = webdriver.ChromeService(executable_path="/Users/puneethkumarg/Downloads/chromedriver-mac-arm64/chromedriver")

driver  = webdriver.Chrome(service=cService)

driver.get("https://licindia.in/#maincontent")


#driver.find_element(by=By.XPATH,value='//*[@id="pills-tab"]/li[2]/button').click()



time.sleep(5)






