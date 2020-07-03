#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import settings

import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
	"""
	Базовый класс содержащий основные методы для работы со страницами
	"""
	def __init__(self, driver):
		print(driver)
		self.driver = driver()
		self.wait = WebDriverWait(self.driver, 10)

	def go_to_site(self, url):
		self.driver.get(url)

	def click_on_element(self, by: str, element: str):
		element_on_click = self.wait.until(ec.presence_of_element_located((by, element)))
		element_on_click.click()

	def close_site(self):
		self.driver.close()

	def input_data(self, by, path: str, data: str):
		input = self.wait.until(ec.presence_of_element_located((by, path)))
		input.send_keys(data)

	def get_page_source(self):
		return self.driver.page_source


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


class GoogleTest(unittest.TestCase):
	mail = settings.EMAIL_FOR_LOG_IN
	password = settings.PASSWORD_FOR_LOG_IN

	def setUp(self) -> None:
		self.site = GMailPage(webdriver.Chrome)

	def test_login_google(self):
		"""
		Первый тест.
		Тестируем логирование на сайте google.com/gmail/ через "временный" сайт stackoverflow.com.
		Если на странице есть разделы "Входящие" И "Отправленные" - тест пройдет успешно
		:return:
		"""
		self.site.go_to_site(
			'https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2fusers%2fstory%2fcurrent%27')
		self.site.login(GoogleTest.mail, GoogleTest.password)
		sleep(2)
		self.site.go_to_site('https://www.google.com/gmail/')
		sleep(2)
		page_source = self.site.get_page_source()
		self.assertIn('Входящие', page_source)
		self.assertIn('Отправленные', page_source)

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
