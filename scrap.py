import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

import os

os.system('cls')

comment_dt=[]

driver = webdriver.Chrome(executable_path=r'C:\Users\Tolu\AppData\Local\Temp\Rar$EXa0.821\chromedriver.exe')
   
driver.get("https://www.filimo.com/m/hgavb")

time.sleep(3)

first_elements = driver.find_elements(By.CLASS_NAME, 'comment-content')

for e in first_elements:
    comment = e.text
    comment_dt.append(comment)

  
df = pd.DataFrame()
df['comment_text'] = comment_dt
df['film_name'] =driver.find_elements(By.CLASS_NAME, 'en-title')

df.to_csv('./data/The_Late_Father.csv')  

