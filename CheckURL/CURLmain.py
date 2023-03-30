import checkURL
import content
import rewrite


def main():
    rewrite.rewrite()
    i = 1
    while i < 99999:

        if checkURL.checkURL(checkURL.URL(i)) == False:
            break

        if checkURL.checkURL(checkURL.URL(i)) == True:
            i = i + 1
            content.content(checkURL.URL(i))


main()
