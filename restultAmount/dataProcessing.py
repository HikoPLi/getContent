import re
import requests
import handleInternetData


def count_result(baseURL, pageNo, query):

    soup = handleInternetData.fetch_data_from_URL(
        handleInternetData.url_2_query(baseURL, pageNo, query, True))

    result_count_element = soup.find(
        'div', {'data-automation': 'searchResultBar'})

    result_count_text = result_count_element.find(
        'span', {'class': 'y44q7i21'}).text
    result_count = re.findall(r"of\s+(.*?)\s+jobs", result_count_text)[0]

    # return amount
    return result_count
