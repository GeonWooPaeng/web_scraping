import requests #HTTP 요청을 보내는 모듈(url가져오기)
from bs4 import BeautifulSoup #html에서 정보를 추출하기 위한 package

# 해당 url로 get 요청을 보냈다.
indeed_result = requests.get("https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=python&limit=50") 

# print(indeed_result.text) #html 전부 가져오기

indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")# BeautifulSoup이 이해할 수 있도록 값을 전달하는 것

pagination = indeed_soup.find("div", {"class":"pagination"}) #indeed_soup에서 pagination 찾기 / 태그값을 기준으로 내용 불러오기(최초 건색 결과만 출력)

pages = pagination.find_all('a') #pagination에서 a로 되어있는 모든 태그 불러오기/[리스트]
spans = []
for page in pages:
  spans.append(page.find("span"))

spans = spans[:-1]