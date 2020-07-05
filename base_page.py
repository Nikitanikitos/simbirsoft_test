# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium import webdriver


class BasePage:
	capabilities = {"browserName": "chrome", "platform": "linux"}
	"""
	Base page class
	"""

	def __init__(self):
		# self.driver = webdriver.Remote(desired_capabilities=BasePage.capabilities)
		self.driver = webdriver.Chrome()
		self.driver.maximize_window()
		self.wait = WebDriverWait(self.driver, 10)

	def go_to_site(self, url):
		self.driver.get(url)

	def click_on_element(self, by, element: str):
		element_on_click = self.wait.until(ec.visibility_of_element_located((by, element)))
		# element_on_click = self.driver.find_element(by, element)
		element_on_click.click()

	def close_site(self):
		self.driver.close()

	def input_data(self, by, path: str, data: str):
		input = self.wait.until(ec.visibility_of_element_located((by, path)))
		# input = self.driver.find_element(by, path)
		input.send_keys(data)
		return input

	def get_page_source(self):
		return self.driver.page_source

	def get_lang_site(self) -> str:
		page_source = self.driver.page_source
		lang = page_source[12:14]
		return lang

	def get_title(self) -> str:
		return self.driver.title

	def get_elements(self, by: str, elements: str) -> list:
		list_elements = self.wait.until(ec.presence_of_all_elements_located((by, elements)))
		return list_elements

	def get_element(self, by: str, element: str):
		result_element = self.wait.until(ec.visibility_of_element_located((by, element)))
		return result_element

	def open_new_tab(self):
		body = self.wait.until(ec.visibility_of_element_located((By.CLASS_NAME, 'body')))
		body.send_keys(Keys.CONTROL + 't')
