import sys
from requests import get
from bs4 import BeautifulSoup



def make_request(url):
    headers = {
    'Host': 'thebookstore.tru.ca',
    'Connection': 'keep-alive',
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36",
    'Accept': "*/*",
    'Referer': 'https://thebookstore.tru.ca/buy_courselisting.asp?control=course&course=38044&term=181',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-CA,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
    'DNT': 1
    }
    r = get(url,headers=headers)
    return BeautifulSoup(r.text, 'html.parser')

def get_download_link(search_term):z
    libgen = 'http://gen.lib.rus.ec/search.php?req={}&lg_topic=libgen&open=0&view=simple&res=25&phrase=0&column=def'
    md5link = 'http://gen.lib.rus.ec/get.php?md5={}'

    r = get(libgen.format(search_term))
    soup = BeautifulSoup(r.text, 'html.parser')

    md5_s = soup.findAll("a")
    for i in md5_s:
        if 'md5' in i.attrs['href']:
            md5 = i.attrs['href'].split('=')[1]
            return (md5link.format(md5))
    return -1

def get_course_number(subj_num,term,num):
    soup = make_request("https://thebookstore.tru.ca/textbooks_xml.asp?control=department&dept={}&term={}".format(subj_num,term))
    courses = soup.findAll('course')
    for i in courses:
        if(i['name'] == num):
            return i['id']

def get_subject_id(subject,term,campus):
    soup = make_request("https://thebookstore.tru.ca/textbooks_xml.asp?control=campus&campus={}&term={}".format(campus,term))
    departments = soup.findAll('department')
    for i in departments:
        if(i['abrev'] == subject):
            return i['id']

def get_section_id(course_id,term,section_num):
    soup = make_request("https://thebookstore.tru.ca/textbooks_xml.asp?control=course&course={}&term={}".format(course_id,term))
    sections = soup.findAll('section')
    if(len(sections) == 1):
        return sections[0]['id']
    for i in sections:
        if(i['name'] == section_num):
            return i['id']

def get_isbn(section,term):
    soup = make_request("https://thebookstore.tru.ca/textbooks_xml.asp?control=section&section={}&term={}".format(section,term))
    for i in range(1,10):
        isbn_str = "isbn-{}".format(i)
        isbn = soup.find("input", {"id": isbn_str})
        #print(isbn_str)
        if isbn is not None:
            return isbn.attrs['value']

    if(soup.find("input", {"id": "sku-new-1"}) is not None):
        return -1 #'No Textbooks in stock'
    else:
        return -2 #'No Textbooks for this Course'

def main(Subj,Num,Sect,DateCode,Campus):
    id = get_subject_id(Subj,DateCode,Campus)
    num = get_course_number(id,DateCode,Num)
    section_id = get_section_id(num,DateCode,Sect)
    isbn = get_isbn(section_id,DateCode)
    link = get_download_link(isbn)

    if(isbn == -1):
        return('No Textbooks in stock')
    if(isbn == -2):
        return('No Textbooks for this Course')
    if(link == -1):
        return('No books found on libgen')

    return link
