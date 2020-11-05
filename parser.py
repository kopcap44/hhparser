import requests
from bs4 import BeautifulSoup as bs 
import csv 

#url = input('enter url: ')
url = 'https://hh.ru/search/vacancy?clusters=true&area=1&enable_snippets=true&salary=&st=searchVacancy&text=Python+junior&from=suggest_post'
headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15',
'accept': '*/*'}
pure_html = 'https://hh.ru' 
FILE = 'jobs.csv'



def get_html(url, params=None):
	r = requests.get(url, headers = headers, params = params)
	return r


def pag_count(html):
	#r1 = get_html(url)
	soup = bs(html, 'html.parser')
	pagination = soup.find_all('a', class_ = 'bloko-button HH-Pager-Control')
	if pagination:
		return int(pagination[-1].getText())
	else:
		return 0


def get_content(html):
	soup = bs(html, 'html.parser')
	items = soup.find_all('div', class_ = 'vacancy-serp-item')
	jobs = []
	for item in items:
		salary = item.find('span', attrs = {'class': 'bloko-section-header-3 bloko-section-header-3_lite' , 'data-qa': "vacancy-serp__vacancy-compensation"})
		if salary:
			salary = salary.getText()
		else:
			salary = 'Ask for salary'


		jobs.append({
			'Name': item.find('a', attrs={'class':'bloko-link HH-LinkModifier'}).getText(),
			'Link': item.find('a', attrs={'class':'bloko-link HH-LinkModifier'})['href'],
			'Salary': salary
			})
		#print(link.getText() + ' | ' + link['href'] + '\n')
	return jobs


def save_file(items, path):
	with open(path, 'w', newline = '') as file:
		writer = csv.writer(file, delimiter = ';')
		writer.writerow(['Name', 'Link', 'Salary'])
		for item in items:
			writer.writerow([item['Name'], item['Link'], item['Salary']])



def parse():
	url  = input('Link from hh.ru: ')
	html = get_html(url)
	pages_count = pag_count(html.text)
	jobs = []
	for page in range(0, pages_count + 1):
		print(f'Парсинг страницы {page} из {pages_count}...')
		#href = get_html(pure_html + link['href'])
		html = get_html(url, params={'page': page})
		jobs.extend(get_content(html.text))
	save_file(jobs, FILE)
	print(f'Получено {len(jobs)} предложений')


parse()


