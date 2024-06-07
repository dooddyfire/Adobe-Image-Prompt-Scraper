from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
import time
import requests 
from seleniumbase import Driver
import pandas as pd 

#url = input("Enter midjourney showcase url : ")

#filename = input("Enter your filename : ")

url = "https://stock.adobe.com/ca/search?creator_id=210487359&filters%5Bcontent_type%3Aphoto%5D=1&filters%5Bcontent_type%3Aillustration%5D=1&filters%5Bcontent_type%3Azip_vector%5D=1&filters%5Bcontent_type%3Avideo%5D=1&filters%5Bcontent_type%3Atemplate%5D=1&filters%5Bcontent_type%3A3d%5D=1&filters%5Bcontent_type%3Aaudio%5D=0&filters%5Binclude_stock_enterprise%5D=0&filters%5Bis_editorial%5D=0&filters%5Bfetch_excluded_assets%5D=1&filters%5Bcontent_type%3Aimage%5D=1&order=relevance&safe_search=1&limit=100&search_page=1&search_type=pagination&load_type=page&get_facets=0"
#url = input("Enter midjourney showcase url : ")

filename = "adobe"
totalx = int(input("กรุณาใส่จำนวนรูปที่จะดึง : (max : 999) : "))
#filename = input("Enter your filename : ")


driver = Driver(uc=True)

driver.get(url)



input("Please Login and Press Enter : ")
#time.sleep(3)

# fix 17/5/2567

# .find_element(By.CSS_SELECTOR,'a.bg-cover').get_attribute('href')

lis = [ i.get_attribute('href') for i in driver.find_elements(By.CSS_SELECTOR,'a.js-search-result-thumbnail')]
for k in lis: 
    print(k)
print("Total : ",len(lis))
print("จำนวนรูปที่จะดึง : ",totalx)

link_lis = []
img_lis = []
desc_lis = []
image_address_lis = []
title_lis = []
kw_lis = []
c = 1 



for item in lis[:totalx]:

    print(f"=============== Item No : {c} =================")
    print(item)

    link_lis.append(item)

    driver.get(item)
    time.sleep(3)

    img = driver.find_element(By.CSS_SELECTOR, "img.js-search-result-thumbnail").get_attribute('src')
    img_lis.append(img)
    print(img)

    title = driver.find_element(By.CSS_SELECTOR,'h1.js-details-title').text 
    title_lis.append(title)
    print(title)

    try:
        image_address = item.split("/")[-1]
        image_address_lis.append(image_address)
        print(image_address)
    except: 
        print("ไม่มี")
        image_address_lis.append("ไม่มี")

    
    try:
        kw = " ".join([ c.text for c in driver.find_elements(By.CSS_SELECTOR,'span.js-keywords-item')])
        print(kw)
        kw_lis.append(kw)
    except:
        print("ไม่มี")
        kw_lis.append("ไม่มี")

    c = c + 1


df = pd.DataFrame()
df['Title'] = title_lis 
df['Link'] = link_lis 
df['Keyword'] = kw_lis 
df['Image'] = img_lis 
df['Image Address'] = image_address_lis 

df.to_excel(f"{filename}.xlsx")
print("All Done Enjoy!!!!")