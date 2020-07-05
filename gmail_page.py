# -*- coding: utf-8 -*-
from base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

from settings import SURNAME, MAIL_RECIPIENT


class GMailPage(BasePage):
	"""
	Gmail page class
	"""
	lang = "en"

	def login(self, mail: str, password: str):
		"""
		Authorization on stackoverflow through google account
		:param mail:
		:param password:
		:return:
		"""
		self.go_to_site(
			'https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2fusers%2fstory%2fcurrent%27')
		self.click_on_element(By.CLASS_NAME, 's-btn__google')
		mail_element = self.enter_data(By.NAME, 'identifier', mail)
		self.press_enter(mail_element)
		password_element = self.enter_data(By.NAME, 'password', password)
		self.press_enter(password_element)
		self.waiting_desired_url('stackoverflow')

	def check_correct_login(self) -> tuple:
		"""
		Verification of authorization
		:return:
		"""
		check_list = ('Inbox', 'Sent')
		self.go_to_site('https://mail.google.com/mail/u/0/#inbox')
		self.waiting_desired_url('inbox')
		GMailPage.lang = self.get_lang_site()
		if GMailPage.lang == "ru":
			check_list = ('Входящие', 'Отправленные')
		return check_list

	def determine_number_of_mails(self) -> int:
		"""
		Determination of the number of mails
		:return: amount_mail
		"""
		self.go_to_site(f'https://mail.google.com/mail/u/0/#all')
		self.waiting_desired_url('all')
		if GMailPage.lang == "ru":
			self.wait.until(ec.title_contains('Вся почта'))
		elif GMailPage.lang == "en":
			self.wait.until(ec.title_contains('All Mail'))
		number_of_mails = self.get_list_elements(By.CLASS_NAME, 'ts')[5].text
		return int(number_of_mails)

	def send_mail(self, number_of_mails: int):
		"""
		Writing and sending mail
		:param number_of_mails:
		:return:
		"""
		self.go_to_site('https://mail.google.com/mail/u/0/h/vn7jwxec9om4/?&cs=b&pv=tl&v=b')
		mail_subject = f"Тестовое задание. {SURNAME}"
		mail = self.compose_mail(number_of_mails)
		self.enter_data(By.NAME, 'to', MAIL_RECIPIENT)
		self.enter_data(By.NAME, 'subject', mail_subject)
		self.enter_data(By.NAME, 'body', mail)
		# self.click_on_element(By.NAME, 'nvp_bu_send')

	def compose_mail(self, number_of_mails: int) -> str:
		letter = f"На данной почте всего {number_of_mails} "
		if number_of_mails == 1:
			letter.join('письмо')
		elif 2 <= number_of_mails >= 4:
			letter.join('письма')
		else:
			letter.join('писем')
		return letter

	def get_lang_site(self) -> str:
		page_source = self.driver.page_source
		index = page_source.find('lang') + 6
		lang = page_source[index:index + 2]
		return lang
