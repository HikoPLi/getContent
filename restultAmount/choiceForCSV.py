# all for functions
import export2CSV
import handleInternetData


def choice4CSV(query, baseURL, lastPage):
    print(f"Processing! Please wait!")
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
