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


class SendMailTest(unittest.TestCase):
	window = GMailPage()
	numbers_mail = 0

	def setUp(self):
		self.window = SendMailTest.window

	@allure.title("Test authorization")
	def test_01_authorization(self):
		"""
		Authorization on stackoverflow through google account and verification of authorization
		:return:
		"""
		site = SendMailTest.window
		with allure.step("gmail.google authorization"):
			self.window.login(EMAIL_FOR_LOG_IN, PASSWORD_FOR_LOG_IN)
		with allure.step("Verification of authorization"):
			check_list = self.window.check_correct_login()
			page_source = self.window.get_page_source()
			for check_item in check_list:
				self.assertIn(check_item, page_source)
			self.assertTrue('Gmail' in site.get_title())

	@allure.title("Determination of the numbers of mails")
	def test_02_get_numbers_of_mails(self):
		"""
		Determination of the numbers of mails
		:return:
		"""
		numbers_mail = 0
		with allure.step("Determination of the numbers of mails"):
			numbers_mail = self.window.get_amount_mail()
			if EXPECTED_AMOUNT_MAIL:
				self.assertEqual(EXPECTED_AMOUNT_MAIL, numbers_mail)
			self.assertEqual(type(numbers_mail), int)
		SendMailTest.numbers_mail = numbers_mail

	@allure.title("Writing and sending mail")
	def test_03_write_and_send_mail(self):
		"""
		Writing and sending mail
		:return:
		"""
		with allure.step("Writing and sending mail"):
			self.window.send_mail(SendMailTest.numbers_mail)

	def test_04_close_window(self):
		"""
		Last test
		:return:
		"""
		self.window.driver.close()


if __name__ == "__main__":
	if sys.argv:
		BasePage.capabilities = {
			"browserName": sys.argv[1],
			"platform": sys.argv[2],
		}
	unittest.main()
