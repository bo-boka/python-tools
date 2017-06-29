import urllib2
from bs4 import BeautifulSoup
import re

opener = urllib2.build_opener()
# opener.addheaders = [{'User-agent', 'Mozilla/5.0'}]

url = ('https://en.wikipedia.org/wiki/Category:Programming_language_concepts')

ourUrl = opener.open(url).read()

soup = BeautifulSoup(ourUrl, "html.parser")

for link in soup.findAll('a', attrs={'href': re.compile("^/wiki/")}):
    print link.text

# body = soup.find(text="Origin").findNext('td')
# outfile = open('spidertest.txt', 'w')
# outfile.write(body.text)
