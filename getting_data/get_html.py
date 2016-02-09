from bs4 import BeautifulSoup
import requests
html = requests.get("http://www.billboard.com").text

print html