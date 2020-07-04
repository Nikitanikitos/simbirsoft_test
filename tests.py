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
	cookies = None

	def setUp(self) -> None:
		self.site = GMailPage()

	@allure.title("Проверка логирования")
	def test_send_mail(self):
		expected_amount_mail = settings.EXPECTED_AMOUNT_MAIL
		"""
		:return:
		"""
		with allure.step("Авторизация на сайте google.com/gmail/"):
			self.site.login(GoogleTest.mail, GoogleTest.password)
		with allure.step("Проверка корректности авторизации"):
			page_source = self.site.check_correct_ligin()
			self.assertIn('Входящие', page_source)
			self.assertIn('Отправленные', page_source)
			self.assertTrue('Gmail' in self.site.get_title())
		with allure.step("Получение колличества писем"):
			amount_mail = self.site.get_amount_mail()
			if expected_amount_mail:
				self.assertEqual(expected_amount_mail, amount_mail)
			self.assertEqual(type(amount_mail), int)


	def tearDown(self):
		self.site.close_site()


if __name__ == "__main__":
	unittest.main()
