import request
import exportContentToFile


def content(URL):
    table = request.request(URL).findAll('h1')

    for row in table:
        text = row.text
        exportContentToFile.exportContentToFile(text)
