#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import settings
from gmail_page import GMailPage

from time import sleep

import allure
import pytest
import unittest
from selenium import webdriver


class GoogleTest(unittest.TestCase):
	mail = settings.EMAIL_FOR_LOG_IN
	password = settings.PASSWORD_FOR_LOG_IN

	def setUp(self) -> None:
		self.site = GMailPage(webdriver.Chrome)

	@allure.testcase('Login test')
	def test_login_google(self):
		"""
		Первый тест.
		Тестируем логирование на сайте google.com/gmail/ через "временный" сайт stackoverflow.com.
		Если на странице есть разделы "Входящие" И "Отправленные" - тест пройдет успешно
		:return:
		"""
		with pytest.allure.step():
			self.site.go_to_site(
				'https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2fusers%2fstory%2fcurrent%27')
		self.site.login(GoogleTest.mail, GoogleTest.password)
		sleep(2)
		self.site.go_to_site('https://www.google.com/gmail/')
		page_source = self.site.get_page_source()
		self.assertIn('Входящие', page_source)
		self.assertIn('Отправленные', page_source)
		self.assertTrue('Gmail' in self.site.get_title())

	def test_count_mail(self):
		"""
		Второй тест.
		Тестируем правильность получения данных о колличестве письмах на почте.
		Если известно ожидаемое значение - внесите его в переменную setting.EXPECTED_AMOUNT_MAIL
		:return:
		"""
		pass

	def tearDown(self):
		self.site.close_site()


if __name__ == "__main__":
	unittest.main()
