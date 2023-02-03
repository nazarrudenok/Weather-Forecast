import telebot
from telebot import types
import requests
from bs4 import BeautifulSoup

bot = telebot.TeleBot('5918833330:AAFb2nJUinsjWQqtY8AnI4SD2yY-_xWSQDE')

@bot.message_handler(commands = ['start'])
def start(message):
	bot.send_message(message.chat.id, 'Вітаю! Обери місто у меню')

@bot.message_handler(commands=['lviv'])
def lviv(message):
    url = 'https://www.unian.ua/pogoda/85436-lviv'
    response = requests.get(url)
    bs = BeautifulSoup(response.text, 'html.parser')

    status = bs.find('div', class_ = 'info-now__text')
    temp = bs.find('div', class_ = 'info-now__c')
    vidch_yak = bs.find(class_ = 'info-now__list').find_all('span')
    vidch_yak_number = bs.find(class_ = 'info-now__list').find_all('b')
    humidity = bs.find(class_ = 'info-now__list').find_all('span')
    humidity_number = bs.find(class_ = 'info-now__list').find_all('b')
    ymov_opadiv = bs.find(class_ = 'info-now__list').find_all('span')
    tisk = bs.find(class_ = 'info-now__list').find_all('span')
    tisk_number = bs.find(class_ = 'info-now__list').find_all('b')
    shv_vitru = bs.find(class_ = 'info-now__list').find_all('span')
    shv_vitru_number = bs.find(class_ = 'info-now__list').find_all('b')

    bot.send_message(message.chat.id, status.text + '\n'
	'Температура повітря у місті сатновить: ' + temp.text + '\n' +
	vidch_yak[0].text + ' ' + vidch_yak_number[0].text + '\n' +
	humidity[3].text + ':' + ' ' + humidity_number[2].text + '\n' +
	ymov_opadiv[8].text + ' ' + vidch_yak_number[5].text + '\n' +
	tisk[4].text + ' ' + tisk_number[3].text + '\n' +
	shv_vitru[6].text + ' ' + shv_vitru_number[4].text
	)

@bot.message_handler(commands=['kyiv'])
def kyiv(message):
    url = 'https://www.unian.ua/pogoda/85486-kijiv'
    response = requests.get(url)
    bs = BeautifulSoup(response.text, 'html.parser')

    status = bs.find('div', class_ = 'info-now__text')
    temp = bs.find('div', class_ = 'info-now__c')
    vidch_yak = bs.find(class_ = 'info-now__list').find_all('span')
    vidch_yak_number = bs.find(class_ = 'info-now__list').find_all('b')
    humidity = bs.find(class_ = 'info-now__list').find_all('span')
    humidity_number = bs.find(class_ = 'info-now__list').find_all('b')
    ymov_opadiv = bs.find(class_ = 'info-now__list').find_all('span')
    tisk = bs.find(class_ = 'info-now__list').find_all('span')
    tisk_number = bs.find(class_ = 'info-now__list').find_all('b')
    shv_vitru = bs.find(class_ = 'info-now__list').find_all('span')
    shv_vitru_number = bs.find(class_ = 'info-now__list').find_all('b')

    bot.send_message(message.chat.id, status.text + '\n' +
		'Температура повітря у місті сатновить: ' + temp.text + '\n' +
		vidch_yak[0].text + ' ' + vidch_yak_number[0].text + '\n' +
		humidity[3].text + ':' + ' ' + humidity_number[2].text + '\n' +
		ymov_opadiv[8].text + ' ' + vidch_yak_number[5].text + '\n' +
		tisk[4].text + ' ' + tisk_number[3].text + '\n' +
		shv_vitru[6].text + ' ' + shv_vitru_number[4].text
		)

@bot.message_handler(commands=['odesa'])
def odesa(message):
    url = 'https://www.unian.ua/pogoda/85432-odesa'
    response = requests.get(url)
    bs = BeautifulSoup(response.text, 'html.parser')

    status = bs.find('div', class_ = 'info-now__text')
    temp = bs.find('div', class_ = 'info-now__c')
    vidch_yak = bs.find(class_ = 'info-now__list').find_all('span')
    vidch_yak_number = bs.find(class_ = 'info-now__list').find_all('b')
    humidity = bs.find(class_ = 'info-now__list').find_all('span')
    humidity_number = bs.find(class_ = 'info-now__list').find_all('b')
    ymov_opadiv = bs.find(class_ = 'info-now__list').find_all('span')
    tisk = bs.find(class_ = 'info-now__list').find_all('span')
    tisk_number = bs.find(class_ = 'info-now__list').find_all('b')
    shv_vitru = bs.find(class_ = 'info-now__list').find_all('span')
    shv_vitru_number = bs.find(class_ = 'info-now__list').find_all('b')

    bot.send_message(message.chat.id, status.text + '\n' +
		'Температура повітря у місті сатновить: ' + temp.text + '\n' +
		vidch_yak[0].text + ' ' + vidch_yak_number[0].text + '\n' +
		humidity[3].text + ':' + ' ' + humidity_number[2].text + '\n' +
		ymov_opadiv[8].text + ' ' + vidch_yak_number[5].text + '\n' +
		tisk[4].text + ' ' + tisk_number[3].text + '\n' +
		shv_vitru[6].text + ' ' + shv_vitru_number[4].text
		)

