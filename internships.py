from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

passfile = open('pass.txt', 'r')
password = passfile.read()
passfile.close()

browser = Chrome(options= Options().set_headless())

browser.get('https://courseweb.sliit.lk/login/index.php')

usernameTextBox = browser.find_element_by_xpath('//*[@id="username"]')
usernameTextBox.send_keys('IT19051130')

passwordTextBox = browser.find_element_by_xpath('//*[@id="password"]')
passwordTextBox.send_keys(password)
passwordTextBox.submit()

browser.get('https://courseweb.sliit.lk/login/index.php')

opportunities = []
