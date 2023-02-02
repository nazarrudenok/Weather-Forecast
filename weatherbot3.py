import telebot
from telebot import types
import requests
from bs4 import BeautifulSoup
from pyowm import OWM
from pyowm.utils.config import get_default_config

bot = telebot.TeleBot('5918833330:AAFb2nJUinsjWQqtY8AnI4SD2yY-_xWSQDE')
owm = OWM('81f28410dced88a2b071ac219fcde6c5')

owm = owm.weather_manager()

config_dict = get_default_config()
config_dict['language'] = 'ua'

@bot.message_handler(commands = ['start'])
def start(message):
	bot.send_message(message.chat.id, 'Вітаю! Обери місто у меню')

@bot.message_handler(commands = ['lviv_today'])
def lviv(message):
	observation = owm.weather_at_place('Lviv,UA')
	w = observation.weather
	status = w.detailed_status

	url = 'https://www.unian.ua/pogoda/85436-lviv'
	response = requests.get(url)
	bs = BeautifulSoup(response.text, 'html.parser')

	temp = bs.find('div', class_ = 'info-now__c')
	vidch_yak = bs.find(class_ = 'info-now__list').find_all('span')
	vidch_yak_number = bs.find(class_ = 'info-now__list').find_all('b')
	humidity = bs.find(class_ = 'info-now__list').find_all('span')
	humidity_number = bs.find(class_ = 'info-now__list').find_all('b')
	ymov_opadiv = bs.find(class_ = 'info-now__list').find_all('span')
	ymov_opadiv_number = bs.find(class_ = 'info-now__list').find_all('b')
	tisk = bs.find(class_ = 'info-now__list').find_all('span')
	tisk_number = bs.find(class_ = 'info-now__list').find_all('b')
	shv_vitru = bs.find(class_ = 'info-now__list').find_all('span')
	shv_vitru_number = bs.find(class_ = 'info-now__list').find_all('b')

	bot.send_message(message.chat.id, 'У Львові зараз: ' +
	status + '\n'
	'Температура повітря у місті сатновить: ' + temp.text + '\n' +
	vidch_yak[0].text + ' ' + vidch_yak_number[0].text + '\n' +
	humidity[3].text + ':' + ' ' + humidity_number[2].text + '\n' +
	ymov_opadiv[8].text + ' ' + vidch_yak_number[5].text + '\n' +
	tisk[4].text + ' ' + tisk_number[3].text + '\n' +
	shv_vitru[6].text + ' ' + shv_vitru_number[4].text
	)

@bot.message_handler(commands = ['kyiv_today'])
def kyiv(message):
	observation = owm.weather_at_place('Kyiv,UA')
	w = observation.weather
	status = w.detailed_status

	url = 'https://www.unian.ua/pogoda/85486-kijiv'
	response = requests.get(url)
	bs = BeautifulSoup(response.text, 'html.parser')

	temp = bs.find('div', class_ = 'info-now__c')
	vidch_yak = bs.find(class_ = 'info-now__list').find_all('span')
	vidch_yak_number = bs.find(class_ = 'info-now__list').find_all('b')
	humidity = bs.find(class_ = 'info-now__list').find_all('span')
	humidity_number = bs.find(class_ = 'info-now__list').find_all('b')
	ymov_opadiv = bs.find(class_ = 'info-now__list').find_all('span')
	ymov_opadiv_number = bs.find(class_ = 'info-now__list').find_all('b')
	tisk = bs.find(class_ = 'info-now__list').find_all('span')
	tisk_number = bs.find(class_ = 'info-now__list').find_all('b')
	shv_vitru = bs.find(class_ = 'info-now__list').find_all('span')
	shv_vitru_number = bs.find(class_ = 'info-now__list').find_all('b')

	bot.send_message(message.chat.id, 'У Києві зараз: ' +
	status + '\n'
	'Температура повітря у місті сатновить: ' + temp.text + '\n' +
	vidch_yak[0].text + ' ' + vidch_yak_number[0].text + '\n' +
	humidity[3].text + ':' + ' ' + humidity_number[2].text + '\n' +
	ymov_opadiv[8].text + ' ' + vidch_yak_number[5].text + '\n' +
	tisk[4].text + ' ' + tisk_number[3].text + '\n' +
	shv_vitru[6].text + ' ' + shv_vitru_number[4].text
	)

bot.polling(none_stop = True)