@bot.message_handler(commands=['lutsk'])
def lutsk(message):
    url = 'https://www.unian.ua/pogoda/85462-luck'
    response = requests.get(url)
    bs = BeautifulSoup(response.text, 'html.parser')

    status = bs.find('div', class_ = 'info-now__text')
    temp = bs.find('div', class_ = 'info-now__c')
    vidch_yak = bs.find(class_ = 'info-now__list').find_all('span')
    vidch_yak_number = bs.find(class_ = 'info-now__list').find_all('b')
    humidity = bs.find(class_ = 'info-now__list').find_all('span')
    humidity_number = bs.find(class_ = 'info-now__list').find_all('b')
    ymov_opadiv = bs.find(class_ = 'info-now__list').find_all('span')
    tisk = bs.find(class_ = 'info-now__list').find_all('span')
    tisk_number = bs.find(class_ = 'info-now__list').find_all('b')
    shv_vitru = bs.find(class_ = 'info-now__list').find_all('span')
    shv_vitru_number = bs.find(class_ = 'info-now__list').find_all('b')

    bot.send_message(message.chat.id, status.text + '\n' +
		'Температура повітря у місті сатновить: ' + temp.text + '\n' +
		vidch_yak[0].text + ' ' + vidch_yak_number[0].text + '\n' +
		humidity[3].text + ':' + ' ' + humidity_number[2].text + '\n' +
		ymov_opadiv[8].text + ' ' + vidch_yak_number[5].text + '\n' +
		tisk[4].text + ' ' + tisk_number[3].text + '\n' +
		shv_vitru[6].text + ' ' + shv_vitru_number[4].text
		)

@bot.message_handler(commands=['rivne'])
def lutsk(message):
    url = 'https://www.unian.ua/pogoda/85485-rivne'
    response = requests.get(url)
    bs = BeautifulSoup(response.text, 'html.parser')

    status = bs.find('div', class_ = 'info-now__text')
    temp = bs.find('div', class_ = 'info-now__c')
    vidch_yak = bs.find(class_ = 'info-now__list').find_all('span')
    vidch_yak_number = bs.find(class_ = 'info-now__list').find_all('b')
    humidity = bs.find(class_ = 'info-now__list').find_all('span')
    humidity_number = bs.find(class_ = 'info-now__list').find_all('b')
    ymov_opadiv = bs.find(class_ = 'info-now__list').find_all('span')
    tisk = bs.find(class_ = 'info-now__list').find_all('span')
    tisk_number = bs.find(class_ = 'info-now__list').find_all('b')
    shv_vitru = bs.find(class_ = 'info-now__list').find_all('span')
    shv_vitru_number = bs.find(class_ = 'info-now__list').find_all('b')

    bot.send_message(message.chat.id, status.text + '\n' +
		'Температура повітря у місті сатновить: ' + temp.text + '\n' +
		vidch_yak[0].text + ' ' + vidch_yak_number[0].text + '\n' +
		humidity[3].text + ':' + ' ' + humidity_number[2].text + '\n' +
		ymov_opadiv[8].text + ' ' + vidch_yak_number[5].text + '\n' +
		tisk[4].text + ' ' + tisk_number[3].text + '\n' +
		shv_vitru[6].text + ' ' + shv_vitru_number[4].text
		)

@bot.message_handler(commands=['zhytomyr'])
def lutsk(message):
    url = 'https://www.unian.ua/pogoda/85468-zhitomir'
    response = requests.get(url)
    bs = BeautifulSoup(response.text, 'html.parser')

    status = bs.find('div', class_ = 'info-now__text')
    temp = bs.find('div', class_ = 'info-now__c')
    vidch_yak = bs.find(class_ = 'info-now__list').find_all('span')
    vidch_yak_number = bs.find(class_ = 'info-now__list').find_all('b')
    humidity = bs.find(class_ = 'info-now__list').find_all('span')
    humidity_number = bs.find(class_ = 'info-now__list').find_all('b')
    ymov_opadiv = bs.find(class_ = 'info-now__list').find_all('span')
    tisk = bs.find(class_ = 'info-now__list').find_all('span')
    tisk_number = bs.find(class_ = 'info-now__list').find_all('b')
    shv_vitru = bs.find(class_ = 'info-now__list').find_all('span')
    shv_vitru_number = bs.find(class_ = 'info-now__list').find_all('b')

    bot.send_message(message.chat.id, status.text + '\n' +
		'Температура повітря у місті сатновить: ' + temp.text + '\n' +
		vidch_yak[0].text + ' ' + vidch_yak_number[0].text + '\n' +
		humidity[3].text + ':' + ' ' + humidity_number[2].text + '\n' +
		ymov_opadiv[8].text + ' ' + vidch_yak_number[5].text + '\n' +
		tisk[4].text + ' ' + tisk_number[3].text + '\n' +
		shv_vitru[6].text + ' ' + shv_vitru_number[4].text
		)

