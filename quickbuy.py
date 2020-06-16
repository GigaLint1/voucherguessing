from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome("C:/Users/grego/Desktop/MyProjects/codeguess/chromedriver.exe", chrome_options=chrome_options)

codeinput = driver.find_element_by_xpath('//*[@id="modal"]/div/div/div[2]/div/div/div[2]/div/div[1]/div/div/div/input')
codeinput.send_keys('IPRICEGSSNEW')
driver.find_element_by_xpath('//*[@id="modal"]/div/div/div[2]/div/div/div[2]/div/div[1]/button').click()
driver.find_element_by_class_name("rzRywA").click()
driver.find_element_by_xpath('//*[@id="modal"]/div/div/div[2]/div/div/div[3]/button[2]').click()
driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[2]/div[3]/div[2]/div[7]/div[5]/button').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[3]/div[4]/div[2]/div[16]/button').click()