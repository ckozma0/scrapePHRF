from bs4 import BeautifulSoup
import requests
from requests_html import HTMLSession

url = 'http://www.phrfne.org/page/handicapping/base_handicaps'
agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36\
(KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36',
}

# create an HTML Session object
session = HTMLSession()
session.headers.update(headers)
# Use the object above to connect to needed webpage
resp = session.get(url, headers =headers)
 

# Run JavaScript code on webpage
resp.html.render()

soup = BeautifulSoup(resp.html.html, "html.parser")

#table = soup.find("tr")
table = soup.find_all('table')[2]

rows = [str(row.text).strip() for row in table.find_all("tr")]
print(rows)
#sibs = [str(row.next_sibling.replace(u'\xa0', '')).strip() for row in table.find_all('td')]
#print(sibs)
#data = dict(zip(rows, sibs))

#data_model = {"boat": None, "rating": None}
#print(data)

#data_model["boat"] = data['boat']
#data_model['rating'] = data['rating']

#print(data_model)