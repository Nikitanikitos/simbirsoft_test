# -*- coding: utf-8 -*-
from time import sleep

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium import webdriver


class BasePage:
	capabilities = {"browserName": "chrome", "platform": "linux"}
	"""
	Базовый класс содержащий основные методы для работы со страницами
	"""

	def __init__(self):
		# self.driver = webdriver.Remote(desired_capabilities=BasePage.capabilities)
		self.driver = webdriver.Chrome()
		self.wait = WebDriverWait(self.driver, 10)

	def go_to_site(self, url):
		self.driver.get(url)

	def click_on_element(self, by, element: str):
		self.wait.until(ec.visibility_of_element_located((by, element)))
		element_on_click = self.driver.find_element(by, element)
		element_on_click.click()

	def close_site(self):
		self.driver.close()

	def input_data(self, by, path: str, data: str):
		self.wait.until(ec.visibility_of_element_located((by, path)))
		input = self.driver.find_element(by, path)
		input.send_keys(data)

	def get_page_source(self):
		return self.driver.page_source

	def get_lang_site(self):
		page_source = self.driver.page_source
		lang = page_source[12:14]
		return lang

	def get_title(self):
		return self.driver.title

	def find_elements(self, by: str, elements: str) -> list:
		list_elements = self.wait.until(ec.presence_of_all_elements_located((by, elements)))
		return list_elements

	def find_element(self, by: str, element: str):
		result_element = self.wait.until(ec.visibility_of_element_located((by, element)))
		return result_element
