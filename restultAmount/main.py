import dataProcessing
import math
import content
import fileIO
import export2CSV
import handleInternetData
import os


def choice4text(baseURL, lastPage):
    print(f"Processing! Please wait! Total page: {lastPage}")
    os.chdir('../restultAmount/data')
    fileIO.rewrite()
    page = 0
    while page < lastPage:
        page = page + 1
        url = handleInternetData.url_2_query(baseURL, page, query, True)
        handleInternetData.fetch_data_from_URL(url)
        content.content(url)

        if page == lastPage:
            print("End of Operation! Thank for using!")
            break
    return page


def choice4CSV(baseURL, lastPage):
    print(f"Processing! Please wait! Total page: {lastPage}")
    export2CSV.csvTitle()
    page = 0
    number = 0

    while page < lastPage:
        page = page + 1
        table = handleInternetData.fetch_data_from_URL(
            handleInternetData.url_2_query(baseURL, page, query)).findAll('h1')

        for row in table:
            number = number + 1
            text = row.text
            export2CSV.csvContent(str(query), page, text,
                                  handleInternetData.url_2_query(baseURL, page, query), number)

            if page == lastPage:
                print("End of Operation! Thank for using!")
                break
    return page


def main(query):
    baseURL = handleInternetData.baseURL()
    number_string = dataProcessing.count_result(baseURL, 1, query)
    pages = int(number_string.replace(",", ""))

    lastPage = math.ceil(pages/30)
    print("URL request has been called !")
    print(f"The total page is: {lastPage}")

    print("Which type of file you want to save as")
    userChoice = input(
        ".text or .csv? (text for .text, csv for .csv, all for both)")
    switcher = {
        "csv": choice4CSV,
        "text": choice4text,
        # "all": choice4CSV & choice4text
    }
    switcher.get(userChoice)(baseURL, lastPage)


query = input("Search: ")
main(query)
