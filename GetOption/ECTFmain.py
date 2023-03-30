from GetOption import URL
from GetOption import pageS
import content
import rewrite

page = int(pageS.pageS(URL.BASEURL()))
rewrite.rewrite()
i = 1
while i < page:
    i = i + 1
    URL.URL(i)
    content.content(URL.URL(i))

    if i == page:
        break
