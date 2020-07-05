#!/usr/bin/env python3
# -*- coding: utf-8 -*-
try:
	from settings import EMAIL_FOR_LOG_IN, PASSWORD_FOR_LOG_IN, EXPECTED_AMOUNT_MAIL
except ImportError:
	exit("Do copy settings.py.default in settings.py and set values")

import sys
import allure
import unittest
from gmail_page import GMailPage
from base_page import BasePage


class SendMailTest(unittest.TestCase):

	def setUp(self):
		with allure.step("Webdriver initialization"):
			self.window = GMailPage()

	@allure.testcase("Determination of the numbers of mails, writing and sending mail")
	def test_write_and_send_mail(self):
		"""
		The test determines the number of mails and writes and sends mail
		:return:
		"""
		self.gmail_authorization()
		self.check_correct_authorization()
		amount_mail = self.determine_numbers_mails()
		self.write_and_send_mail(amount_mail)

	@allure.step("Gmail authorization")
	def gmail_authorization(self):
		"""
		Authorization on stackoverflow through google account,
		:return:
		"""
		self.window.login(EMAIL_FOR_LOG_IN, PASSWORD_FOR_LOG_IN)

	@allure.step("verification of authorization")
	def check_correct_authorization(self):
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

	@allure.step("Determination of the numbers of mails")
	def determine_numbers_mails(self):
		"""
		Determination of the numbers of mails
		:return:
		"""
		amount_mail = self.window.get_amount_mail()
		if EXPECTED_AMOUNT_MAIL:
			self.assertEqual(EXPECTED_AMOUNT_MAIL, amount_mail)
		self.assertEqual(type(amount_mail), int)
		return amount_mail

	@allure.step("Writing and sending mail")
	def write_and_send_mail(self, amount_mail):
		"""
		Writing and sending mail
		:param amount_mail:
		:return:
		"""
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
