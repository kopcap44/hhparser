import requests
from bs4 import BeautifulSoup as bs 
import csv 

#url = input('enter url: ')
url = 'https://www.fl.ru/projects/'
#to avoid users only sites 
headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15',
'accept': '*/*'}
#doing a request to site
r = requests.get(url, headers = headers)
#here html code of the page
soup = bs(r.content, 'html.parser')
#parsing items with class equal b-post__link
items = soup.find('a', class_='b-post__link')
#creating a string 
last = ''

# you have to create file named fl.txt in current directory 
# reading data from this file. This is for tracking the new posts on site
# we store here the last vacansy id
with open('fl.txt') as f:
	for line in f:
		last = line 

# if stored id not equal last id on site that means that there are a new post
if items['name'] != last:
	print('Wake up u need to make money')
	print(items.get('href'))
	# writing new id in to the file 
	with open('fl.txt', 'w') as f:
		f.write(items['name'])
else:
	print('U have some time to relax, no new job was spoted')
