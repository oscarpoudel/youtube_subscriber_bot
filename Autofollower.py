from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Enter your username and password to the end part


class subscribebot:
    def __init__(self, username, passowrd):
        self.username = username
        self.password = passowrd
        self.bot = webdriver.Chrome(executable_path='chromedriver.exe')

    def login(self):
        bot = self.bot
        bot.get("https://www.ytmonster.net/login")
        time.sleep(3)
        email = bot.find_element_by_name('usernames').send_keys(self.username)
        password = bot.find_element_by_name(
            'passwords').send_keys(self.password)
        time.sleep(1)
        bot.find_element_by_name('passwords').send_keys(Keys.RETURN)
        time.sleep(3)

    def subscribe(self):
        bot = self.bot
        bot.get("https://www.ytmonster.net/exchange/subscribers")
        time.sleep(5)
       # bot.find_element_by_xpath('//a[text()="Subscribe"]').click()
        bot.find_element_by_id("subText").click()
        time.sleep(5)
        tablist = bot.window_handles
        bot.switch_to.window(tablist[1])
        time.sleep(2)
        bot.find_element_by_xpath(
            '//*[@id="buttons"]/ytd-button-renderer/a').click()
        time.sleep(5)
        emailid = bot.find_element_by_xpath('//*[@id="identifierId"]')
        emailid.send_keys("bbaarraall111")

        next = bot.find_element_by_xpath(
            '//*[@id="identifierNext"]/div/button/div[2]').click()
        time.sleep(5)

        passw = bot.find_element_by_xpath(
            '//*[@id="password"]/div[1]/div/div[1]/input')
        passw.send_keys("oossccaarR")
        next2 = bot.find_element_by_xpath(
            '//*[@id="passwordNext"]/div/button/div[2]').click()
        time.sleep(15)
        subotton = bot.find_element_by_xpath(
            '//*[@id="subscribe-button"]/ytd-subscribe-button-renderer/paper-button').click()
        time.sleep(2)
        bot.close()
        bot.switch_to.window(tablist[0])
        veryfy = bot.find_element_by_class_name('verifyClick').click()
        time.sleep(10)
        i = 1
        while True:
            bot.find_element_by_id("subText").click()
            time.sleep(5)
            tabl = bot.window_handles
            bot.switch_to.window(tabl[1])
            time.sleep(2)
            subotton = bot.find_element_by_xpath(
                '//*[@id="subscribe-button"]/ytd-subscribe-button-renderer/paper-button').click()
            time.sleep(2)
            bot.close()
            bot.switch_to.window(tabl[0])
            veryfy = bot.find_element_by_class_name('verifyClick').click()
            time.sleep(17)
            i = i+1
            print("done subscription = ", i, "\n")
            if(i == 70):
                print("subscription limit ended for today . Enjoy your day!!")
                bot.close()


if __name__ == '__main__':
    yout = subscribebot("Enter Your Username", "Enter your password")
    yout.login()
    yout.subscribe()
