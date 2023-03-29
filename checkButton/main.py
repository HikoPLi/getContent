import checkButton
import URL
import content


def main():
    i = 1
    while i < 999:
        if checkButton.checkButton(URL.URL(i)) == False:
            i = i + 1
            content.content(URL.URL(i))
        if checkButton.checkButton(URL.URL(i)) == True:
            break


main()