@bot.message_handler(commands=['chernihiv'])
def lutsk(message):
    url = 'https://www.unian.ua/pogoda/85461-chernigiv'
    response = requests.get(url)
    bs = BeautifulSoup(response.text, 'html.parser')

    status = bs.find('div', class_ = 'info-now__text')
    temp = bs.find('div', class_ = 'info-now__c')
    vidch_yak = bs.find(class_ = 'info-now__list').find_all('span')
    vidch_yak_number = bs.find(class_ = 'info-now__list').find_all('b')
    humidity = bs.find(class_ = 'info-now__list').find_all('span')
    humidity_number = bs.find(class_ = 'info-now__list').find_all('b')
    ymov_opadiv = bs.find(class_ = 'info-now__list').find_all('span')
    tisk = bs.find(class_ = 'info-now__list').find_all('span')
    tisk_number = bs.find(class_ = 'info-now__list').find_all('b')
    shv_vitru = bs.find(class_ = 'info-now__list').find_all('span')
    shv_vitru_number = bs.find(class_ = 'info-now__list').find_all('b')

    bot.send_message(message.chat.id, status.text + '\n' +
		'Температура повітря у місті сатновить: ' + temp.text + '\n' +
		vidch_yak[0].text + ' ' + vidch_yak_number[0].text + '\n' +
		humidity[3].text + ':' + ' ' + humidity_number[2].text + '\n' +
		ymov_opadiv[8].text + ' ' + vidch_yak_number[5].text + '\n' +
		tisk[4].text + ' ' + tisk_number[3].text + '\n' +
		shv_vitru[6].text + ' ' + shv_vitru_number[4].text
		)

@bot.message_handler(commands=['sumy'])
def lutsk(message):
    url = 'https://www.unian.ua/pogoda/85492-sumi'
    response = requests.get(url)
    bs = BeautifulSoup(response.text, 'html.parser')

    status = bs.find('div', class_ = 'info-now__text')
    temp = bs.find('div', class_ = 'info-now__c')
    vidch_yak = bs.find(class_ = 'info-now__list').find_all('span')
    vidch_yak_number = bs.find(class_ = 'info-now__list').find_all('b')
    humidity = bs.find(class_ = 'info-now__list').find_all('span')
    humidity_number = bs.find(class_ = 'info-now__list').find_all('b')
    ymov_opadiv = bs.find(class_ = 'info-now__list').find_all('span')
    tisk = bs.find(class_ = 'info-now__list').find_all('span')
    tisk_number = bs.find(class_ = 'info-now__list').find_all('b')
    shv_vitru = bs.find(class_ = 'info-now__list').find_all('span')
    shv_vitru_number = bs.find(class_ = 'info-now__list').find_all('b')

    bot.send_message(message.chat.id, status.text + '\n' +
		'Температура повітря у місті сатновить: ' + temp.text + '\n' +
		vidch_yak[0].text + ' ' + vidch_yak_number[0].text + '\n' +
		humidity[3].text + ':' + ' ' + humidity_number[2].text + '\n' +
		ymov_opadiv[8].text + ' ' + vidch_yak_number[5].text + '\n' +
		tisk[4].text + ' ' + tisk_number[3].text + '\n' +
		shv_vitru[6].text + ' ' + shv_vitru_number[4].text
		)

@bot.message_handler(commands=['kharkiv'])
def lutsk(message):
    url = 'https://www.unian.ua/pogoda/85437-harkiv'
    response = requests.get(url)
    bs = BeautifulSoup(response.text, 'html.parser')

    status = bs.find('div', class_ = 'info-now__text')
    temp = bs.find('div', class_ = 'info-now__c')
    vidch_yak = bs.find(class_ = 'info-now__list').find_all('span')
    vidch_yak_number = bs.find(class_ = 'info-now__list').find_all('b')
    humidity = bs.find(class_ = 'info-now__list').find_all('span')
    humidity_number = bs.find(class_ = 'info-now__list').find_all('b')
    ymov_opadiv = bs.find(class_ = 'info-now__list').find_all('span')
    tisk = bs.find(class_ = 'info-now__list').find_all('span')
    tisk_number = bs.find(class_ = 'info-now__list').find_all('b')
    shv_vitru = bs.find(class_ = 'info-now__list').find_all('span')
    shv_vitru_number = bs.find(class_ = 'info-now__list').find_all('b')

    bot.send_message(message.chat.id, status.text + '\n' +
		'Температура повітря у місті сатновить: ' + temp.text + '\n' +
		vidch_yak[0].text + ' ' + vidch_yak_number[0].text + '\n' +
		humidity[3].text + ':' + ' ' + humidity_number[2].text + '\n' +
		ymov_opadiv[8].text + ' ' + vidch_yak_number[5].text + '\n' +
		tisk[4].text + ' ' + tisk_number[3].text + '\n' +
		shv_vitru[6].text + ' ' + shv_vitru_number[4].text
		)

