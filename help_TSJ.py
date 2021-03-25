# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 18:35:32 2021

@author: chchien
"""

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://tsj.tw")

print ("webpage is loaded sucessfullly!\n")

WebDriverWait(driver,20,0.1).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[2]/div[3]/div[1]/button[1]")))

print ("button is loaded sucessfullly!\n")

button = driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[1]/button[1]")

driver.execute_script("window.scrollTo(0, 880)") 

click_num = input ("你想幫TSJ吹幾次呢?\n")

for i in range (int(click_num)):
    button.click()

while (1):
    click_num = input ("你還想幫TSJ吹幾次呢? (輸入0以終止吹吹)\n")
    if (int(click_num) == 0):
        Y_N = input ("真的不吹了嗎? Y/N\n")
        if (Y_N == "Y"):
            break
        elif (Y_N == "N"):
            continue
    for i in range (int(click_num)):
        button.click()

input ("Press any key to close the browser...")
driver.quit()
