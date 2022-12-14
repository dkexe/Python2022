from selenium import webdriver
from pathlib import Path
from chromedriver_py import binary_path # this will get you the path variable
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
class start_Browser():
    path = Path(__file__).parent.absolute()
    chrome_path = str(path)+"/chromedriver"
    firefox_path = str(path) +"/geckodriver"

    URL ="https://www.google.com"

    def start_FireFox(URL):
        driver = webdriver.Firefox()

        try:
            driver.get(URL)
            time.sleep(2)
            element_input = driver.find_element(By.XPATH,"//input[@class='gLFyf']")
            element_input.send_keys("appium")
            element_input.send_keys(Keys.ENTER)
            
            
            time.sleep(5)

            get_searchlist = driver.find_elements(By.XPATH, "//div[@class='yuRUbf']/a")

            for i in get_searchlist:
                print(i.get_attribute('href') ) 

            # get_searchlist[0].click()
            get_searchlist[0].send_keys(Keys.ENTER)
            time.sleep(5)
            print(driver.title)
            # assert "appium" in driver.title.lower()
            output = driver.title.lower()
            driver.quit()
            return output
        except :
            print("Error")
            driver.quit()

        

    def end_browser(driver):
        driver.quit()

    def start_Chrome(URL,email):
        try:
            driver = webdriver.Chrome(start_Browser.chrome_path)
            
            driver.get(URL)
            time.sleep(5)
            

            element_email = driver.find_element(By.XPATH,"//input[@id='mauticform_input_generalsubscribersformhomepage_email1']")

            element_email.send_keys(email)
            time.sleep(2)
            element_email.send_keys(Keys.ENTER)
            time.sleep(5)
            element_message = driver.find_element(By.XPATH,"//div[@id='mauticform_generalsubscribersformhomepage_message']")
            print(element_message.text)
            
            output =element_message.text


            driver.quit()
            return output
        except:
            print("Error")
            driver.quit()
