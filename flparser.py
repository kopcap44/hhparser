import requests
from bs4 import BeautifulSoup as bs 
import csv 

#url = input('enter url: ')
url = 'https://www.fl.ru/projects/'
headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15',
'accept': '*/*'}

FILE = 'vacansy.csv'



r = requests.get(url, headers = headers)

soup = bs(r.content, 'html.parser')
items = soup.find('a', class_='b-post__link')

last = ''

with open('fl.txt') as f:
	for line in f:
		last = line 


if items['name'] != last:
	print('Wake up u need to make money')
	print(items.get('href'))
	with open('fl.txt', 'w') as f:
		f.write(items['name'])
else:
	print('U have some time to relax, no new job was spoted')
