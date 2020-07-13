from indeed import get_jobs as get_indeed_jobs 
from so import get_jobs as get_so_jobs
from save import save_to_file

indeed_jobs = get_indeed_jobs() 
so_jobs = get_so_jobs()
jobs = indeed_jobs + so_jobs
save_to_file(jobs)


#CSV -> Comma Separated Value #excel 확장 명
#CSV file을 잘 열고 싶으면 google sheets에서 csv file을 upload하면 됩니다.