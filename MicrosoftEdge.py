from selenium import webdriver
from bs4 import BeautifulSoup
from  datetime import date, timedelta

#datetime.now().strftime("%a, %d %b %Y, %I:%M %p")
dateWeekAgo = date.today() - timedelta(days = 7)

yearIn = int(dateWeekAgo.strftime("%Y"))
monthIn = int(dateWeekAgo.strftime("%m"))

credFile = open('Credentials.txt', 'r')
username = credFile.readline().strip()
password = credFile.readline().strip()
credFile.close()

browser = webdriver.Edge(r"./msedgedriver.exe")

browser.get('https://courseweb.sliit.lk/login/index.php')

usernameTextBox = browser.find_element_by_xpath('//*[@id="username"]')
usernameTextBox.send_keys(username)

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
        if year >= yearIn:
            if month >= monthIn:
                opportunities.append(opportunity)
        else:
            break

for y in opportunities:
    listFile.write(y + '\n')
    print(y)

listFile.close()