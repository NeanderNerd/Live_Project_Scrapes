# Title: Scrape of Zoom+Care.com for open positions
# Course: Live Project
# Author: Christoher L. Garrick
# Purpose: Prosper IT Job Board App Project in association with The Tech Academy
#          and PortladTech.Org.

# Import all required modules
from bs4 import BeautifulSoup
import requests
import json

# Declare Raw Data
company = "Zoom+Care"
baseurl = "http://www.zoomcare.com"
url = baseurl + "/careers/open-positions"
jobs = []

# Establish link with webpage to scrape.
r = requests.get(url)
try:
    r.raise_for_status()
except Exception as exc:
    print('there was a problem: %s' % (exc))

data = r.text
soup = BeautifulSoup(data, 'html.parser')

# Find and iterate through all divs containing the lists of jobs and get the
# location from it's previous sibling. Iterate through the list of jobs and
# get the information saved into a dictionary called job. Then save each job
# into the list of jobs.
for links in soup.find_all('div', class_="block block-views"):

    jobLocation = links.find_previous_sibling('div', class_="block block-block cities").get('id')

    for link in links.find_all('tr', class_="odd views-row-first"):

        jobTitle = link.find_next('a').contents[0]
        applicationLink = link.find_next('a').get('href')
        applicationLink = baseurl + applicationLink

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
        print(job)
    print(len(jobs))

# Convert jobs list of dictionaries to .json file.
with open(company + '.json', 'w') as outfile:
    json.dump(jobs, outfile)
