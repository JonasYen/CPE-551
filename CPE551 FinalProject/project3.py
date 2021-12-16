from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver


executable_path = '/CPE551/FinalProject/driver/chromedriver'
page_url = 'https://www.amazon.com/stores/page/8B4E4A2F-87D2-4D79-B8F7-DB5C135D66D6?ingress=0&visitId=fcb524f3-c1d1-4b0e-a744-116090c65280&lp_slot=auto-sparkle-hsa-tetris&store_ref=SB_A03752781QNONGPKTSEBZ&ref_=sbx_be_s_sparkle_ssd_hl'
results = []# variable to hold all reviews
driver = webdriver.Chrome(executable_path=executable_path)
limit = 1
page = driver.get(page_url)

for i in range(limit):
    
    temp = []
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    divs = soup.select('li.ProductGridItem__itemOuter__5ow0w.ProductGridItem__fixed__1w9d4')


    for idx, div in enumerate(divs):
        desc = None
        price = None   
        p_desc = div.select('div.ProductGridItem__itemInfo__s_dZ2 div.ProductGridItem__itemInfoChild__1HpO6 div.Title__truncateTitle__3ekKu')
        if p_desc != []:
            desc = p_desc[0].get_text()
   
        p_price = div.select('div.ProductGridItem__price__2H_kW span.price.style__xlarge__1mW1P.ProductGridItem__buyPrice__6DIeT.style__fixedSize__2cXU- ')
        if p_price != []:
            price = p_price[0].get_text(strip = True)
        temp.append((desc, price))
        
    results += temp

results = pd.DataFrame(results, columns=['name', 'price'])

print(results)
# print(len(results))