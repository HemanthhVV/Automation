from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from config import CHROME_FILE_PATH #STEP1
import time

#STEPS:
#1.CREATE AN PATH OF FOLDER WHERE THIS MESSAGES ARE GONNA STORE AND NO NEED TO RELOAD OF THE WHATSAPP
#2.YOU NEED TO INSTALL CHROME DRIVER FROM CHROMIUM PAGE FOR YOUR RESPECTED CHROME VERSION (WHICH CAN BE SEEN IN SETTINGS)
#3.GIVE THE PATH OF THE CHROMEDRIVER IN EXE PATH 
#YOU CAN ALSO DOWNLOAD VARIOUS DRIVERS INCASE IF YOU ARE USING OTHER BROWSERS THAN CHROME

contact=input("Enter the contact Name: ")
text=input("Enter the text you want: ")
service=Service(executable_path="C:\\Users\\{user_name}\\chromedriver\\chromedriver") #STEP2 AND STEP3 #NO NEED OF CURLY BRACE
options=webdriver.ChromeOptions()
options.add_argument(CHROME_FILE_PATH)
driver = webdriver.Chrome(service=service,options=options)
driver.maximize_window()
driver.get('https://web.whatsapp.com/')
time.sleep(14)
input_Xpath="//p[@class='selectable-text copyable-text iq0m558w']"
input_box_search = driver.find_element(By.XPATH,input_Xpath)
input_box_search.click()
time.sleep(2)
input_box_search.send_keys(contact)
time.sleep(2)
selected_contact = driver.find_element(By.XPATH,"//span[@title= \""+ contact +"\"]")
selected_contact.click()
time.sleep(2)
inp_xpath = "//div[@title='Type a message']"
input_box = driver.find_element(By.XPATH,inp_xpath)
input_box.click()
time.sleep(2)
input_box.send_keys(text + Keys.ENTER)
time.sleep(5)
driver.quit()