import os
import fileIO
import time
# ---for function
import getToGrandparentDir
import handleInternetData
import content


def choice4text(query, baseURL, lastPage):
    print(str(os.getcwd()))
    startTime = time.time()
    # os.chdir("../restultAmount/fetchHTML")
    print(f"Processing! Please wait!")
    # getToGrandparentDir.grandparentDir()
    # os.chdir('../restultAmount/data')
    fileIO.rewrite()
    page = 0
    while page < lastPage:
        page = page + 1
        url = handleInternetData.url_2_query(baseURL, page, query)
        handleInternetData.fetch_data_from_URL(url)
        content.content(page)

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
