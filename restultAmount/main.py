import dataProcessing
import math
import choiceForCSV
import handleInternetData
import choiceForText


def main():
    query = input("Search: ")
    baseURL = handleInternetData.baseURL()
    number_string = dataProcessing.count_result(baseURL, 1, query)
    pages = int(number_string.replace(",", ""))

    lastPage = math.ceil(pages/30)
    print("URL request has been called !")
    print(f"The total page is: {lastPage}")

    print("Which type of file you want to save as")
    userChoice = input(
        ".text or .csv? (text for .text, csv for .csv)")
    switcher = {
        "csv": choiceForCSV.choice4CSV,
        "text": choiceForText.choice4text
    }
    switcher.get(userChoice)(query, baseURL, lastPage)


if __name__ == '__main__':
    main()
