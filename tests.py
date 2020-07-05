#!/usr/bin/env python3
# -*- coding: utf-8 -*-
try:
	from sources.settings import EMAIL_FOR_LOG_IN, PASSWORD_FOR_LOG_IN, EXPECTED_NUMBERS_OF_MAIL
except ImportError:
	exit("Сделайте копию settings.py.default в settings.py и установите нужные значения")

from sources.gmail_page import GMailPage
from sources.base_page import BasePage
import unittest
import allure
import sys


class GMailTest(unittest.TestCase):
	"""
	Тест для авторизации в gmail аккаунте,
	подсчета колличества писем на gmail,
	отправки письма с полученными данными
	"""

	@allure.step("Инициализация webdriver")
	def setUp(self):
		self.window = GMailPage()

	@allure.testcase("Определения колличества писем, написание и отправка письма с полученными данными")
	def test_write_and_send_mail(self):
		"""
		Авторизация в gmail, проверка корректности авторизации,
		определения колличества писем на почте,
		написание и отправка письма с полученными данными
		:return:
		"""
		self.gmail_authorization()
		self.check_authorization()
		amount_mail = self.determine_number_of_mails()
		self.write_and_send_mail(amount_mail)

	@allure.step("Авторизация на gmail")
	def gmail_authorization(self):
		"""
		Функция для авторизации в gmail аккаунте через stackoverflow
		(обход защиты от ненадежных аккаунтов)
		:return:
		"""
		self.window.login(EMAIL_FOR_LOG_IN, PASSWORD_FOR_LOG_IN)

	@allure.step("Проверка корректности авторизации")
	def check_authorization(self):
		"""
		Функция проверяет корректность шага авторизации
		:return:
		"""
		check_list = self.window.check_correct_login()
		page_source = self.window.driver.page_source
		if check_list:
			for check_item in check_list:
				self.assertIn(check_item, page_source)
		self.assertTrue('Gmail' in self.window.driver.title)

	@allure.step("Определенние колличества писем на почте")
	def determine_number_of_mails(self) -> int:
		"""
		Функция получает колличество писем на почте.
		Если ожидаемое значение известно - значения сравниваются
		:return number_of_mails:
		"""
		number_of_mails = self.window.determine_number_of_mails()
		if EXPECTED_NUMBERS_OF_MAIL:
			self.assertEqual(EXPECTED_NUMBERS_OF_MAIL, number_of_mails)
		self.assertEqual(type(number_of_mails), int)
		return number_of_mails

	@allure.step("Написание и отправка письма")
	def write_and_send_mail(self, number_of_mails: int):
		"""
		Функция для составления и отправки письма на указанный адрес в settings.py
		:param number_of_mails:
		:return:
		"""
		self.window.send_mail(number_of_mails)

	@allure.step("Закрытие webdriver")
	def tearDown(self):
		self.window.close_site()


if __name__ == "__main__":
	if len(sys.argv) == 3:
		BasePage.capabilities['browserName'] = sys.argv[1]
		BasePage.capabilities['platform'] = sys.argv[2]
		for q in range(2):
			sys.argv.pop()
	# GMailTest.run()
	unittest.main()
