import checkURL
import content


def main():
    i = 1
    while i < 99999:

        if checkURL.checkURL(checkURL.URL(i)) == False:
            break

        if checkURL.checkURL(checkURL.URL(i)) == True:
            i = i + 1
            content.content(checkURL.URL(i))


main()
