import requests #HTTP 요청을 보내는 모듈(url가져오기)
from bs4 import BeautifulSoup #html에서 정보를 추출하기 위한 package

LIMIT = 50
URL = f"https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=python&limit={LIMIT}"


def get_last_page():

  # 해당 url로 get 요청을 보냈다.
  result = requests.get(URL) 
  # print(result.text) #html 전부 가져오기
  soup = BeautifulSoup(result.text, "html.parser")# BeautifulSoup이 이해할 수 있도록 값을 전달하는 것
  pagination = soup.find("div", {"class":"pagination"}) #indeed_soup에서 pagination 찾기 / 태그값을 기준으로 내용 불러오기(최초 건색 결과만 출력)
  links = pagination.find_all('a') #pagination에서 a로 되어있는 모든 태그 불러오기/[리스트]
  
  pages = []
  for link in links[:-1]:
    pages.append(int(link.string)) #string만 가져오기

  max_page = pages[-1]

  return max_page



def extract_job(html):
    title = html.find("h2", {"class": "title"}).find("a")["title"]
    company = html.find("span",{"class": "company"})
    company_anchor = company.find("a")
    if company_anchor is not None:
      company = str(company_anchor.string)
    else:
      company = str(company.string)
    company = company.strip()
    location  = html.find("span",{"class":"location"}).string
    job_id = html["data-jk"] #한국 indeed에는 없습니다.
  
    return {'title': title, 'company': company, 'location': location, "link":f"https://kr.indeed.com/viewjob?jk={job_id}"}




def extract_jobs(last_page):
# 각 일자리 정보를 가져오고 일자리를 return한다
  jobs = []
  for page in range(last_page):
    print(f"Scrapping indeed_page {page}")
    result = requests.get(f"{URL}&start={0*LIMIT}")
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("div",{"class": "jobsearch-SerpJobCard"})
    for result in results:
      job = extract_job(result)
      jobs.append(job)    
  return jobs


def get_jobs():
  last_page = get_last_page() 
  jobs = extract_jobs(last_page)
  return jobs
