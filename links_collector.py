from bs4 import BeautifulSoup
import requests

# r = requests.get('https://naturalmedicineclinic.herokuapp.com/admin')
# # r.status_code
# r.headers['content-type']
# print(r)
url = "https://github.com/faisalnazik" 
text = requests.get(url).text
soup = BeautifulSoup(text, "html5lib")
all_urls = [a['href']
for a in soup('a')
if a.has_attr('href')]
print(len(all_urls))# 91 for me, way too many
print(all_urls)