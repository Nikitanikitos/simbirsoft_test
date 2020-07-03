# -*- coding: utf-8 -*-
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
	"""
	Базовый класс содержащий основные методы для работы со страницами
	"""
	def __init__(self, driver):
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

	def get_title(self):
		return self.driver.title
