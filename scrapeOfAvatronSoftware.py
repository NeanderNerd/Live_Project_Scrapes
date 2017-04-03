# Title: Scrape of Avatron Software
# Course: Live Project
# Author: Christopher L. Garrick
# Purpose: Prosper IT Job Board App Project in association
#          with The Tech Academy and PortladTech.Org.
# This Scrape was pretty straight forward until I reached
# the end and found out I was getting a duplicate posting.
# I decided to iterate through the list and compare them
# to find and remove the duplicate.

from bs4 import BeautifulSoup
import requests
import json

company = 'Avatron_Software'
url = "https://avatron.com/about/jobs/"
jobHours = "Full Time"
jobLocation = "Portland, OR"
jobs = []

r = requests.get(url)
try:
    r.raise_for_status()
except Exception as exc:
    print('there was a problem %s' % (exc))

data = r.text
soup = BeautifulSoup(data, 'html.parser')

for link in soup.find_all('div', class_='avia_textblock'):
    if link.find_next('h2'): # This if statement was necessary because
                             # there were multiple divs fitting the
                             # description above and I only wanted the
                             # ones with an h2 tag because those were the
                             # job postings.
        jobTitle = link.find_next('h2').contents[0]
        applicationLink = link.find_next('a').get('href')
        job = {
            'ApplicationLink': applicationLink,
            'Company': company,
            'DatePosted': '',
            'Experience': '',
            'Hours': jobHours,
            'JobID': '',
            'JobTitle': jobTitle,
            'LanguagesUsed': '',
            'Location': jobLocation,
            'Salary': '',
        }
        jobs.append(job)
    if len(jobs) > 1:
        for i in range(len(jobs)-1):
            if job == jobs[i-2]:
                jobs.remove(job)


with open(company + '.json', 'w') as outfile:
    json.dump(jobs, outfile)