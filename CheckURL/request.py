import requests
from bs4 import BeautifulSoup


def request(URL):
    session_object = requests.Session()
    page_obj = session_object.get(URL)
    soup = BeautifulSoup(page_obj.text, 'html5lib')
    return soup
