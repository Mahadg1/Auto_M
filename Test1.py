import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service= Service(r"C:/Users/dgmah/Documents/SeleniumTests/chromedriver.exe"), options=options)
#driver = webdriver.Chrome()
driver.get("https://www.makemytrip.com/")
driver.maximize_window()
driver.implicitly_wait(10)
#LandingPage = driver.find_element(By.XPATH, '//*[@class = "bgGradient webpSupport landingPageBg"]')
LandingPage = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@class = "bgGradient webpSupport landingPageBg"]')))
    
    

def selectTripType(trip):
    tripele = driver.find_elements(By.XPATH, '//*[@class= "fswTabs latoRegular darkGreyText "]/li')
    
    for i in range(len(tripele)):
        if tripele[i].text == trip:
            tripele[i].click()
            break

def selectFrom(city):
    fromele = driver.find_element(By.XPATH, '//*[@id="fromCity"]')
    fromele.send_keys(city)
    fromlist = driver.find_elements(By.XPATH, '//*[@class="react-autosuggest__suggestions-list"]/li')
    for i in range(len(fromlist)):
        if fromlist[i].text == city:
            fromlist[i].click()
            print(fromlist[i].text)
            break

def selectToCity(city):
    toele = driver.find_element(By.XPATH, '//*[@id="toCity"]')
    toele.send_keys(city)
    tolist = driver.find_elements(By.XPATH, '//*[@class="react-autosuggest__suggestions-list"]/li')
    for i in range(len(tolist)):
        if tolist[i].text == city:
            tolist[i].click()
            print(tolist[i].text)
            break
    

selectTripType("Round Trip")
selectFrom("Mumbai")
selectToCity("Goa")

driver.close()
driver.quit()
