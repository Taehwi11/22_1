from bs4 import BeautifulSoup
import pandas as pd
import requests

store_address=[]
store_number=[]
store_parking=[]
store_yeah=[]
for n in range(1,10):
    req=requests.get("http://www.blushaak.co.kr/bbs/board.php?bo_table=franchise&page={}".format(n))
    html=req.text
    soupblue = BeautifulSoup(html, 'html.parser')
    store_name =soupblue.select('div.title>span')
    store_imformation=soupblue.select('li>span')
   
    for i in range(len(store_imformation)//3):
        store_address.append(store_imformation[3*i].text)
        store_number.append(store_imformation[3*i+1].text)
        store_parking.append(store_imformation[3*i+2].text)
    
    for e in zip(store_name,store_address,store_number,store_parking):
        store_yeah.append({'매장명':e[0].text, '주소':e[1], '전화번호':e[2],'주차여부':e[3]})

    for a in store_yeah:
        print(a)
df =pd.DataFrame(store_yeah)
df.to_csv('./6장_data/blueskak.csv', encoding='cp949', mode='w', index=True)