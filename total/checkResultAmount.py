import re
import requests
from bs4 import BeautifulSoup


def checkAmount(query):

    query = input("Search: ")

    url = f'https://hk.jobsdb.com/hk/search-jobs/{query}/1'

    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')

    result_count_element = soup.find(
        'div', {'data-automation': 'searchResultBar'})

    result_count_text = result_count_element.find(
        'span', {'class': 'y44q7i21'}).text
    result_count = re.findall(r"of\s+(.*?)\s+jobs", result_count_text)[0]

    # return amount
    return result_count
