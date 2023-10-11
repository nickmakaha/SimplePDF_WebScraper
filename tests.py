import requests
 
# for tree traversal scraping in webpage
from bs4 import BeautifulSoup
 
# for input and output operations
import io
 
# For getting information about the pdfs
from PyPDF2 import PdfFileReader

cookies = {
    
}

headers = {
    
}

baseurl = 'https://nickdj.me/files'
r = requests.get('https://nickdj.me/files')

#print(r.text)
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
   # print("test")
    re = requests.get(url, cookies=cookies, headers=headers)
    with open("pdfs2/" + name.split('/')[-1], "wb") as f:
        f.write(re.content)