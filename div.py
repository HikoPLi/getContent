import re
from bs4 import BeautifulSoup as bs

html = '''
<div class="_1mil">
    <div class="_2yjq">Медсестра - Регистратор</div>
    <div class="pz-o">
        <span>
            <span>требуемый опыт работы <span>от года до 3 лет</span></span>
        </span>
    </div>
    <div>80 000 — 120 000 тг</div>
</div>

'''

soup = bs(html, 'lxml')
print(soup.select_one('._1mil div:last-child').text)
print(soup.select_one('._1mil div:last-of-type').text)
