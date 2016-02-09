from bs4 import BeautifulSoup
import requests

url = "http://shop.oreilly.com/category/browse-subjects/data.do?sortby=publicationDate&page=1"
soup = BeautifulSoup(requests.get(url).text, 'html5lib')

tds = soup('td', 'thumbtext')

def is_video(td):
    """it is a video if it has exactly one pricelabel and starts with 'Video'"""
    pricelabels = td('span', 'pricelabel')
    return (len(pricelabels) == 1 and pricelabels[0].text.strip().startswith("Video"))

print len([td for td in tds if not is_video(td)])

