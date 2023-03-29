from bs4 import BeautifulSoup
import requests
import URL


def pageS(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    select_element = soup.select_one('select[id="pagination"]')
    option_elements = select_element.select('option')
    last_option_element = option_elements[-1]
    last_option_value = last_option_element['value']
    return last_option_value