@bot.message_handler(commands=['lugansk'])
def lutsk(message):
    url = 'https://www.unian.ua/pogoda/85464-lugansk'
    response = requests.get(url)
    bs = BeautifulSoup(response.text, 'html.parser')

    status = bs.find('div', class_ = 'info-now__text')
    temp = bs.find('div', class_ = 'info-now__c')
    vidch_yak = bs.find(class_ = 'info-now__list').find_all('span')
    vidch_yak_number = bs.find(class_ = 'info-now__list').find_all('b')
    humidity = bs.find(class_ = 'info-now__list').find_all('span')
    humidity_number = bs.find(class_ = 'info-now__list').find_all('b')
    ymov_opadiv = bs.find(class_ = 'info-now__list').find_all('span')
    tisk = bs.find(class_ = 'info-now__list').find_all('span')
    tisk_number = bs.find(class_ = 'info-now__list').find_all('b')
    shv_vitru = bs.find(class_ = 'info-now__list').find_all('span')
    shv_vitru_number = bs.find(class_ = 'info-now__list').find_all('b')

    bot.send_message(message.chat.id, status.text + '\n' +
		'Температура повітря у місті сатновить: ' + temp.text + '\n' +
		vidch_yak[0].text + ' ' + vidch_yak_number[0].text + '\n' +
		humidity[3].text + ':' + ' ' + humidity_number[2].text + '\n' +
		ymov_opadiv[8].text + ' ' + vidch_yak_number[5].text + '\n' +
		tisk[4].text + ' ' + tisk_number[3].text + '\n' +
		shv_vitru[6].text + ' ' + shv_vitru_number[4].text
		)

@bot.message_handler(commands=['donetsk'])
def lutsk(message):
    url = 'https://www.unian.ua/pogoda/85441-doneck'
    response = requests.get(url)
    bs = BeautifulSoup(response.text, 'html.parser')

    status = bs.find('div', class_ = 'info-now__text')
    temp = bs.find('div', class_ = 'info-now__c')
    vidch_yak = bs.find(class_ = 'info-now__list').find_all('span')
    vidch_yak_number = bs.find(class_ = 'info-now__list').find_all('b')
    humidity = bs.find(class_ = 'info-now__list').find_all('span')
    humidity_number = bs.find(class_ = 'info-now__list').find_all('b')
    ymov_opadiv = bs.find(class_ = 'info-now__list').find_all('span')
    tisk = bs.find(class_ = 'info-now__list').find_all('span')
    tisk_number = bs.find(class_ = 'info-now__list').find_all('b')
    shv_vitru = bs.find(class_ = 'info-now__list').find_all('span')
    shv_vitru_number = bs.find(class_ = 'info-now__list').find_all('b')

    bot.send_message(message.chat.id, status.text + '\n' +
		'Температура повітря у місті сатновить: ' + temp.text + '\n' +
		vidch_yak[0].text + ' ' + vidch_yak_number[0].text + '\n' +
		humidity[3].text + ':' + ' ' + humidity_number[2].text + '\n' +
		ymov_opadiv[8].text + ' ' + vidch_yak_number[5].text + '\n' +
		tisk[4].text + ' ' + tisk_number[3].text + '\n' +
		shv_vitru[6].text + ' ' + shv_vitru_number[4].text
		)

@bot.message_handler(commands=['dnipro'])
def lutsk(message):
    url = 'https://www.unian.ua/pogoda/85440-dnipro'
    response = requests.get(url)
    bs = BeautifulSoup(response.text, 'html.parser')

    status = bs.find('div', class_ = 'info-now__text')
    temp = bs.find('div', class_ = 'info-now__c')
    vidch_yak = bs.find(class_ = 'info-now__list').find_all('span')
    vidch_yak_number = bs.find(class_ = 'info-now__list').find_all('b')
    humidity = bs.find(class_ = 'info-now__list').find_all('span')
    humidity_number = bs.find(class_ = 'info-now__list').find_all('b')
    ymov_opadiv = bs.find(class_ = 'info-now__list').find_all('span')
    tisk = bs.find(class_ = 'info-now__list').find_all('span')
    tisk_number = bs.find(class_ = 'info-now__list').find_all('b')
    shv_vitru = bs.find(class_ = 'info-now__list').find_all('span')
    shv_vitru_number = bs.find(class_ = 'info-now__list').find_all('b')

    bot.send_message(message.chat.id, status.text + '\n' +
		'Температура повітря у місті сатновить: ' + temp.text + '\n' +
		vidch_yak[0].text + ' ' + vidch_yak_number[0].text + '\n' +
		humidity[3].text + ':' + ' ' + humidity_number[2].text + '\n' +
		ymov_opadiv[8].text + ' ' + vidch_yak_number[5].text + '\n' +
		tisk[4].text + ' ' + tisk_number[3].text + '\n' +
		shv_vitru[6].text + ' ' + shv_vitru_number[4].text
		)

