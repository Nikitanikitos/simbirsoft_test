from time import sleep
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import settings

class google_test(unittest.TestCase):

	def setUp(self) -> None:
		self.driver = webdriver.Chrome()

	def test_login_google(self):
		self.driver.get('https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2fusers%2fstory%2fcurrent%27')
		sleep(2)
		self.driver.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]').click()
		self.driver.find_element_by_xpath('//input[@type="email"]').send_keys(settings.EMAIL_FOR_LOG_IN)
		self.driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
		sleep(2)
		self.driver.find_element_by_xpath('//input[@type="password"]').send_keys(settings.PASSWORD_FOR_LOG_IN)
		self.driver.find_element_by_xpath('//*[@id="passwordNext"]').click()
		sleep(2)
		self.driver.get('https://www.google.com/gmail/')
		sleep(4)
		self.driver.close()


if __name__ == "__main__":
	unittest.main()
