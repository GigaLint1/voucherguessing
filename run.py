from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome("C:/Users/grego/Desktop/MyProjects/shoppee/chromedriver.exe", chrome_options=chrome_options)

codeinput = driver.find_element_by_xpath('//*[@id="modal"]/div/div/div[2]/div/div/div[2]/div/div[1]/div/div/div/input')

for i in range(10): 
    codeinput.send_keys(str(i))
    for j in range(10):  
        codeinput.send_keys(str(j))
        for k in range(10):
            codeinput.send_keys(str(k))            
            for l in range(10):
                codeinput.send_keys(str(l))
                driver.find_element_by_xpath('//*[@id="modal"]/div/div/div[2]/div/div/div[2]/div/div[1]/button').click()
                codeinput.send_keys(Keys.BACKSPACE)
            codeinput.send_keys(Keys.BACKSPACE)
        codeinput.send_keys(Keys.BACKSPACE)  
    codeinput.send_keys(Keys.BACKSPACE) 

    
    
