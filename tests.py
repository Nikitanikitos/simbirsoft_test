#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

try:
	from settings import EMAIL_FOR_LOG_IN, PASSWORD_FOR_LOG_IN, EXPECTED_AMOUNT_MAIL
except ImportError:
	exit("Do copy settings.py.default in settings.py and set values")

import allure
import unittest
from gmail_page import GMailPage
from base_page import BasePage


class GoogleTest(unittest.TestCase):

	def setUp(self):
		self.site = GMailPage()

	@allure.title("Тест авторизации, подсчета писем, отправки письма")
	def test_send_mail(self):
		"""
		Авторизовываемся на gmail через stackoverflow,
		определяем колличество писем,
		пишем и отправляем письмо
		:return:
		"""
		site = self.site
		with allure.step("Авторизация на сайте google.com/gmail/"):
			site.login(EMAIL_FOR_LOG_IN, PASSWORD_FOR_LOG_IN)
		with allure.step("Проверка корректности авторизации"):
			check_list = site.check_correct_login()
			page_source = site.get_page_source()
			if check_list:
				for check_item in check_list:
					self.assertIn(check_item, page_source)
			self.assertTrue('Gmail' in site.get_title())
		with allure.step("Получение колличества писем"):
			amount_mail = site.get_amount_mail()
			if EXPECTED_AMOUNT_MAIL:
				self.assertEqual(EXPECTED_AMOUNT_MAIL, amount_mail)
			self.assertEqual(type(amount_mail), int)
		with allure.step("Отправка письма"):
			site.send_mail(amount_mail)

	def tearDown(self):
		self.site.close_site()


if __name__ == "__main__":
	if sys.argv:
		BasePage.capabilities = {
			"browserName": sys.argv[1],
			"platform": sys.argv[2],
		}
	unittest.main()
