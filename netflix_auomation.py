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

while True:
    try:
        spinner  = driver.find_element(by=By.CSS_SELECTOR, value=".nf-loading-spinner")

    except Exception as e:
        try:
            x = driver.find_element(by=By.ID, value='81624954')
            count =  float(x.find_elements(by=By.CSS_SELECTOR, value="*")[0].get_attribute("currentTime"))
            print(count)
            if count>0:
                print("Video Running")
                # break
            else:
                print("Not Running")
            
            time.sleep(10)
        except Exception as e:

            print("video error : ", e)

driver.quit()

