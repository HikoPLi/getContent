import os
import fileIO
# ---for function
import handleInternetData
import content


def choice4text(query, baseURL, lastPage):
    print(f"Processing! Please wait!")
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
