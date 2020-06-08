#!/usr/bin/env python
# coding: utf-8

# Stackoverflow 크롤링 연습 

# In[4]:


import requests 
from bs4 import BeautifulSoup


# In[12]:


URL = f"https://stackoverflow.com/jobs?q=python"


def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pages = soup.find("div", {"class": "s-pagination"}).find_all('a')
    last_page = pages[-2].get_text(strip=True)
    return int(last_page)


def extract_job(html):
    title = html.find("h2", {"class": "fc-black-800"}).find("a")["title"]
    company, location = html.find("h3", {
        "class": "fc-black-700"
    }).find_all(
        "span", recursive=False)
    company = company.get_text(strip=True)
    location = location.get_text(strip=True).strip(" \r").strip("\n")
    job_id = html["data-jobid"]

    return {
        "title": title,
        "company": company,
        "location": location,
        "apply_link": f"https://stackoverflow.com/jobs/{job_id}"
    }


def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        result = requests.get(f"{URL}&pg={page+1}")
        soup = BeautifulSoup(result.text, 'html.parser')
        results = soup.find_all("div", {"class": "-job"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs


def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    return jobs


# In[14]:


import csv

def save_to_file(jobs):
    file = open("jobs.csv", mode="w" ,encoding="utf-8", newline="")
    writer = csv.writer(file)
    writer.writerow(["title","company","location","apply_link"])
    for job in jobs:
        writer.writerow(list(job.values()))
    return


# In[ ]:


save_to_file(get_jobs())


# Indeed 크롤링 연습 

# In[16]:


LIMIT = 50
URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}"


def extract_indeed_pages():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pagination = soup.find("div", {"class": "pagination"})

    links = pagination.find_all('a')
    pages = []
    for link in links[:-1]:
        pages.append(int(link.string))
    max_page = ages[-1]
    return max_page


def extract_job(html):
    title = html.find("h2", {"class": "title"}).find("a")["title"]
    company = html.find("span", {"class": "company"})
    company_anchor = company.find("a")
    if company_anchor is not None:
        company = str(company_anchor.string)
    else:
        company = str(company.string)
    company = company.strip()
    location = html.find("div", {"class": "recJobLoc"})["data-rc-loc"]
    job_id = html["data-jk"]

    return {
        "title": title,
        "company": company,
        "location": location,
        "link": f"https://www.indeed.com/viewjob?jk={job_id}"
    }


def extract_indeed_jobs(max_page):
  jobs = []
  for page in range(int(max_page)):
    result = requests.get(f"{URL}&start={page*LIMIT}")
    soup = BeautifulSoup(result.text, 'html.parser')
    results = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})
    for result in results:
        job = extract_job(result)
        jobs.append(job)
  return jobs


# In[ ]:





# In[22]:


save_to_file(extract_indeed_jobs(last_page))


# In[18]:





# In[24]:





# In[25]:





# In[ ]:




