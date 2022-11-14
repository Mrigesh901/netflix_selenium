from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


driverService = Service(executable_path="E:\setup\chromedriver.exe")
driver = webdriver.Chrome(service=driverService)

driver.get("https://www.netflix.com/in/")



genre = driver.find_element(by=By.XPATH, value='//*[@id="appMountPoint"]/div/div/div/div/div/div[3]/div[1]/div[2]/ul/li[15]/a/span')
genre.click()
movie = driver.find_element(by=By.CSS_SELECTOR, value='.nm-collections-title-img')
movie.click()
time.sleep(3)

description = driver.find_element(by=By.XPATH, value='//*[@id="section-hero"]/div/div[1]/div[2]/div[1]/div[2]/div[1]')
print("description   :    ", description.text)

starring = driver.find_element(by=By.XPATH, value='//*[@id="section-hero"]/div/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/span[2]')
print("Star Cast    :     ", starring.text)

driver.find_element(by=By.XPATH, value='//*[@id="section-additional-videos"]/div[2]/ul/li[1]/div/button/span[1]').click()
time.sleep(60)

driver.quit()

