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


@allure.feature('Feature1')
@allure.story('Story1')
class SendMailTest(unittest.TestCase):

	def setUp(self):
		with allure.step("Webdriver initialization"):
			self.window = GMailPage()

	@allure.testcase("Test Gmail authorization, determination of the numbers of mails and writing and sending mail")
	def test_write_and_send_mail(self):
		"""
		Authorization on stackoverflow through google account,
		Determination of the numbers of mails,
		Writing and sending mail
		:return:
		"""
		with allure.step("Gmail authorization"):
			self.window.login(EMAIL_FOR_LOG_IN, PASSWORD_FOR_LOG_IN)
		with allure.step("verification of authorization"):
			check_list = self.window.check_correct_login()
			page_source = self.window.get_page_source()
			if check_list:
				for check_item in check_list:
					self.assertIn(check_item, page_source)
			self.assertTrue('Gmail' in self.window.get_title())
		with allure.step("Determination of the numbers of mails"):
			amount_mail = self.window.get_amount_mail()
			if EXPECTED_AMOUNT_MAIL:
				self.assertEqual(EXPECTED_AMOUNT_MAIL, amount_mail)
			self.assertEqual(type(amount_mail), int)
		with allure.step("Writing and sending mail"):
			self.window.send_mail(amount_mail)

	def tearDown(self):
		with allure.step("Webdriver close"):
			self.window.close_site()


if __name__ == "__main__":
	if sys.argv:
		BasePage.capabilities = {
			"browserName": sys.argv[1],
			"platform": sys.argv[2],
		}
	unittest.main()
