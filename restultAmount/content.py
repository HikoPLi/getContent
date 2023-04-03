from bs4 import BeautifulSoup
import exportContentToFile


def content(page):

    with open(f"html{page}.html") as html:
        soup = BeautifulSoup(html, "html.parser")
        divs = soup.find_all("h1")

    for row in divs:
        text = row.text
        exportContentToFile.exportContentToFile(text)
