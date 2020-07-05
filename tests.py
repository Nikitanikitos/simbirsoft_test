#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

from base_page import BasePage

try:
	from settings import EMAIL_FOR_LOG_IN, PASSWORD_FOR_LOG_IN, EXPECTED_NUMBERS_OF_MAIL
except ImportError:
	exit("Do copy settings.py.default in settings.py and set values")

import allure
from gmail_page import GMailPage
import unittest


class GMailTest(unittest.TestCase):
	"""
	Test for counting the number of mails and sending mail with this data
	"""

	@allure.step("Webdriver initialization")
	def setUp(self):
		self.window = GMailPage()

	@allure.testcase("Determination of the number of mails, writing and sending mail")
	def test_write_and_send_mail(self):
		"""
		The test determines the number of mails and writes and sends mail
		:return:
		"""
		self.gmail_authorization()
		self.check_authorization()
		amount_mail = self.determine_number_of_mails()
		self.write_and_send_mail(amount_mail)

	@allure.step("Gmail authorization")
	def gmail_authorization(self):
		"""
		Authorization on stackoverflow through google account
		:return:
		"""
		self.window.login(EMAIL_FOR_LOG_IN, PASSWORD_FOR_LOG_IN)

	@allure.step("Verification of authorization")
	def check_authorization(self):
		"""
		Verification of authorization
		:return:
		"""
		check_list = self.window.check_correct_login()
		page_source = self.window.get_page_source()
		if check_list:
			for check_item in check_list:
				self.assertIn(check_item, page_source)
		self.assertTrue('Gmail' in self.window.get_title())

	@allure.step("Determination of the number of mails")
	def determine_number_of_mails(self) -> int:
		"""
		Determination of the number of mails.
		If the expected value is known, an equality check is performed with it
		:return:
		"""
		number_of_mails = self.window.determine_number_of_mails()
		if EXPECTED_NUMBERS_OF_MAIL:
			self.assertEqual(EXPECTED_NUMBERS_OF_MAIL, number_of_mails)
		self.assertEqual(type(number_of_mails), int)
		return number_of_mails

	@allure.step("Writing and sending mail")
	def write_and_send_mail(self, number_of_mails: int):
		"""
		Writing and sending mail
		:param number_of_mails:
		:return:
		"""
		self.window.send_mail(number_of_mails)

	@allure.step("Webdriver close")
	def tearDown(self):
		self.window.close_site()


if __name__ == "__main__":
	if len(sys.argv) == 3:
		BasePage.capabilities['browserName'] = sys.argv[1]
		BasePage.capabilities['platform'] = sys.argv[2]
		del sys.argv[2]
		del sys.argv[1]
	unittest.main()