@bot.message_handler(commands=['poltava'])
def lutsk(message):
    url = 'https://www.unian.ua/pogoda/85451-poltava'
    response = requests.get(url)
    bs = BeautifulSoup(response.text, 'html.parser')

    status = bs.find('div', class_ = 'info-now__text')
    temp = bs.find('div', class_ = 'info-now__c')
    vidch_yak = bs.find(class_ = 'info-now__list').find_all('span')
    vidch_yak_number = bs.find(class_ = 'info-now__list').find_all('b')
    humidity = bs.find(class_ = 'info-now__list').find_all('span')
    humidity_number = bs.find(class_ = 'info-now__list').find_all('b')
    ymov_opadiv = bs.find(class_ = 'info-now__list').find_all('span')
    tisk = bs.find(class_ = 'info-now__list').find_all('span')
    tisk_number = bs.find(class_ = 'info-now__list').find_all('b')
    shv_vitru = bs.find(class_ = 'info-now__list').find_all('span')
    shv_vitru_number = bs.find(class_ = 'info-now__list').find_all('b')

    bot.send_message(message.chat.id, status.text + '\n' +
		'Температура повітря у місті сатновить: ' + temp.text + '\n' +
		vidch_yak[0].text + ' ' + vidch_yak_number[0].text + '\n' +
		humidity[3].text + ':' + ' ' + humidity_number[2].text + '\n' +
		ymov_opadiv[8].text + ' ' + vidch_yak_number[5].text + '\n' +
		tisk[4].text + ' ' + tisk_number[3].text + '\n' +
		shv_vitru[6].text + ' ' + shv_vitru_number[4].text
		)

@bot.message_handler(commands=['zaporizhzhia'])
def lutsk(message):
    url = 'https://www.unian.ua/pogoda/85455-zaporizhzhya'
    response = requests.get(url)
    bs = BeautifulSoup(response.text, 'html.parser')

    status = bs.find('div', class_ = 'info-now__text')
    temp = bs.find('div', class_ = 'info-now__c')
    vidch_yak = bs.find(class_ = 'info-now__list').find_all('span')
    vidch_yak_number = bs.find(class_ = 'info-now__list').find_all('b')
    humidity = bs.find(class_ = 'info-now__list').find_all('span')
    humidity_number = bs.find(class_ = 'info-now__list').find_all('b')
    ymov_opadiv = bs.find(class_ = 'info-now__list').find_all('span')
    tisk = bs.find(class_ = 'info-now__list').find_all('span')
    tisk_number = bs.find(class_ = 'info-now__list').find_all('b')
    shv_vitru = bs.find(class_ = 'info-now__list').find_all('span')
    shv_vitru_number = bs.find(class_ = 'info-now__list').find_all('b')

    bot.send_message(message.chat.id, status.text + '\n' +
		'Температура повітря у місті сатновить: ' + temp.text + '\n' +
		vidch_yak[0].text + ' ' + vidch_yak_number[0].text + '\n' +
		humidity[3].text + ':' + ' ' + humidity_number[2].text + '\n' +
		ymov_opadiv[8].text + ' ' + vidch_yak_number[5].text + '\n' +
		tisk[4].text + ' ' + tisk_number[3].text + '\n' +
		shv_vitru[6].text + ' ' + shv_vitru_number[4].text
		)

@bot.message_handler(commands=['kherson'])
def lutsk(message):
    url = 'https://www.unian.ua/pogoda/85465-herson'
    response = requests.get(url)
    bs = BeautifulSoup(response.text, 'html.parser')

    status = bs.find('div', class_ = 'info-now__text')
    temp = bs.find('div', class_ = 'info-now__c')
    vidch_yak = bs.find(class_ = 'info-now__list').find_all('span')
    vidch_yak_number = bs.find(class_ = 'info-now__list').find_all('b')
    humidity = bs.find(class_ = 'info-now__list').find_all('span')
    humidity_number = bs.find(class_ = 'info-now__list').find_all('b')
    ymov_opadiv = bs.find(class_ = 'info-now__list').find_all('span')
    tisk = bs.find(class_ = 'info-now__list').find_all('span')
    tisk_number = bs.find(class_ = 'info-now__list').find_all('b')
    shv_vitru = bs.find(class_ = 'info-now__list').find_all('span')
    shv_vitru_number = bs.find(class_ = 'info-now__list').find_all('b')

    bot.send_message(message.chat.id, status.text + '\n' +
		'Температура повітря у місті сатновить: ' + temp.text + '\n' +
		vidch_yak[0].text + ' ' + vidch_yak_number[0].text + '\n' +
		humidity[3].text + ':' + ' ' + humidity_number[2].text + '\n' +
		ymov_opadiv[8].text + ' ' + vidch_yak_number[5].text + '\n' +
		tisk[4].text + ' ' + tisk_number[3].text + '\n' +
		shv_vitru[6].text + ' ' + shv_vitru_number[4].text
		)

@bot.message_handler(commands=['mykolaiv'])
def lutsk(message):
    url = 'https://www.unian.ua/pogoda/85493-mikolajiv'
    response = requests.get(url)
    bs = BeautifulSoup(response.text, 'html.parser')

    status = bs.find('div', class_ = 'info-now__text')
    temp = bs.find('div', class_ = 'info-now__c')
    vidch_yak = bs.find(class_ = 'info-now__list').find_all('span')
    vidch_yak_number = bs.find(class_ = 'info-now__list').find_all('b')
    humidity = bs.find(class_ = 'info-now__list').find_all('span')
    humidity_number = bs.find(class_ = 'info-now__list').find_all('b')
    ymov_opadiv = bs.find(class_ = 'info-now__list').find_all('span')
    tisk = bs.find(class_ = 'info-now__list').find_all('span')
    tisk_number = bs.find(class_ = 'info-now__list').find_all('b')
    shv_vitru = bs.find(class_ = 'info-now__list').find_all('span')
    shv_vitru_number = bs.find(class_ = 'info-now__list').find_all('b')

    bot.send_message(message.chat.id, status.text + '\n' +
		'Температура повітря у місті сатновить: ' + temp.text + '\n' +
		vidch_yak[0].text + ' ' + vidch_yak_number[0].text + '\n' +
		humidity[3].text + ':' + ' ' + humidity_number[2].text + '\n' +
		ymov_opadiv[8].text + ' ' + vidch_yak_number[5].text + '\n' +
		tisk[4].text + ' ' + tisk_number[3].text + '\n' +
		shv_vitru[6].text + ' ' + shv_vitru_number[4].text
		)

