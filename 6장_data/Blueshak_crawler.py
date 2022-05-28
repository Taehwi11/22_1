from bs4 import BeautifulSoup
import pandas as pd
import requests

store_address=[]
store_number=[]
store_parking=[]
store_yeah=[]
for n in range(1,10): #9페이지까지 있으므로 반복
    req=requests.get("http://www.blushaak.co.kr/bbs/board.php?bo_table=franchise&page={}".format(n))
    html=req.text
    soupblue = BeautifulSoup(html, 'html.parser') #html을 불러옴
    store_name =soupblue.select('div.title>span') #매장명 가져옴
    store_imformation=soupblue.select('li>span') #블루샥 홈페이지에 주소,전화번호,주차유무가, 다른 이름으로 되어있지 않아서 한꺼번에 불러옴
   
    for i in range(len(store_imformation)//3): #한꺼번에 가져온 정보를 각각 나누는 작업
        store_address.append(store_imformation[3*i].text)
        store_number.append(store_imformation[3*i+1].text)
        store_parking.append(store_imformation[3*i+2].text)
    
    for e in zip(store_name,store_address,store_number,store_parking): #나눠준 자료들을 합쳐서 하나로 만들어준다
        store_yeah.append({'매장명':e[0].text, '주소':e[1], '전화번호':e[2],'주차여부':e[3]})

    for a in store_yeah:
        print(a)
df =pd.DataFrame(store_yeah) #DataFrame으로 변환
df.to_csv('./6장_data/blueskak.csv', encoding='cp949', mode='w', index=True) #csv형식으로 변환해준다