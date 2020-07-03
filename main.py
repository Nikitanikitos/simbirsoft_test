from time import sleep
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import settings


class BasePage:

	def __init__(self, driver):
		self.driver = driver()

	def go_to_site(self, url):
		self.driver.get(url)

	def click_on_element(self, by, element):
		element_on_click = self.driver.find_element(by, element)
		element_on_click.click()

	def close_site(self):
		self.driver.close()

	def input_data(self, by, path, data):
		input = self.driver.find_element(by, path)
		input.send_keys(data)

	def get_page_source(self):
		return self.driver.page_source


class GMailPage(BasePage):

	def login(self, mail, password):
		self.click_on_element(By.XPATH, '//*[@id="openid-buttons"]/button[1]')
		sleep(1)
		self.input_data(By.NAME, 'identifier', mail)
		self.click_on_element(By.ID, 'identifierNext')
		sleep(1)
		self.input_data(By.NAME, 'password', password)
		self.click_on_element(By.ID, 'passwordNext')


class GoogleTest(unittest.TestCase):
	mail = settings.EMAIL_FOR_LOG_IN
	password = settings.PASSWORD_FOR_LOG_IN

	def setUp(self) -> None:
		self.site = GMailPage(webdriver.Chrome)

	def test_login_google(self):
		self.site.go_to_site(
			'https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2fusers%2fstory%2fcurrent%27')
		sleep(1)
		self.site.login(GoogleTest.mail, GoogleTest.password)
		sleep(2)
		self.site.go_to_site('https://www.google.com/gmail/')
		sleep(4)
		self.assertIn('Входящие', self.site.get_page_source())

	def test_count_mail(self):
		pass

	def tearDown(self):
		self.driver.close_site()


if __name__ == "__main__":
	unittest.main()