@bot.message_handler(commands=['kropyvnytskyi'])
def lutsk(message):
    url = 'https://www.unian.ua/pogoda/85502-kropivnickiy'
    response = requests.get(url)
    bs = BeautifulSoup(response.text, 'html.parser')

    status = bs.find('div', class_ = 'info-now__text')
    temp = bs.find('div', class_ = 'info-now__c')
    vidch_yak = bs.find(class_ = 'info-now__list').find_all('span')
    vidch_yak_number = bs.find(class_ = 'info-now__list').find_all('b')
    humidity = bs.find(class_ = 'info-now__list').find_all('span')
    humidity_number = bs.find(class_ = 'info-now__list').find_all('b')
    ymov_opadiv = bs.find(class_ = 'info-now__list').find_all('span')
    tisk = bs.find(class_ = 'info-now__list').find_all('span')
    tisk_number = bs.find(class_ = 'info-now__list').find_all('b')
    shv_vitru = bs.find(class_ = 'info-now__list').find_all('span')
    shv_vitru_number = bs.find(class_ = 'info-now__list').find_all('b')

    bot.send_message(message.chat.id, status.text + '\n' +
		'Температура повітря у місті сатновить: ' + temp.text + '\n' +
		vidch_yak[0].text + ' ' + vidch_yak_number[0].text + '\n' +
		humidity[3].text + ':' + ' ' + humidity_number[2].text + '\n' +
		ymov_opadiv[8].text + ' ' + vidch_yak_number[5].text + '\n' +
		tisk[4].text + ' ' + tisk_number[3].text + '\n' +
		shv_vitru[6].text + ' ' + shv_vitru_number[4].text
		)

@bot.message_handler(commands=['cherkasy'])
def lutsk(message):
    url = 'https://www.unian.ua/pogoda/85474-cherkasi'
    response = requests.get(url)
    bs = BeautifulSoup(response.text, 'html.parser')

    status = bs.find('div', class_ = 'info-now__text')
    temp = bs.find('div', class_ = 'info-now__c')
    vidch_yak = bs.find(class_ = 'info-now__list').find_all('span')
    vidch_yak_number = bs.find(class_ = 'info-now__list').find_all('b')
    humidity = bs.find(class_ = 'info-now__list').find_all('span')
    humidity_number = bs.find(class_ = 'info-now__list').find_all('b')
    ymov_opadiv = bs.find(class_ = 'info-now__list').find_all('span')
    tisk = bs.find(class_ = 'info-now__list').find_all('span')
    tisk_number = bs.find(class_ = 'info-now__list').find_all('b')
    shv_vitru = bs.find(class_ = 'info-now__list').find_all('span')
    shv_vitru_number = bs.find(class_ = 'info-now__list').find_all('b')

    bot.send_message(message.chat.id, status.text + '\n' +
		'Температура повітря у місті сатновить: ' + temp.text + '\n' +
		vidch_yak[0].text + ' ' + vidch_yak_number[0].text + '\n' +
		humidity[3].text + ':' + ' ' + humidity_number[2].text + '\n' +
		ymov_opadiv[8].text + ' ' + vidch_yak_number[5].text + '\n' +
		tisk[4].text + ' ' + tisk_number[3].text + '\n' +
		shv_vitru[6].text + ' ' + shv_vitru_number[4].text
		)

@bot.message_handler(commands=['vinnytsia'])
def lutsk(message):
    url = 'https://www.unian.ua/pogoda/85484-vinnicya'
    response = requests.get(url)
    bs = BeautifulSoup(response.text, 'html.parser')

    status = bs.find('div', class_ = 'info-now__text')
    temp = bs.find('div', class_ = 'info-now__c')
    vidch_yak = bs.find(class_ = 'info-now__list').find_all('span')
    vidch_yak_number = bs.find(class_ = 'info-now__list').find_all('b')
    humidity = bs.find(class_ = 'info-now__list').find_all('span')
    humidity_number = bs.find(class_ = 'info-now__list').find_all('b')
    ymov_opadiv = bs.find(class_ = 'info-now__list').find_all('span')
    tisk = bs.find(class_ = 'info-now__list').find_all('span')
    tisk_number = bs.find(class_ = 'info-now__list').find_all('b')
    shv_vitru = bs.find(class_ = 'info-now__list').find_all('span')
    shv_vitru_number = bs.find(class_ = 'info-now__list').find_all('b')

    bot.send_message(message.chat.id, status.text + '\n' +
		'Температура повітря у місті сатновить: ' + temp.text + '\n' +
		vidch_yak[0].text + ' ' + vidch_yak_number[0].text + '\n' +
		humidity[3].text + ':' + ' ' + humidity_number[2].text + '\n' +
		ymov_opadiv[8].text + ' ' + vidch_yak_number[5].text + '\n' +
		tisk[4].text + ' ' + tisk_number[3].text + '\n' +
		shv_vitru[6].text + ' ' + shv_vitru_number[4].text
		)

