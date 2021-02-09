from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from  datetime import datetime

#datetime.now().strftime("%a, %d %b %Y, %I:%M %p")

yearIn = 2021
monthIn = 1
dateIn = 1

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

browser.get('https://courseweb.sliit.lk/mod/forum/view.php?f=211&showall=1')

content = browser.page_source
soup = BeautifulSoup(content, features="html.parser")

opportunities = []
listFile = open('../List.txt', 'w')

opportunity = ''

startIndex = 0

for x in soup.findAll('td', attrs={'class': 'topic starter'}):
    opportunity = str(x.text).strip()
    if opportunity.find('Internship') != -1:
        startIndex = opportunity.find('20')
        year = int(opportunity[startIndex:startIndex+4])
        month = int(opportunity[startIndex+6:startIndex+7])
        date = int(opportunity[startIndex+9:startIndex+10])
        if year >= yearIn:
            if month >= monthIn:
                if date >= dateIn:
                    opportunities.append(opportunity)
        else:
            break

for y in opportunities:
    listFile.write(y + '\n')

listFile.close()

