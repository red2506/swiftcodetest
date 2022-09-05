import os
from tkinter.tix import Select
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

# Adding the chrome driver to environment path
driver = webdriver.Chrome("C:/Users/manir/Downloads/chrome/chromedriver.exe")
driver.get("http://localhost:9000/login")
driver.maximize_window()

# To wait for the page to load all the elements
driver.implicitly_wait(20)

######### Login snippet ###########
driver.find_element("name", "email").send_keys("ayush.gautam@betsol.com")
driver.find_element("name", "password").send_keys("1234")
driver.find_element("xpath", "/html/body/div[1]/div/div/div/div/div/form/button").click()

# Expanding the sidebar
driver.find_element("xpath", "//*[@id='nav-mobile']/li[1]/a/i").click()
driver.implicitly_wait(20)
driver.find_element("xpath", "//*[@id='slide-out']/li[6]/a").click()
# Clicking on the user profile to fill information
driver.find_element("xpath", "//*[@id='my_profile']/div/form/div/a/i").click()

######### Personal Info ###########
# Name data
driver.find_element("xpath", "//*[@id='first_name']").clear()
driver.find_element("xpath", "//*[@id='first_name']").send_keys("Ayush")
driver.find_element("xpath", "//*[@id='middle_name']").clear()
driver.find_element("xpath", "//*[@id='middle_name']").send_keys("Middle")
driver.find_element("xpath", "//*[@id='last_name']").clear()
driver.find_element("xpath", "//*[@id='last_name']").send_keys("Gautam")

# Date of birth
driver.find_element("xpath", "//*[@id='date_of_birth']").click()

driver.implicitly_wait(10)

# Year
driver.find_element("xpath", "//*[starts-with(@id, 'pika-title-')]/div/div[2]").click()
driver.find_element("xpath", "//*[starts-with(@id, 'select-options-')]/span[text()='2006']").click()

# Month
driver.find_element("xpath", "//*[starts-with(@id, 'pika-title')]/div/div[1]/input").click()
driver.find_element("xpath", "//*[starts-with(@id, 'select-options-')]/span[text()='February']").click()

# Day
driver.find_element("xpath", "//*[starts-with(@aria-labelledby, 'pika-title-')]/tbody/tr/td/button[.='10']").click()

# Submitting the date of birth
driver.find_element("xpath", "//*[starts-with(@id, 'modal-')]/div/div[2]/div[2]/div/button[2]").click()

# Gender
driver.find_element("xpath", "//*[@id='candidate_info']/ul/li[1]/div[2]/div/div[1]/div[3]/div/div/div/input").click()
driver.find_element("xpath", "//*[starts-with(@id, 'select-options-')]/span[(contains(., 'Male'))]").click()

# Continue
driver.find_element("xpath", "//*[@id='candidate_info']/ul/li[1]/div[2]/div/div[2]/div/button").click()

######### Contact Info ###########
time.sleep(5)
# Contact details
driver.find_element("xpath", "//*[@id='mobile_number']").clear()
driver.find_element("xpath", "//*[@id='mobile_number']").send_keys("9878201084")
driver.find_element("xpath", "//*[@id='contact_number']").clear()
driver.find_element("xpath", "//*[@id='contact_number']").send_keys("9878201084")

# Address
driver.find_element("xpath", "//*[@id='address']").clear()
driver.find_element("xpath", "//*[@id='address']").send_keys("G1 Balaji Nivas, 1st Cross Road Pratibha Industrial area, Yellechenahalli Bangalore, 560078")

# Continue
driver.find_element("xpath", "//*[@id='candidate_info']/ul/li[2]/div[2]/div/div[3]/div/button[2]").click()

######### Class 10 ###########
# Percentage
driver.find_element("xpath", "//*[@id='class_x']").clear()
driver.find_element("xpath", "//*[@id='class_x']").send_keys("74")
driver.find_element("xpath", "//*[@id='class_x_year']").clear()
driver.find_element("xpath", "//*[@id='class_x_year']").send_keys("2015")

# Continue
driver.find_element("xpath", "//*[@id='candidate_info']/ul/li[3]/div[2]/div/div[3]/div/button[2]").click()

######### Class 12 ###########
# Percentage
driver.find_element("xpath", "//*[@id='class_xii']").clear()
driver.find_element("xpath", "//*[@id='class_xii']").send_keys("57")
driver.find_element("xpath", "//*[@id='class_xii_year']").clear()
driver.find_element("xpath", "//*[@id='class_xii_year']").send_keys("2018")

# Continue
driver.find_element("xpath", "//*[@id='candidate_info']/ul/li[4]/div[2]/div/div[4]/div/button[2]").click()

