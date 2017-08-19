import requests
from BeautifulSoup import BeautifulSoup
import re
import csv

csv_file = open('ranking_university_USnews.csv', 'wb', buffering=0)
writer = csv.writer(csv_file)

url = "https://www.usnews.com/best-graduate-schools/search?sort=rank_sort&sortdir=asc&program=top-computer-science-schools&page="

cookie = {}


records = []
ranks1 = []
names = []
locations = []
# for url in urls:
url = url + str(1)
print url
r = requests.get(url)
print r
soup = BeautifulSoup(r.text)
for rank in soup.findAll('span', attrs={'class': 'rankscore-bronze cluetip cluetip-stylized'}):
    ranks1.append(int(re.findall('\d+', rank.text)[0]))
for college in soup.findAll('a', attrs={'class': 'school-name'}):
    names.append(college.text)
for location in soup.findAll('p', attrs={'class': 'location'}):
    locations.append(location.text)

# print len(ranks), len(names), len(locations)
ranks2 = range(203, 281)
ranks = ranks1+list(ranks2)

print(ranks1)


# # print ranks
# for i in range(len(ranks)):
#     records.append(i+1)
#     records.append(ranks[i])
#     records.append(names[i].encode('utf-8'))
#     records.append(locations[i])
#     writer.writerow(records)
#     records = []