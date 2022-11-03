import requests
from lxml import html

s = requests.Session()

link1 = 'https://org.mephi.ru/pupil-rating/get-rating/entity/9729/original/no'
link2 = 'https://org.mephi.ru/pupil-rating/get-rating/entity/9054/original/no'
link3 = 'https://org.mephi.ru/pupil-rating/get-rating/entity/9743/original/no'
link4 = 'https://org.mephi.ru/pupil-rating/get-rating/entity/9744/original/no'

for link in [link1, link2, link3, link4]:
    r = s.get(link)
    if r.status_code == 200:
        tree = html.fromstring(r.content)
        elements = tree.xpath('//tr')
        for element in elements:
            if len(element.getchildren()) > 1:
                print(str(element.getchildren()[2].text).strip(), len(element.getchildren()[1].getchildren()) > 0)
