import requests
from bs4 import BeautifulSoup


def baseURL():
    BASEURL = 'https://hk.jobsdb.com/hk/search-jobs'
    return BASEURL


def url_2_query(baseURL, pageNo, query, testMode=False):

    if testMode:
        pageNo = 1
        query = 'python'

    URL2Query = f'{baseURL}/{query}/{pageNo}'

    return URL2Query


def fetch_data_from_URL(URL2Query):
    sessionRes = requests.Session()
    pageData = sessionRes.get(URL2Query)
    soup = BeautifulSoup(pageData.text, 'html5lib')
    return soup
