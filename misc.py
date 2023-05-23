from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=Service(r"C:/Users/dgmah/Documents/SeleniumTests/chromedriver.exe"))
driver.get("https://www.lambdatest.com/selenium-playground/window-popup-modal-demo")
driver.maximize_window() 
doublewin =WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "followboth")))

doublewin.click()
parentguid = driver.current_window_handle
print(driver.title)
w= driver.window_handles

for i in range(len(w)):
    if w[i] != parentguid:
     driver.switch_to.window(w[i])
     print(driver.title)
     testele = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, '//div[@data-testid= "sheetDialog"]')))
     if testele.is_displayed():
        break
     driver.close()
driver.switch_to.window(parentguid)
     #ele = driver.find_element(By.XPATH, '//*[@class= "x1lliihq x6ikm8r x10wlt62 x1n2onr6 xg8j3zb"]')
     #while ele.is_displayed():

      #assert "Connect with LambdaTest on Facebook" in ele
driver.quit()