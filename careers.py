import urllib.request
from bs4 import BeautifulSoup
import json
import pandas as pd
import sys
sys.path.insert(0,'./site')
from topdev import TopDev
def main():
    keywords = 'django,python,data science'
    job_frame = []
    for keyword in keywords.split(','):
        jobs = TopDev(keyword).getJobsDetail()
        job_frame.extend(jobs)
    jobs_frame = pd.DataFrame(job_frame)
    print(jobs_frame)
if __name__ == '__main__':
    main()
