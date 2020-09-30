import nltk
from urllib.request import urlopen
from bs4 import BeautifulSoup
import feedparser


# 3.1 Accessing text from the web and from disk
# Electronic books
url = "http://www.gutenberg.org/files/12345/12345.txt"
raw = urlopen(url).read().decode('ascii')
print(raw[:75])

tokens = nltk.word_tokenize(raw)  # returns a list of punctuation and string
text = nltk.Text(tokens)
print(text.collocations())

start_index = raw.find("Chapter I")
end_index = raw.rfind("End of Project Gutenberg's Friday, the Thirteenth")


# Dealing with HTML
url = "http://news.bbc.co.uk/2/hi/health/2284783.stm"
html = urlopen(url).read().decode('ascii')
soup = BeautifulSoup(html, 'html.parser')
raw = soup.get_text()
tokens = nltk.word_tokenize(raw)
text = nltk.Text(tokens)
print(text.concordance('blonde'))


# Processing RSS feeds
llog = feedparser.parse("http://languagelog.ldc.upenn.edu/nll/?feed=atom")
print(llog['feed']['title'])  # u'Language Log'
print(len(llog.entries))
post = llog.entries[2]
print(post.title)
content = post.content[0].value
soup = BeautifulSoup(content, 'html.parser')
print(nltk.word_tokenize(soup.get_text()))


# Reading local files
with open('document.txt') as f:
    raw = f.read()



