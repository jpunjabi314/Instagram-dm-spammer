
#script.py
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import stdiomask

print("Disclaimer: This code is for educational purposes only. Before spamming, you should have consent from the person who is being attacked.")
print("This program only works if you have dmed the person before spamming them.")

print("")

class InstaScript:
    def __init__(self, username, password, victim_username, message_text, number):
        self.username = username
        self.password = password
        self.victim_username = victim_username
        self.number = number
        self.message_text = message_text
        self.browser = webdriver.Chrome()

    def login(self):
        browser = self.browser
        browser.implicitly_wait(5)

        #opening instagram.com
        browser.get('https://www.instagram.com/')
        #-------login process starts
        #finding input boxes for username and password and pasing the appropriate values
        browser.find_element_by_xpath("//input[@name='username']").send_keys(self.username)
        browser.find_element_by_xpath("//input[@name='password']").send_keys(self.password)
        sleep(1)
        #findind login button and clicking it
        browser.find_element_by_xpath("//button[@type='submit']").click()
        #-------login process ends

    def victim_profile(self):
        browser = self.browser
        browser.implicitly_wait(5)

        #Clicking "Not Now" in pop up just after login
        sleep(2.5)
        not_now_button = browser.find_element_by_xpath("//button[text()='Not Now']")
        sleep(1)
        not_now_button.click()

        #Clicking "Not Now" in pop up just after login for notifcations 

        sleep(2.5)
        not_now_button2 = browser.find_element_by_xpath("//button[text()='Not Now']")
        sleep(1)
        not_now_button2.click()
        sleep(2)

        browser.find_element_by_xpath("//span[text()='Search']").click()
        sleep(1)

        browser.find_element_by_xpath("//input[@placeholder='Search']").send_keys(self.victim_username)
        sleep(2)

        searchforvictim = browser.find_element_by_xpath("//*[text()='" + self.victim_username + "']")
        searchforvictim.click()

        sleep(2)

        #message_button = browser.find_element_by_xpath("//button[text()='Message']")
        #message_button.click()

        browser.find_element_by_xpath("//button[@type='button']").click()

        sleep(2)

        sleep(1.5)

        message_area = browser.find_element_by_xpath("//textarea[@placeholder='Message...']")
        message_area.click()
        message_area.send_keys(self.message_text, Keys.ENTER)
        for _ in range(0, self.number):
            message_area = browser.find_element_by_xpath("//textarea[@placeholder='Message...']")
            message_area.click()
            message_area.send_keys(self.message_text, Keys.ENTER)







if __name__ == '__main__':


    username = input("Enter your username: ")
    password = stdiomask.getpass(prompt='Password: ', mask='*')
    victimusername = input("Enter your victim username: ")
    message = input("Enter your message: ")
    number = int(input("Enter the number of times you would like to send the message: "))


    victim = InstaScript(username, password, victimusername, message, number)
    victim.login()
    victim.victim_profile()
        


