# -*- coding: utf-8 -*-
from time import sleep

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec


class GMailPage(BasePage):
	"""
	Класс для страницы gmail, который содержит основные функции для тестов
	"""
	def login(self, mail: str, password: str):
		"""
		Функция, котороая логинится на "временном" сайте (в данном случае) stackoverflow.com
		:param mail:
		:param password:
		:return:
		"""
		self.go_to_site(
			'https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2fusers%2fstory%2fcurrent%27')
		self.click_on_element(By.CLASS_NAME, 's-btn__google')
		self.input_data(By.NAME, 'identifier', mail)
		self.click_on_element(By.ID, 'identifierNext')
		self.input_data(By.NAME, 'password', password)
		self.click_on_element(By.ID, 'passwordNext')
		self.wait.until(ec.title_contains('Stack Overflow'))

	def check_correct_ligin(self):
		check_list = None
		self.go_to_site('https://www.google.com/gmail/')
		lang = self.get_lang_site()
		if lang == "ru":
			check_list = ['Входящие', 'Отправленные']
		elif lang == "en":
			check_list = ['Inbox', 'Sent']
		return check_list

	def get_amount_mail(self) -> int:
		self.go_to_site(f'https://mail.google.com/mail/u/0/#all')
		lang = self.get_lang_site()
		if lang == "ru":
			self.wait.until(ec.title_contains('Вся почта'))
		elif lang == "en":
			self.wait.until(ec.title_contains('All Mail'))
		amount_mail = self.find_elements(By.CLASS_NAME, 'ts')
		return int(amount_mail[5].text)
