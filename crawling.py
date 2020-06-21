from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from mongo.mongodb import MongoCon

db = MongoCon()

ref_url = 'https://www.hallym.or.kr'
base_url = ref_url + '/hallymuniv_sub.asp?left_menu=left_health&screen=ptp118&alphabet='
url_list = [
    'A',
    'B',
    'C',
    'D',
    'E',
    'F',
    'G',
    'H',
    'I',
    'J',
    'K',
    'L',
    'M',
    'N',
    'O',
    'P',
    'Q',
    'R',
    'S',
    'T',
    'U',
    'V',
    'W',
    'X',
    'Y',
    'Z'
]


def get_all_term(elem):
    ol = elem.find_all('ol', {'class': 'sch_list'})[0]

    term_list = ol.select('li')
    word_list = []

    for i in range(len(term_list)):
        term_one = term_list[i]

        splited = term_one.text.split(':')
        word_list.append({'word': splited[0].strip(), 'mean': splited[1].strip(), 'ref': ref_url})

    return word_list


for i in range(len(url_list)):
    url = base_url + url_list[i]

    html = urlopen(url)
    bsObject = bs(html, "html.parser")

    word_list = get_all_term(bsObject)

    for j in range(1, 100000):
        temp_url = url + "&search_type=&search_text=&page=" + str(j + 1)
        html = urlopen(temp_url)

        bsObject = bs(html, "html.parser")
        divs = bsObject.find_all('div')
        temp_word_list = get_all_term(bsObject)

        if len(divs) == 0 or len(temp_word_list) == 0:
            break

        word_list.extend(temp_word_list)

    db.update_word(word_list)
    print('{} : {} is inserted'.format(url_list[i], len(word_list)))
