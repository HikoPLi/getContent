import URL
import pageS
import content

page = int(pageS.pageS(URL.BASEURL()))

i = 1
while i < page:
    i = i + 1
    URL.URL(i)
    content.content(URL.URL(i))

    if i == page:
        break
