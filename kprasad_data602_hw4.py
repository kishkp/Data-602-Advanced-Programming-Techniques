import sys
sys.path.append('C:/Users/Administrator/Documents/GitHub/alchemyapi_python')

from alchemyapi import AlchemyAPI
from bs4 import BeautifulSoup
import urllib2

url = ('http://tech.firstpost.com/news-analysis/blackberry-pulls-out-from-the-devices-business-and-no-ones-surprised-338013.html')
html = urllib2.urlopen(url).read()
soup = BeautifulSoup(html)

# remove script and style elements
for script in soup(["script", "style"]):
    script.extract()    

# get text
html_text = soup.get_text()

#from alchemyapi import AlchemyAPI
alchemyapi = AlchemyAPI()
response = alchemyapi.keywords('text', html_text)

print "Ranked list of Keywords and Relevance \n"
rank = 0
for keyword in response['keywords'][1:10]:
    rank = rank + 1
    print 'Rank: ', rank, '\tKeyword: ', keyword['text'].encode('utf-8'), '\tRelevance: ', keyword['relevance'].encode('utf-8')
