from bs4 import BeautifulSoup as bs
import request
import URL


def pageS(URL):
    totalPage = request.request(URL).findAll('select')
    soup = bs(totalPage, 'lxml')
    print(soup.select_one('<select class="z1s6m00 z1s6m01 z1s6m06 z1s6m07 z1s6m0a _1hbhsw6p _1hbhsw69i _1hbhsw65u _1hbhsw65 _16b9myk0 _3reozq0 _3reozq1 y44q7i0 y44q7i1 y44q7i21 y44q7ii y44q7i26 y44q7i18  _1hbhsw632" id="pagination" aria-label="Pagination dropdown">:last-child').text)


pageS(URL.BASEURL())
