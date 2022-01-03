import urllib.request
from bs4 import BeautifulSoup
from dom import Dom
import json
class TopDev:
    def __init__(self,keyword):
        self.keyword = keyword
    def jobSearch(self):
        return 'https://topdev.vn/viec-lam-it/' + self.keyword.replace(' ', '-') + '?filter=list_jobs'
    def getJobUrls(self):
        url = self.jobSearch()
        html = Dom(url).extractHTML()
        jobs = html.findAll('div', class_='list__job')[0].findAll('div',class_='cont')
        job_urls = []
        for job in jobs:
            job_urls.append('https://topdev.vn' + job.findAll('a',class_='job-title')[0].get('href'))
        return job_urls
    def getJobsDetail(self):
        urls = self.getJobUrls()
        jobs = []
        for url in urls:
            html = Dom(url).extractHTML()
            string_data = html.findAll('script')[1].text
            object_data = json.loads(string_data)
            job = {}
            # post_type
            post_type = object_data['@type']
            job['post_type'] = post_type
            # industry
            industry = object_data['industry']
            job['industry'] = industry
            # job title
            job_title = object_data['title']
            job['job_title'] = job_title
            # date posted
            date_posted = object_data['datePosted']
            job['date_posted'] = date_posted
            # date valid through
            date_valid_through = object_data['validThrough']
            job['date_valid_through'] = date_valid_through
            # skills
            skills = object_data['skills']
            job['skills'] = skills

            # baseSalary
            base_salary_currency = object_data['baseSalary']['currency']
            job['base_salary_currency'] = base_salary_currency
            # base_salary_value
            base_salary_value = object_data['baseSalary']['value']['value']
            job['base_salary_value'] = base_salary_value

            # job_description
            job_description = BeautifulSoup(object_data['description'], "html.parser").text.strip()
            job['job_description'] = job_description

            # hiringOrganization
            # organization_name
            organization_name = object_data['hiringOrganization']['name']
            job['organization_name'] = organization_name

            # organization_description
            organization_description = object_data['hiringOrganization']['description']
            job['organization_description'] = organization_description

            # employmentType
            employment_type = object_data['employmentType'][0]
            job['employment_type'] = employment_type

            # jobBenefits

            benefits = BeautifulSoup(object_data['jobBenefits'], "html.parser").findAll('li')
            job_benefits = []
            for benefit in benefits:
                job_benefits.append(benefit.text.strip())
            job_benefits = '\n'.join(job_benefits)
            job['job_benefits'] = job_benefits

            # jobLocation
            # street_address
            street_address = object_data['jobLocation']['address'][0]['streetAddress']
            job['street_address'] = street_address
            # address_locality
            address_locality = object_data['jobLocation']['address'][0]['addressLocality']
            job['address_locality'] = address_locality
            # address_country
            address_country = object_data['jobLocation']['address'][0]['addressCountry']
            job['address_country'] = address_country
            # postal_code
            postal_code = object_data['jobLocation']['address'][0]['postalCode']
            job['postal_code'] = postal_code
            # address_region
            address_region = object_data['jobLocation']['address'][0]['addressRegion']
            job['address_region'] = address_region

            if 'experienceRequirements' in object_data:
                experience = object_data['experienceRequirements']['monthsOfExperience']
                job['experience'] = experience
            else:
                job['experience'] = 'NaN'
            jobs.append(job)
        return jobs