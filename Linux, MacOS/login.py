#!/usr/bin/python3.5   

from selenium import webdriver # importing selenium package
from time import sleep
  
usr = "username/login ID"    # replace "username/login ID" with your username. example-: '123456'  
pwd = "Password"             # replace "Password" with your password. example-: 'abcdef'

#usr=input('Enter username') # asks for the username/login ID, everytime you run this script.
#pwd=input('Enter Password') # asks for the password, everytime you run this script.

driver = webdriver.Firefox() 
driver.get('https://securelogin.pu.ac.in/cgi-bin/login?cmd=login&mac=a0:af:bd:ab:52:34&ip=172.16.178.36&essid=PU%40CAMPUS&apname=UIET_BLK1_1F_L1&apgroup=PU-AP-UIET&url=http%3A%2F%2Fbit%2Edo%2FWifion') 
print ("PU login")
sleep(1) 
  
username_box = driver.find_element_by_id('user') 
username_box.send_keys(usr) 
print ("Username entered") 
sleep(1)

password_box = driver.find_element_by_id('password') 
password_box.send_keys(pwd) 
print ("Password entered") 
  
login_box = driver.find_element_by_name('Login') 
login_box.click() 
  
print ("Login Successful") 
#input('Press anything to quit') 
driver.quit() 
print("Finished")