@bot.message_handler(commands=['khmelnytskyi'])
def lutsk(message):
    url = 'https://www.unian.ua/pogoda/85717-hmelnickiy'
    response = requests.get(url)
    bs = BeautifulSoup(response.text, 'html.parser')

    status = bs.find('div', class_ = 'info-now__text')
    temp = bs.find('div', class_ = 'info-now__c')
    vidch_yak = bs.find(class_ = 'info-now__list').find_all('span')
    vidch_yak_number = bs.find(class_ = 'info-now__list').find_all('b')
    humidity = bs.find(class_ = 'info-now__list').find_all('span')
    humidity_number = bs.find(class_ = 'info-now__list').find_all('b')
    ymov_opadiv = bs.find(class_ = 'info-now__list').find_all('span')
    tisk = bs.find(class_ = 'info-now__list').find_all('span')
    tisk_number = bs.find(class_ = 'info-now__list').find_all('b')
    shv_vitru = bs.find(class_ = 'info-now__list').find_all('span')
    shv_vitru_number = bs.find(class_ = 'info-now__list').find_all('b')

    bot.send_message(message.chat.id, status.text + '\n' +
		'Температура повітря у місті сатновить: ' + temp.text + '\n' +
		vidch_yak[0].text + ' ' + vidch_yak_number[0].text + '\n' +
		humidity[3].text + ':' + ' ' + humidity_number[2].text + '\n' +
		ymov_opadiv[8].text + ' ' + vidch_yak_number[5].text + '\n' +
		tisk[4].text + ' ' + tisk_number[3].text + '\n' +
		shv_vitru[6].text + ' ' + shv_vitru_number[4].text
		)

@bot.message_handler(commands=['ternopil'])
def lutsk(message):
    url = 'https://www.unian.ua/pogoda/85467-ternopil'
    response = requests.get(url)
    bs = BeautifulSoup(response.text, 'html.parser')

    status = bs.find('div', class_ = 'info-now__text')
    temp = bs.find('div', class_ = 'info-now__c')
    vidch_yak = bs.find(class_ = 'info-now__list').find_all('span')
    vidch_yak_number = bs.find(class_ = 'info-now__list').find_all('b')
    humidity = bs.find(class_ = 'info-now__list').find_all('span')
    humidity_number = bs.find(class_ = 'info-now__list').find_all('b')
    ymov_opadiv = bs.find(class_ = 'info-now__list').find_all('span')
    tisk = bs.find(class_ = 'info-now__list').find_all('span')
    tisk_number = bs.find(class_ = 'info-now__list').find_all('b')
    shv_vitru = bs.find(class_ = 'info-now__list').find_all('span')
    shv_vitru_number = bs.find(class_ = 'info-now__list').find_all('b')

    bot.send_message(message.chat.id, status.text + '\n' +
		'Температура повітря у місті сатновить: ' + temp.text + '\n' +
		vidch_yak[0].text + ' ' + vidch_yak_number[0].text + '\n' +
		humidity[3].text + ':' + ' ' + humidity_number[2].text + '\n' +
		ymov_opadiv[8].text + ' ' + vidch_yak_number[5].text + '\n' +
		tisk[4].text + ' ' + tisk_number[3].text + '\n' +
		shv_vitru[6].text + ' ' + shv_vitru_number[4].text
		)

@bot.message_handler(commands=['chernivtsi'])
def lutsk(message):
    url = 'https://www.unian.ua/pogoda/85434-chernivci'
    response = requests.get(url)
    bs = BeautifulSoup(response.text, 'html.parser')

    status = bs.find('div', class_ = 'info-now__text')
    temp = bs.find('div', class_ = 'info-now__c')
    vidch_yak = bs.find(class_ = 'info-now__list').find_all('span')
    vidch_yak_number = bs.find(class_ = 'info-now__list').find_all('b')
    humidity = bs.find(class_ = 'info-now__list').find_all('span')
    humidity_number = bs.find(class_ = 'info-now__list').find_all('b')
    ymov_opadiv = bs.find(class_ = 'info-now__list').find_all('span')
    tisk = bs.find(class_ = 'info-now__list').find_all('span')
    tisk_number = bs.find(class_ = 'info-now__list').find_all('b')
    shv_vitru = bs.find(class_ = 'info-now__list').find_all('span')
    shv_vitru_number = bs.find(class_ = 'info-now__list').find_all('b')

    bot.send_message(message.chat.id, status.text + '\n' +
		'Температура повітря у місті сатновить: ' + temp.text + '\n' +
		vidch_yak[0].text + ' ' + vidch_yak_number[0].text + '\n' +
		humidity[3].text + ':' + ' ' + humidity_number[2].text + '\n' +
		ymov_opadiv[8].text + ' ' + vidch_yak_number[5].text + '\n' +
		tisk[4].text + ' ' + tisk_number[3].text + '\n' +
		shv_vitru[6].text + ' ' + shv_vitru_number[4].text
		)

