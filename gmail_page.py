# -*- coding: utf-8 -*-
from base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

from settings import SURNAME, MAIL_RECIPIENT


class GMailPage(BasePage):
	lang = "en"
	"""
	Gmail page class
	"""
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
		self.input_data(By.NAME, 'identifier', mail)
		self.click_on_element(By.ID, 'identifierNext')
		self.input_data(By.NAME, 'password', password)
		self.click_on_element(By.ID, 'passwordNext')
		self.wait.until(ec.title_contains('Stack Overflow'))

	def check_correct_login(self):
		"""
		Verification of authorization
		:return:
		"""
		check_list = ['Inbox', 'Sent']
		self.go_to_site('https://mail.google.com/mail/u/0/#inbox')
		GMailPage.lang = self.get_lang_site()
		if GMailPage.lang == "ru":
			check_list = ['Входящие', 'Отправленные']
		return check_list

	def get_amount_mail(self) -> int:
		"""
		Determination of the number of mails
		:return: amount_mail
		"""
		self.go_to_site(f'https://mail.google.com/mail/u/0/#all')
		if GMailPage.lang == "ru":
			self.wait.until(ec.title_contains('Вся почта'))
		elif GMailPage.lang == "en":
			self.wait.until(ec.title_contains('All Mail'))
		amount_mail = self.get_elements(By.CLASS_NAME, 'ts')
		return int(amount_mail[5].text)

	def send_mail(self, amount_mail):
		"""
		Writing and sending mail
		:param amount_mail:
		:return:
		"""
		self.go_to_site('https://mail.google.com/mail/u/0/h/vn7jwxec9om4/?&cs=b&pv=tl&v=b')
		letter_subject = f"Тестовое задание. {SURNAME}"
		letter = self.compose_a_letter(amount_mail)
		self.input_data(By.NAME, 'to', MAIL_RECIPIENT)
		self.input_data(By.NAME, 'subject', letter_subject)
		self.input_data(By.NAME, 'body', letter)
		# self.click_on_element(By.NAME, 'nvp_bu_send')

	@staticmethod
	def compose_a_letter(amount_mail):
		letter = f"На данной почте всего {amount_mail} "
		if amount_mail == 1:
			letter.join('письмо')
		elif 2 <= amount_mail >= 4:
			letter.join('письма')
		else:
			letter.join('писем')
		return letter
