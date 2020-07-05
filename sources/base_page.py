# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
	"""
	Базовой класс страницы
	"""
	capabilities = {"browserName": "chrome", "platform": "linux"}

	def __init__(self):
		# self.driver = webdriver.Remote(desired_capabilities=BasePage.capabilities)
		self.driver = webdriver.Firefox()
		self.wait = WebDriverWait(self.driver, 20)

	def go_to_site(self, url):
		self.driver.get(url)

	def click_on_element(self, by, element: str):
		element_on_click = self.wait.until(ec.visibility_of_element_located((by, element)))
		element_on_click.click()

	def close_site(self):
		self.driver.close()

	def enter_data(self, by, path: str, data: str):
		enter = self.wait.until(ec.visibility_of_element_located((by, path)))
		enter.send_keys(data)
		return enter

	def press_enter(self, element):
		element.send_keys(Keys.ENTER)

	def waiting_desired_url(self, url_part):
		self.wait.until(ec.url_contains(url_part))

	def get_list_elements(self, by: str, value: str) -> list:
		list_elements = self.wait.until(ec.presence_of_all_elements_located((by, value)))
		return list_elements

	def get_element(self, by: str, value: str):
		element = self.wait.until(ec.visibility_of_element_located((by, value)))
		return element
