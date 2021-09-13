from bs4 import BeautifulSoup
import requests
import re
# Importing pandas as pd
import pandas as pd

df = pd.DataFrame()

url = "https://www.house.gov/representatives" 
text = requests.get(url).text
soup = BeautifulSoup(text, "html5lib")
all_urls = [a['href']
for a in soup('a')
if a.has_attr('href')]

# Must start with http:// or https://
# Must end with .house.gov or .house.gov/
regex = r"^https?://.*\.house\.gov/?$"

# Let's write some tests!
assert re.match(regex, "http://joel.house.gov")
assert re.match(regex, "https://joel.house.gov")
assert re.match(regex, "http://joel.house.gov/")
assert re.match(regex, "https://joel.house.gov/")
assert not re.match(regex, "joel.house.gov")
assert not re.match(regex, "http://joel.house.com")
assert not re.match(regex, "https://joel.house.gov/biography")


# And now apply
good_urls = [url for url in all_urls if re.match(regex, url)]

good_urls = list(set(good_urls))
print(len(all_urls)) #967 total 
# print(all_urls)
print(len(good_urls)) #437 for me the good one
# print(good_urls)

# Creating two columns
df['links'] = good_urls[0::1]
# Converting to excel
df.to_excel('result.xlsx', index = True)
