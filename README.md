# Тестовое задание для SimbirSoft

## Краткое описание
Программа выполняет авторизацию в google аккаунт,подсчитывает колличество писем на почте, формирует письмо и отправляет указанному получателю.<br>
На всю работу программы реализованны тесты, которые проверяют каждый шаг программы. В написании тестов используется паттерн тестирования [Page object]

## Содержание репозитория
- ***test.py*** - основной файл с тестами
- ***sources/base_page.py*** - файл с базовым классом страницы
- ***sources/gmail_page.py*** - файл с классом gmail страницы
- ***settings.py.default*** - файл с настройками
- ***selenium-server-standalone.jar*** - java файл для поддержки Selenium Grid

## Используемый стек:
- [Selenium]
- [Selenium Grid]
- [Allure]
- [unittest]

## Настройки программы
Для успешного исполнения программы скопировать содержимое settings.py.default в settings.py и установить нужные значения

## Запуск программы
Перед запуском программы запустите selenium grid, например так:

	java -jar selenium-server-standalone.jar -role hub
	java -jar selenium-server-standalone.jar -role node -browser browserName=chrome,platform=LINUX

Для запуска тестов с отчетом Allure используйте run_test.sh (браузер по умолчанию=chrome, platform=LINUX).

Для запуска тестов с изменением параметров Webdriver выполните (тест без отчета Allure):
	
	./tests.py [Параметр browserName] [Параметр platform]

[Selenium]: //www.selenium.dev/
[Selenium Grid]: //www.selenium.dev/documentation/en/grid/
[Page object]: //habr.com/ru/company/wapstart/blog/138674/
[Allure]: //docs.qameta.io/allure/
[unittest]: //docs.python.org/3/library/unittest.html
