import re
import os
import math
import handleInternetData


def saveHTML(lastPage, soup):
    number = 0
    while number < lastPage:
        number = number + 1
        with open(f'html{number}.html', 'w') as fetchHTML:
            fetchHTML.write(str(soup))

        if number == lastPage:
            break


def fetchHTML(pages, query, soup):
    pages = int(pages.replace(",", ""))
    lastPage = math.ceil(pages/30)
    os.chdir('../restultAmount/fetchHTML')

    if os.path.exists(query) == True:
        os.chdir(query)
        saveHTML(lastPage, soup)

    else:
        os.mkdir(query)
        os.chdir(query)
        saveHTML(lastPage, soup)


def count_result(baseURL, pageNo, query):

    soup = handleInternetData.fetch_data_from_URL(
        handleInternetData.url_2_query(baseURL, pageNo, query))

    resultCountElement = soup.find(
        'div', {'data-automation': 'searchResultBar'})

    resultCountText = resultCountElement.find(
        'span', {'class': 'y44q7i21'}).text
    result_count = re.findall(r"of\s+(.*?)\s+jobs", resultCountText)[0]

    fetchHTML(result_count, query, soup)

    # return amount
    return result_count
