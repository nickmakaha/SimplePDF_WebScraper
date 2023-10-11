import requests
 
# for tree traversal scraping in webpage
from bs4 import BeautifulSoup
 
# for input and output operations
import io
 
# For getting information about the pdfs
from PyPDF2 import PdfFileReader

cookies = {
    'csrftoken': 'Sj97Q99fZZ1ZM8mofQphyUBzJOPGp6Ei',
    'sessionid': '9490afca63e0a282db6425ccf02c977a',
    'iwe_term_enrollment_urn%3amace%3aucla.edu%3appid%3aperson%3aDDF571DAAD6E4C8298F55D00D8ECC88B': '23F',
    '_hp2_id.3001039959': '%7B%22userId%22%3A%224554400192369438%22%2C%22pageviewId%22%3A%22390133472406216%22%2C%22sessionId%22%3A%226270327147447193%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D',
    'MCPopupClosed': 'yes',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    # 'Cookie': 'csrftoken=Sj97Q99fZZ1ZM8mofQphyUBzJOPGp6Ei; sessionid=9490afca63e0a282db6425ccf02c977a; iwe_term_enrollment_urn%3amace%3aucla.edu%3appid%3aperson%3aDDF571DAAD6E4C8298F55D00D8ECC88B=23F; _hp2_id.3001039959=%7B%22userId%22%3A%224554400192369438%22%2C%22pageviewId%22%3A%22390133472406216%22%2C%22sessionId%22%3A%226270327147447193%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D; MCPopupClosed=yes',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

baseurl = 'https://upe.seas.ucla.edu/testbank/'
r = requests.get('https://upe.seas.ucla.edu/testbank/', cookies=cookies, headers=headers)


soup = BeautifulSoup(r.text)
urls = []
names = []
for i, link in enumerate(soup.findAll("a")):
   # print("test")
    _FULLURL = (baseurl + str(link.get("href")))
    if _FULLURL.endswith(".pdf"):
        print(_FULLURL)
        urls.append(_FULLURL)
        names.append(soup.select("a")[i].attrs["href"])
        


names_urls = zip(names, urls)
print(names_urls)
for name, url in names_urls:
   # print(url)
    split = url.split('/testbank')
   # print(split)
    rurl = split[0]
    rurl += '/testbank'
    rurl += split[2]
    re = requests.get(rurl, cookies=cookies, headers=headers)
    with open("pdfs/" + name.split('/')[-1], "wb") as f:
        f.write(re.content)