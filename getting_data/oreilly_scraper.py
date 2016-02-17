from bs4 import BeautifulSoup
import requests
from time import sleep
from collections import Counter
from oreilly_scraper_functions import *

base_url = "http://shop.oreilly.com/category/browse-subjects/data.do?sortby=publicationDate&page="

books = []

NUM_PAGES = 31

for page_num in range(1, NUM_PAGES+1):
    print "souping page", page_num, ",", len(books), " found so far."
    url = base_url + str(page_num)
    soup = BeautifulSoup(requests.get(url).text, 'html5lib')
    
    for td in soup('td', 'thumbtext'):
        if not is_video(td):
            books.append(book_info(td))
    
    # respect the robots.txt
    sleep(30)

def get_year(book):
    """book["date"] looks like 'November 2014' so we need to split on the space 
    and then take the second piece"""
    
    return int(book["date"].split()[1])

year_counts = Counter(get_year(book) for book in books
                      if get_year(book) <= 2014)

import matplotlib.pyplot as plt
years = sorted(year_counts)
book_counts = [year_counts[year] for year in years]
plt.plot(years, book_counts)
plt.ylabel("# of data books")
plt.title("Data is big!")
plt.show()