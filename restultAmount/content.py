# import handleInternetData
from bs4 import BeautifulSoup
import exportContentToFile


def content(page):

    with open(f"html{page}.html") as html:
        soup = BeautifulSoup(html, "html.parser")
        divs = soup.find_all("h1")

    # table = handleInternetData.fetch_data_from_URL(URL).findAll('h1') # find query in html

    for row in divs:
        text = row.text
        exportContentToFile.exportContentToFile(text)
