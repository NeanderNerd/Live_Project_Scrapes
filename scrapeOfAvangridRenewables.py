# Title: Scrape of Avangrid Renewables website for open positions
#        in Portland, OR
# Course: Live Project
# Author: Christopher L. Garrick
# Purpose: Prosper IT Job Board App Project in association with
#          The Tech Academy and PortlandTech.Org.
# Scrape Info: This was an interesting scrape in that I had to use
#              Selenium to select the Oregon option in states for the
#              jobs to populate. Great practice and learned a lot about
#              Selenium.

from selenium.webdriver import Firefox
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
import json

company = "Avangrid_Renewables"
baseurl = "https://app.jobcast.net/widget/34344/jobs/page/jobs"
applicationLink = "http://www.avangridrenewables.us/careers.html"
jobLocation = "Portland, Oregon, United States"
jobs = []

driver = Firefox()
driver.get(baseurl)

Select(driver.find_element_by_name("locationKey")).select_by_value('p-18654')

driver.implicitly_wait(5)

jobRoleResultArray = WebDriverWait(driver, 10).until(
    lambda x: x.find_elements_by_xpath("//div[@class='joblist_job_role']")
)
jobMetaResultArray = WebDriverWait(driver, 10).until(
    lambda x: x.find_elements_by_xpath("//div[@class='joblist_job_meta']")
)

for i in range(0, len(jobRoleResultArray), 1):
    a = jobRoleResultArray[i].text
    b = jobMetaResultArray[i].text
    jobTitle = a.replace("Portland, Oregon, United States", "")
    jobPost, jobHours = b.split('\n', 1)
    job = {
        'ApplicationLink': applicationLink,
        'Company': company,
        'DatePosted': jobPost,
        'Experience': '',
        'Hours': jobHours,
        'JobID': '',
        'JobTitle': jobTitle,
        'LanguagesUsed': '',
        'Location': jobLocation,
        'Salary': ''
    }
    jobs.append(job)

with open(company + '.json', 'w') as outfile:
    json.dump(jobs, outfile)