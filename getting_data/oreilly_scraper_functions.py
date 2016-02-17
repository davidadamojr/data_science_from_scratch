from bs4 import BeautifulSoup
import requests
import re

def is_video(td):
    """it is a video if it has exactly one pricelabel and starts with 'Video'"""
    pricelabels = td('span', 'pricelabel')
    return (len(pricelabels) == 1 and pricelabels[0].text.strip().startswith("Video"))

def book_info(td):
    """given a BeautifulSoup <td> Tag representing a book, extract the book's details 
    and return a dict"""
    
    title = td.find("div", "thumbheader").a.text
    author_name = td.find("div", "AuthorName").text
    authors = [x.strip() for x in re.sub("^By ", "", author_name).split(",")]
    isbn_link = td.find("div", "thumbheader").a.get("href")
    isbn = re.match("/product/(.*)\.do", isbn_link).groups()[0]
    date = td.find("span", "directorydate").text.strip()
    
    return {
            "title": title,
            "authors": authors,
            "isbn": isbn,
            "date": date
            }

