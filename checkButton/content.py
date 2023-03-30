from checkButton import request
from checkButton import exportContentToFile


def content(URL):
    table = request.request(URL).findAll('h1')

    for row in table:
        text = row.text
        # print(text)
        exportContentToFile.exportContentToFile(text)
