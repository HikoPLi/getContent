from bs4 import BeautifulSoup
import time
# functions
import getToGrandparentDir
import export2CSV
import handleInternetData
import os


def choice4CSV(query, baseURL, lastPage):
    startTime = time.time()
    print(f"Processing! Please wait!")
    export2CSV.csvTitle()
    page = 0
    number = 0

    print(str(os.getcwd()))
    os.chdir(f"{os.getcwd()}/{query}")

    while page < lastPage:

        page = page + 1

        with open(f"html{page}.html") as html:
            soup = BeautifulSoup(html, "html.parser")
            divs = soup.find_all("h1")

        for row in divs:
            number = number + 1
            text = row.text
            export2CSV.csvContent(str(query), page, text,
                                  handleInternetData.url_2_query(baseURL, page, query), number)

            if page == lastPage:
                print("End of Operation! Thank for using!")
                break

    try:
        endTime = time.time()
        runTime = endTime - startTime
        print(f"Run time: {runTime}s")
    except:
        print("Run time error!")
    return page
