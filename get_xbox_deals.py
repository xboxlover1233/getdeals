import requests
from bs4 import BeautifulSoup

cookies = dict(xnv2_currency_country='RU')

xbox_url = 'https://www.xbox-now.com/en/deal-list'
html_text = requests.get(xbox_url, cookies=cookies).text
soup = BeautifulSoup(html_text, 'html.parser')

games = soup.find_all('div', class_='box-body comparison-table-entry')

for game in games:
	link = game.find('a', href=True)
	
	local_price = game.find_all('span', {'style' : 'white-space: nowrap'})
	flags = game.find_all('img', {'style' : 'margin-bottom: 2px;'})
	if ('RUB' in local_price[3].text):
		price = int(float(local_price[3].text.partition(' ')[0].replace(',','')))

		if (price > 10 and price < 100):
			price = price + 80
		elif (price > 100 and price < 500):
			price = price + 85
		elif (price > 500 and price < 1000):
			price = price + 90
		elif (price > 1000 and price < 2000):
			price = price + 95
		elif (price > 2000 and price < 3000):
			price = price + 100
		elif (price > 3000 and price < 4000):
			price = price + 110
		elif (price > 4000 and price < 5000):
			price = price + 115
		elif (price > 5000 and price < 6000):
			price = price + 120
		# elif (price > 9999 && < 99999):
			# price = price + 99999
		print(link['title'] + ' - ' + str(price) + '₽ ' + flags[1]['alt'])
