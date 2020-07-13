import requests #HTTP 요청을 보내는 모듈(url가져오기)
from bs4 import BeautifulSoup #html에서 정보를 추출하기 위한 package

URL = f"https://stackoverflow.com/jobs?q=python&sort=i"

def get_last_page():
  result = requests.get(URL)
  soup = BeautifulSoup(result.text, "html.parser")
  pages = soup.find("div", {"class" : "s-pagination"}).find_all("a")
  last_page = pages[-2].get_text(strip=True)
  return int(last_page)




def extract_job(html):
  title = html.find("h2",{"class" : "fs-body3"}).find("a")["title"]

  company, location = html.find("h3",{"class" : "fs-body1"}).find_all("span", recursive=False) #find_all로 span을 전부 가져오는 것을 방지한다(첫 단계 span만 가져온다), [company, location]인 리스트
  # print(company.get_text(strip=True), location.get_text(strip=True)) #문자만 가져오고 빈칸을 없애준다.
  company = company.get_text(strip=True)
  location = location.get_text(strip=True)
  job_id = html['data-jobid']
  return {'title' : title, 'company': company, 'location' : location, 'apply_link' : f"https://stackoverflow.com/jobs/{job_id}"}



def extract_jobs(last_page):
  jobs = [] 
  for page in range(last_page):
    print(f"Scraping so_Page: {page}")
    result = requests.get(f"{URL}&pg={page+1}")
    # print(result.status_code) # 확인 코드 잘 되면 200 출력
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("div", {"class":"-job"})
    for result in results:
      job = extract_job(result)
      jobs.append(job)
    return jobs


def get_jobs():
  last_page = get_last_page()
  jobs = extract_jobs(last_page)
  return jobs