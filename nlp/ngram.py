from bs4 import BeautifulSoup
import requests
import re
import random

from collections import defaultdict


def fix_unicode(text):
    return text.replace(u"\u2019", "'")

url = "http://radar.oreilly.com/2010/06/what-is-data-science.html"
html = requests.get(url).text
soup = BeautifulSoup(html, 'html5lib')

content = soup.find("div", "entry-content")                         # find entry-content div
regex = r"[\w']+|[\.]"                                              # matches a word or a period

document = []

for paragraph in content("p"):
    words = re.findall(regex, fix_unicode(paragraph.text))
    document.extend(words)

bigrams = zip(document, document[1:])
transitions = defaultdict(list)
for prev, current in bigrams:
    transitions[prev].append(current)

def generate_using_bigrams():
    current = "."                                                   # this means the next word will start a sentence
    result = []
    while True:
        next_word_candidates = transitions[current]                 # bigrams (current, _)
        current = random.choice(next_word_candidates)               # choose one at random
        result.append(current)                                      # append it to results
        if current == ".": return " ".join(result)                  # if ".", then we're done

trigrams = zip(document, document[1:], document[2:])
trigram_transitions = defaultdict(list)
starts = []

for prev, current, next in trigrams:
    if prev == ".":                                                 # if the previous "word" was a period
        starts.append(current)                                      # then this is a start word

    trigram_transitions[(prev, current)].append(next)