######### Undergrade ###########
# College name
driver.find_element("xpath","//*[@id='candidate_info']/ul/li[5]/div[2]/div/div[1]/div[1]/div/input").click()
driver.find_element("xpath", "//li[starts-with(@id, 'select-options-')]/span[(contains(., 'A.G.M. Rural Engineering College, Hubli'))]").click()

# Stream
driver.find_element("xpath", "//*[@id='candidate_info']/ul/li[5]/div[2]/div/div[2]/div[1]/div/input").click()
driver.find_element("xpath", "//li[starts-with(@id, 'select-options-')]/span[(contains(., 'Information Science & Engineering'))]").click()

# Scores
driver.find_element("xpath", "//*[@id='be_avg']").clear()
driver.find_element("xpath", "//*[@id='be_avg']").send_keys("70")
driver.find_element("xpath", "//*[@id='sem_1']").clear()
driver.find_element("xpath", "//*[@id='sem_1']").send_keys("70")
driver.find_element("xpath", "//*[@id='sem_2']").clear()
driver.find_element("xpath", "//*[@id='sem_2']").send_keys("70")
driver.find_element("xpath", "//*[@id='sem_3']").clear()
driver.find_element("xpath", "//*[@id='sem_3']").send_keys("70")
driver.find_element("xpath", "//*[@id='sem_4']").clear()
driver.find_element("xpath", "//*[@id='sem_4']").send_keys("70")
driver.find_element("xpath", "//*[@id='sem_5']").clear()
driver.find_element("xpath", "//*[@id='sem_5']").send_keys("70")
driver.find_element("xpath", "//*[@id='sem_6']").clear()
driver.find_element("xpath", "//*[@id='sem_6']").send_keys("70")
driver.find_element("xpath", "//*[@id='sem_7']").clear()
driver.find_element("xpath", "//*[@id='sem_7']").send_keys("70")
driver.find_element("xpath", "//*[@id='sem_8']").clear()
driver.find_element("xpath", "//*[@id='sem_8']").send_keys("70")

# Continue
driver.find_element("xpath", "//*[@id='candidate_info']/ul/li[5]/div[2]/div/div[4]/div/button[2]").click()

######### Job Priority ###########

# Job Priority 1
driver.find_element("xpath","//*[@id='candidate_info']/ul/li[6]/div[2]/div/div[2]/div[1]/div[1]/div/input").click()
driver.find_element("xpath", "(//*[starts-with(@id, 'select-options-')]/span[(contains(., 'Networking'))])[1]").click()

# Job Priority 2
driver.find_element("xpath","//*[@id='candidate_info']/ul/li[6]/div[2]/div/div[2]/div[1]/div[2]/div/input").click()
driver.find_element("xpath", "(//*[starts-with(@id, 'select-options-')]/span[(contains(., 'Development'))])[2]").click()

# Job Priority 3
driver.find_element("xpath","//*[@id='candidate_info']/ul/li[6]/div[2]/div/div[2]/div[2]/div[1]/div/input").click()
driver.find_element("xpath", "(//*[starts-with(@id, 'select-options-')]/span[(contains(., 'Database'))])[3]").click()

# # Job Priority 4
driver.find_element("xpath","//*[@id='candidate_info']/ul/li[6]/div[2]/div/div[2]/div[2]/div[2]/div/input").click()
driver.find_element("xpath", "(//*[starts-with(@id, 'select-options-')]/span[(contains(., 'Security'))])[4]").click()

# # Continue
driver.find_element("xpath", "//*[@id='candidate_info']/ul/li[6]/div[2]/div/div[3]/div/button[2]").click()

######### Uploading Profile pic and Resume ###########
# Profile Pic
driver.implicitly_wait(10)
driver.find_element("xpath", "//*[@id='candidate_info']/ul/li[7]/div[2]/div/div[1]/div[1]/a").click()
driver.find_element("xpath", "//*[@id='profilePicture']").send_keys("C:/Users/Naveen/Downloads/images.jpg")
driver.find_element("xpath", "//*[@id='profile_photo_close']").click()

# Resume
driver.implicitly_wait(10)
driver.find_element("xpath", "//*[@id='candidate_info']/ul/li[7]/div[2]/div/div[1]/div[2]/div/a").click()
driver.find_element("xpath", "//*[@id='resume']").send_keys("C:/Users/Naveen/Downloads/document.pdf")
driver.find_element("xpath", "//*[@id='upload-picture']").click()

# Submit
time.sleep(8)
driver.find_element("xpath", "//*[@id='submit_info']").click()

# Logout
time.sleep(8)
driver.find_element("xpath", "//*[@id='nav-mobile']/li[2]/a").click()

driver.quit()