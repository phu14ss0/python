import requests
from bs4 import BeautifulSoup




f = open("crawl_data.txt", 'w', -1, "utf-8")        # utf-8 속성이 있어야 파일 쓸 때 인코딩 에러 x
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}    # 멜론 사이트는 헤더 값이 있어야 함
url = 'https://www.melon.com/chart/index.htm'

code = requests.get(url, headers = header).text     # 크롤링할 페이지의 모든 태그를 가져옴
soup = BeautifulSoup(code,'html.parser')            # html 파일을 가져옴
title = soup.find_all("div", {"class":"ellipsis rank01"})       # 노래 제목의 정보는 div 태그의 ellipsis rank01클래스 안에 있음
                                                                # find_all함수는 해당 조건에 맞는 모든 태그를 가져옴
singer = soup.find_all("div", {"class":"ellipsis rank02"})      # 가수의 정보는 div 태그의 ellipsis rank02클래스 안에 있음

real_title = []
real_singer = []

for i in title:
    real_title.append(i.find('a').text)         # html 태그에서 노래 제목만(a 태그의 텍스트 값)
                                                # find함수는 해당 조건에 맞는 하나의 태그만 가져옴. 중복이면 가장 첫 번째 태그

for j in singer:
    real_singer.append(j.find('a').text)        # html 태그에서 가수만(a 태그의 텍스트 값)

for k in range(1,51):   # 차트 순위가 1위~50위
    f.write("{}.{} -{}\n".format(k,real_title[k],real_singer[k]))   # '1(순위).노래제목 -가수'의 형태로 데이터를 저장

f.close()
