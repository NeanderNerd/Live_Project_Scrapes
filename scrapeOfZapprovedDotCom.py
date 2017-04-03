# This was a tricky scrape because I had to find out where the information was coming from
# and use that link instead of the company website. I was frustrated for about 30 min until
# I remembered to check what I was getting from the website and go from there.
# Title: Scrape of Zapproved.com for open positions in Portland, OR
# Course: Live Project
# Author: Christopher L. Garrick
# Purpose: Prosper IT Job Board App Project in association with
#          The Tech Academy and PortlandTech.Org.

from selenium.webdriver import Firefox
from selenium.webdriver.support.wait import WebDriverWait
import json

driver = Firefox()
driver.get('https://widgets.jobscore.com/jobs/zapproved/'
           'widget_iframe?group_by=department&amp;parent_url=https%3A%2F%2F'
           'www.zapproved.com%2Fabout-us%2Fcareers%2F&amp;widget_id=js_widget_iframe_1')
company = "Zapproved"
baseurl = "http://www.zapproved.com"
jobLocation = 'Portland, OR'
jobs = []
jobResultArray = WebDriverWait(driver, 10).until(lambda x:
                                    x.find_elements_by_xpath('//tr[@class="job clickable"]'))

lengthOfJobResultArray = len(jobResultArray)


for i in range(0, lengthOfJobResultArray, 1):
    a = jobResultArray[i].text
    jobTitle = a.strip(' Portland, OR')
    applicationLink = jobResultArray[i].find_element_by_xpath('//a[@class="job-detail-link"]').get_attribute('href')
    job = {
        'ApplicationLink': applicationLink,
        'Company': company,
        'DatePosted': '',
        'Experience': '',
        'Hours': '',
        'JobID': '',
        'JobTitle': jobTitle,
        'LanguagesUsed': '',
        'Location': jobLocation,
        'Salary': ''
    }
    jobs.append(job)

with open(company + '.json', 'w') as outfile:
    json.dump(jobs, outfile)