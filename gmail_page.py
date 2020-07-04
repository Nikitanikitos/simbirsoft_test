# -*- coding: utf-8 -*-
from time import sleep

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec


class GMailPage(BasePage):
	amount_mail_dict = {'inbox': 0, 'starred': 0, 'deferred': 0, 'sent': 0, 'drafts': 0}
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
		self.go_to_site('https://www.google.com/gmail/')
		page_source = self.get_page_source()
		return page_source

	def get_amount_mail(self) -> int:
		wait = WebDriverWait(self.driver, 2)
		self.go_to_site(f'https://mail.google.com/mail/u/0/#all')
		while True:
			try:
				wait.until(ec.visibility_of_element_located((By.CLASS_NAME, 'v1')))
			except TimeoutException:
				break
		amount_mail = self.find_elements(By.CLASS_NAME, 'ts')
		return int(amount_mail[5].text)