@bot.message_handler(commands=['ivano_frankivsk'])
def lutsk(message):
    url = 'https://www.unian.ua/pogoda/85430-ivano-frankivsk'
    response = requests.get(url)
    bs = BeautifulSoup(response.text, 'html.parser')

    status = bs.find('div', class_ = 'info-now__text')
    temp = bs.find('div', class_ = 'info-now__c')
    vidch_yak = bs.find(class_ = 'info-now__list').find_all('span')
    vidch_yak_number = bs.find(class_ = 'info-now__list').find_all('b')
    humidity = bs.find(class_ = 'info-now__list').find_all('span')
    humidity_number = bs.find(class_ = 'info-now__list').find_all('b')
    ymov_opadiv = bs.find(class_ = 'info-now__list').find_all('span')
    tisk = bs.find(class_ = 'info-now__list').find_all('span')
    tisk_number = bs.find(class_ = 'info-now__list').find_all('b')
    shv_vitru = bs.find(class_ = 'info-now__list').find_all('span')
    shv_vitru_number = bs.find(class_ = 'info-now__list').find_all('b')

    bot.send_message(message.chat.id, status.text + '\n' +
		'Температура повітря у місті сатновить: ' + temp.text + '\n' +
		vidch_yak[0].text + ' ' + vidch_yak_number[0].text + '\n' +
		humidity[3].text + ':' + ' ' + humidity_number[2].text + '\n' +
		ymov_opadiv[8].text + ' ' + vidch_yak_number[5].text + '\n' +
		tisk[4].text + ' ' + tisk_number[3].text + '\n' +
		shv_vitru[6].text + ' ' + shv_vitru_number[4].text
		)

@bot.message_handler(commands=['uzhhorod'])
def lutsk(message):
    url = 'https://www.unian.ua/pogoda/85466-uzhgorod'
    response = requests.get(url)
    bs = BeautifulSoup(response.text, 'html.parser')

    status = bs.find('div', class_ = 'info-now__text')
    temp = bs.find('div', class_ = 'info-now__c')
    vidch_yak = bs.find(class_ = 'info-now__list').find_all('span')
    vidch_yak_number = bs.find(class_ = 'info-now__list').find_all('b')
    humidity = bs.find(class_ = 'info-now__list').find_all('span')
    humidity_number = bs.find(class_ = 'info-now__list').find_all('b')
    ymov_opadiv = bs.find(class_ = 'info-now__list').find_all('span')
    tisk = bs.find(class_ = 'info-now__list').find_all('span')
    tisk_number = bs.find(class_ = 'info-now__list').find_all('b')
    shv_vitru = bs.find(class_ = 'info-now__list').find_all('span')
    shv_vitru_number = bs.find(class_ = 'info-now__list').find_all('b')

    bot.send_message(message.chat.id, status.text + '\n' +
		'Температура повітря у місті сатновить: ' + temp.text + '\n' +
		vidch_yak[0].text + ' ' + vidch_yak_number[0].text + '\n' +
		humidity[3].text + ':' + ' ' + humidity_number[2].text + '\n' +
		ymov_opadiv[8].text + ' ' + vidch_yak_number[5].text + '\n' +
		tisk[4].text + ' ' + tisk_number[3].text + '\n' +
		shv_vitru[6].text + ' ' + shv_vitru_number[4].text
		)

@bot.message_handler(commands=['simferopol'])
def lutsk(message):
    url = 'https://www.unian.ua/pogoda/111221-simferopol'
    response = requests.get(url)
    bs = BeautifulSoup(response.text, 'html.parser')

    status = bs.find('div', class_ = 'info-now__text')
    temp = bs.find('div', class_ = 'info-now__c')
    vidch_yak = bs.find(class_ = 'info-now__list').find_all('span')
    vidch_yak_number = bs.find(class_ = 'info-now__list').find_all('b')
    humidity = bs.find(class_ = 'info-now__list').find_all('span')
    humidity_number = bs.find(class_ = 'info-now__list').find_all('b')
    ymov_opadiv = bs.find(class_ = 'info-now__list').find_all('span')
    tisk = bs.find(class_ = 'info-now__list').find_all('span')
    tisk_number = bs.find(class_ = 'info-now__list').find_all('b')
    shv_vitru = bs.find(class_ = 'info-now__list').find_all('span')
    shv_vitru_number = bs.find(class_ = 'info-now__list').find_all('b')

    bot.send_message(message.chat.id, status.text + '\n' +
		'Температура повітря у місті сатновить: ' + temp.text + '\n' +
		vidch_yak[0].text + ' ' + vidch_yak_number[0].text + '\n' +
		humidity[3].text + ':' + ' ' + humidity_number[2].text + '\n' +
		ymov_opadiv[8].text + ' ' + vidch_yak_number[5].text + '\n' +
		tisk[4].text + ' ' + tisk_number[3].text + '\n' +
		shv_vitru[6].text + ' ' + shv_vitru_number[4].text
		)

bot.polling(non_stop=True)
