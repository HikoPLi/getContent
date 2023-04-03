# library
import math
import time
# fuctions
import choiceForCSV
import handleInternetData
import choiceForText
import dataProcessing


def main():
    query = input("Search: ")  # For users input search
    baseURL = handleInternetData.baseURL()  # Base URL the users get
    numberString = dataProcessing.count_result(
        baseURL, 1, query)  # use page 1 for the basic URL and get total number of elements
    pages = int(numberString.replace(",", ""))
    # final numbers are like ***,**. Change to number without ","

    lastPage = math.ceil(pages/30)  # getting total pages and ceiling
    print("URL request has been called !")
    print(f"The total page is: {lastPage}")

    print("Which type of file you want to save as")  # for users choose
    userChoice = input(
        ".text or .csv? (text for .text, csv for .csv)")
    switcher = {
        "csv": choiceForCSV.choice4CSV,
        "text": choiceForText.choice4text
    }
    switcher.get(userChoice)(query, baseURL, lastPage)


if __name__ == '__main__':
    main()
