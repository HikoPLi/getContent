from checkButton import request


def checkButton(url):

    table = request.request(url).findAll('button')
    for row in table:
        text = row.text
        if 'Next' in text:
            return True
        else:
            return False
