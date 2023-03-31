import handleInternetData
import exportContentToFile


def content(URL):
    table = handleInternetData.fetch_data_from_URL(URL).findAll('h1')

    for row in table:
        text = row.text
        exportContentToFile.exportContentToFile(text)
