from pandas.core.algorithms import take_nd
import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

executable_path = '/CPE551/FinalProject/driver/chromedriver'
page_url = 'https://24h.pchome.com.tw/store/DGCW13?p=1'
results = []# variable to hold all reviews
driver = webdriver.Chrome(executable_path=executable_path)
limit = 1
page = driver.get(page_url)

for i in range(limit):
    
    temp = []
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    divs = soup.select('dd div.prod_info')
    # print(divs)
    
    for idx, dd in enumerate(divs):
        desc = None
        price = None   
        p_desc = dd.select('h5.nick a')
        if p_desc != []:
            desc = p_desc[0].get_text()
                
        p_price=dd.select('ul.price_box span.price')
        if p_price != []:
            price = p_price[0].get_text(strip = True)
        temp.append((desc, price))

    results += temp
    button = driver.find_element_by_css_selector('div#PaginationContainer.pagination.unblock li.sp a')
    
    if button == None :
        break 
    else :
        button.click()

results = pd.DataFrame(results, columns=['name', 'price'])

print(results)
print(len(results))