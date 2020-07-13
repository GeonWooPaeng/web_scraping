import csv 

def save_to_file(jobs):
  file = open("jobs.csv", mode="w")# 쓰기 용 file 만들기 
  writer = csv.writer(file)
  writer.writerow(["title", "company", "location", "link"])
  
  for job in jobs:
    #title,company,location,link가 모여있는 곳에서 제목빼고 내용만 저장하는 방법
    #job은 dict입니다.
    writer.writerow(list(job.values()))
  return