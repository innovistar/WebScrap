import requests
import re
import os
import subprocess
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


page = requests.get("https://odibets.com/league?active=upcoming")
def page_content():
       text = page.content
       txt = str(text)
       return txt

def create_file():
       output = page_content()
       with open("page source.txt", "w") as f:
              f.write(output)

def span():
    with open('page source.txt') as file:
        for line in file:
            words = line.split()
            for word in words:
                if word.startswith("<span"):
                    print(word)

def save_output():
       subprocess.call([r'C:\Users\Inno\Desktop\New folder\trial.bat'])

       


def index():
       lookup = '<span>1.65</span>'
       with open('out_file.txt') as myFile:
              for num, line in enumerate(myFile, 1):
                     if lookup in line:
                            print('found at line', num)
                            return int(num)
def odd_range():
       create_file()
       span()
       save_output()
       number = index()
       if number == 10:
              x = "/html/body/div/div[7]/div[2]/div/div[1]/div[2]/div/button[1]/span[2]"
              return(x)         
       elif number == 14:
              x = "/html/body/div/div[7]/div[2]/div/div[1]/div[2]/div/button[3]/span[2]"
              return(x)
       elif number == 19:
              x = "/html/body/div/div[7]/div[2]/div/div[2]/div[2]/div/button[1]/span[2]"
              return(x)
       elif number == 23:
              x = "/html/body/div/div[7]/div[2]/div/div[2]/div[2]/div/button[3]/span[2]"
              return(x) 
       elif number == 28:
              x = "/html/body/div/div[7]/div[2]/div/div[3]/div[2]/div/button[1]/span[2]"
              return(x)
       elif number == 32:
              x = "/html/body/div/div[7]/div[2]/div/div[3]/div[2]/div/button[3]/span[2]"
              return(x)
       elif number == 37:
              x = "/html/body/div/div[7]/div[2]/div/div[4]/div[2]/div/button[1]/span[2]"
              return(x)
       elif number == 41:
              x = "/html/body/div/div[7]/div[2]/div/div[4]/div[2]/div/button[3]/span[2]"
              return(x)
       elif number == 46:
              x = "/html/body/div/div[7]/div[2]/div/div[5]/div[2]/div/button[1]/span[2]"
              return(x)
       elif number == 50:
              x = "/html/body/div/div[7]/div[2]/div/div[5]/div[2]/div/button[3]/span[2]"
              return(x)
       elif number == 55:
              x = "/html/body/div/div[7]/div[2]/div/div[6]/div[2]/div/button[1]/span[2]"
              return(x)
       elif number == 59:
              x = "/html/body/div/div[7]/div[2]/div/div[6]/div[2]/div/button[3]/span[2]"
              return(x)
       elif number == 64:
              x = "/html/body/div/div[7]/div[2]/div/div[7]/div[2]/div/button[1]/span[2]"
              return(x)
       elif number == 68:
              x = "/html/body/div/div[7]/div[2]/div/div[7]/div[2]/div/button[3]/span[2]"
              return(x)
       elif number == 73:
              x = "/html/body/div/div[7]/div[2]/div/div[8]/div[2]/div/button[1]/span[2]"
              return(x)
       elif number == 77:
              x = "/html/body/div/div[7]/div[2]/div/div[8]/div[2]/div/button[3]/span[2]"
              return(x)


driver = webdriver.Chrome()
try:
   driver.get("https://odibets.com/login")
   print ("Cheking the site...................")
except:
   print ("There is a problem with your internet connention. Try again later")

def username():
   
   element = driver.find_element_by_css_selector("#cont > div.l-form > div > form > div:nth-child(3) > div > input[type=tel]")
   element.send_keys("User name")

def passwd():
    element = driver.find_element_by_css_selector("#cont > div.l-form > div > form > div:nth-child(4) > div.input > input[type=password]")
    element.send_keys("Password")

def login():
   element = driver.find_element_by_xpath("/html/body/div/div[6]/div/form/div[4]/button")
   element.click()


def league():
   username()
   passwd()
   login()
   odd_range()
   element = driver.find_element_by_xpath('//*[@id="cont"]/div[5]/ul[1]/li[4]/a/span[1]/img')
   print (element)
   element.click()
   element1 = driver.find_element_by_xpath('/html/body/div/div[5]/div/a[2]/div')
   element1.click()
   element2 = driver.find_element_by_xpath(x)
   element2.click()
   stake = driver.find_element_by_css_selector('input.stake')
   stake.send_keys('1')
   element3 = driver.find_element_by_xpath('/html/body/div/div[8]/div[3]/div[2]/form/div/button')
   element3.click()
   place = driver.find_element_by_xpath('/html/body/div/div[8]/div[4]/form[1]/button')
   place.click()




league()
   

                            
                     
                     
                     

              
