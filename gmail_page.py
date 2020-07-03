# -*- coding: utf-8 -*-
from base_page import BasePage
from selenium.webdriver.common.by import By


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
		self.click_on_element(By.CLASS_NAME, 's-btn__google')
		self.input_data(By.NAME, 'identifier', mail)
		self.click_on_element(By.ID, 'identifierNext')
		self.input_data(By.NAME, 'password', password)
		self.click_on_element(By.ID, 'passwordNext')

	# def get_amount_mail(self) -> dict:
	# 	amount_mail =
	# 	for type_mail in GMailPage.amount_mail_dict.keys():
	# 		self.click_on_element(By.PARTIAL_LINK_TEXT, type_mail)
	# 	return GMailPage.amount_mail_dict

