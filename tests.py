#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

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
		self.site = GMailPage()

	@allure.title("Проверка логирования")
	def test_send_mail(self):
		"""
		Авторизовываемся на gmail через stackoverflow,
		определяем колличество писем,
		пишем и отправляем письмо
		:return:
		"""
		site = self.site
		expected_amount_mail = settings.EXPECTED_AMOUNT_MAIL
		with allure.step("Авторизация на сайте google.com/gmail/"):
			site.login(GoogleTest.mail, GoogleTest.password)
		with allure.step("Проверка корректности авторизации"):
			check_list = site.check_correct_ligin()
			page_source = site.get_page_source()
			if check_list:
				for check_item in check_list:
					self.assertIn(check_item, page_source)
			self.assertTrue('Gmail' in site.get_title())
		with allure.step("Получение колличества писем"):
			amount_mail = site.get_amount_mail()
			if expected_amount_mail:
				self.assertEqual(expected_amount_mail, amount_mail)
			self.assertEqual(type(amount_mail), int)

	def tearDown(self):
		self.site.close_site()


if __name__ == "__main__":
	unittest.main()
