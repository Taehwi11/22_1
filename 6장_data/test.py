from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import datetime


from selenium import webdriver
import time

#[CODE 1]
def CoffeeBean_store(result):
    CoffeeBean_URL = "https://www.coffeebeankorea.com/store/store.asp"
    wd = webdriver.Chrome('/Users/김태휘/Desktop/chromedriver_win32/chromedriver.exe')
             
    for i in range(1, 3):  #매장 수 만큼 반복
        wd.get(CoffeeBean_URL)
        time.sleep(1)  #웹페이지 연결할 동안 1초 대기
        try:
            wd.execute_script("storePop2(%d)" %i)
            time.sleep(1) #스크립트 실행 할 동안 1초 대기
            html = wd.page_source
            soupCB = BeautifulSoup(html, 'html.parser')
            result.append(soupCB)
        except:
            continue
    return


def main():
    result = []
    print('Compose_Coffee store crawling >>>>>>>>>>>>>>>>>>>>>>>>>>')
    CoffeeBean_store(result)  #[CODE 1]
    
    CB_tbl = pd.DataFrame(result, columns=('store', 'address','phone'))
    CB_tbl.to_csv('./6장_data/Compose_coffee.csv', encoding='cp949', mode='w', index=True)

if __name__ == '__main__':
     main()