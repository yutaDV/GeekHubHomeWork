"""HT 14 TASK  #2.  Створіть програму для отримання курсу валют за певний період.
- отримати від користувача дату (це може бути як один день так і інтервал - початкова
   і кінцева дати, продумайте механізм реалізації) і назву валюти
- вивести курс по відношенню до гривні на момент вказаної дати (або за кожен день у вказаному інтервалі)
- не забудьте перевірку на валідність введених даних"""

import json
import time
from datetime import datetime

import requests


class Currency:
	"""Клас пвертає курс вказаної валюти на вказану дату почитаючи з 01.01.2015р."""
	base_url = 'https://api.privatbank.ua/p24api/exchange_rates?json&date='

	def __init__(self, date, currency):
		self.date = date
		self.currency = currency

	def get_currency(self):
		"""Online request for exchange rates"""

		self.base_url = self.base_url + self.date
		page = requests.get(self.base_url).content
		all_information = json.loads(page)
		for kay, value in all_information.items():
			if kay == 'exchangeRate':
				return value

	def return_base(self, base):
		"""Searching for the desired currency returns a dictionary with data of the currency"""
		for element in base:
			for kay, value in element.items():
				if kay == 'currency' and value == self.currency:
					return element

	def return_result(self, element):
		"""Searching for the desired currency returns a dictionary with data of the currency"""

		result = f'\n Курси валют саном на {self.date} для {self.currency}.\n'
		for kay, value in element.items():
			if kay == 'saleRateNB':
				result += f' Курс НБУ(продаж) - {value} грн.'
			if kay == 'purchaseRateNB':
				result += f' Курс НБУ(покупка) - {value} грн.:'
			if kay == 'saleRate':
				result += f'Комерційний курс(продаж) - {value} грн.'
			if kay == 'purchaseRate':
				result += f'Комерційний курс(покупка)  - {value} грн.'
		return result


def choices_currency():
	"""The fuction returns  and choices  a users currency"""

	menu = {
		'USD':	'долар США', 'EUR':	'євро',
		'CHF':	'швейцарський франк', 'GBP': 'британський фунт',
		'PLZ':	'польський злотий', 'SEK':	'шведська крона',
		'CAD':	'канадський долар'
	}
	print('\n Для обрання валюти вкажіть:')
	for key, value in menu.items():
		time.sleep(1)
		print(f'  {key} - {value}')
	while True:
		time.sleep(1)
		currency = input('\n Вкажіть валюту:')
		if currency in menu:
			return currency
		print('Упс, не коректно вказані дані, спробуйте ще раз')


def correct_date():
	"""Функція перевіряє чи коректно введено дату"""

	while True:
		date = input('Введіть дату у форматі дд.мм.рррр (приклад - 01.01.2016) не раніше 01.01.2015: \n')
		try:
			valid_date = datetime.strptime(date, '%m.%d.%Y')
			if not (datetime(2015, 1, 1) <= valid_date < datetime.now()):
				print('Не коректно введена дата спробуйте знову (не раніше 01.01.2015)')
		except ValueError:
			print('Не коректно введена дата спробуйте знову !')
		else:
			break
	return date


if __name__ == '__main__':
	while True:
		currency = choices_currency()
		break
	while True:
		date = correct_date()
		break
	course_start = Currency(date, currency)
	base = course_start.get_currency()
	element = course_start.return_base(base)
	print(course_start.return_result(element))
