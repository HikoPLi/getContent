from checkButton import checkButton
from checkButton import URL
from checkButton import content
from checkButton import rewrite


def main():
    rewrite.rewrite()
    i = 1
    while i < 999:
        if checkButton.checkButton(URL.URL(i)) == False:
            i = i + 1
            content.content(URL.URL(i))
        if checkButton.checkButton(URL.URL(i)) == True:
            break


main()
