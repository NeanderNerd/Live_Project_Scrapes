# Title: Scrape of Ziba.com for open positions
# Course: Live Project
# Author: Christopher L. Garrick
# Purpose: Prosper IT Job Board App Project in association with
#          The Tech Academy and PortlandTech.Org.

# Import all required modules
from bs4 import BeautifulSoup
import requests
import os.path
import json

# Create a function to separate out data that is not a job posting.
def complete(dictionary):
    if dictionary.get('Location') == 'Portland, OR':
        return(True)

# Establish raw data.
company = "Ziba"
htmlFile = "temp/" + company + "html.txt"
baseurl = "https://www.ziba.com"
url = baseurl + "/careers"
jobs = []
other = []

# Establish link with web page to scrape and save html from
# web page to data and parse with BeautifulSoup.
r = requests.get(url)
try:
    r.raise_for_status()
except Exception as exc:
    print('there was a problem: %s' % (exc))

data = r.text
soup = BeautifulSoup(data, "html.parser")

# Find all Divisions in the parsed website HTML with the class that contains
# the job data and divide all data into separate variables. Save all data to
# a dictionary named job in the format the Job Board App needs and run the function
# to separate real job data from all the other unwanted data unfortunately
# provided.
for link in soup.find_all('div', class_="sqs-block html-block sqs-block-html"):
    jobTitle = link.find_next('a').contents[0]
    jobLocation = link.find_next('h3').contents[0]
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
        'Salary': '',
    }
    if complete(job):
        jobs.append(job)
        #print(job)
    else:
        other.append(job)

# The only way I was able to get the actual job dictionaries to append
# to the jobs list was to make another 'other' list and save the unwanted
# data to it. I'm not sure why I had to waste RAM in this situation but,
# it was the only way it would work.
#print(len(jobs))
#print(len(other))

# Create .json file and add the jobs list of dictionaries to it for the
# Job Board App.
with open(company + '.json', 'w') as outfile:
    json.dump(jobs, outfile)