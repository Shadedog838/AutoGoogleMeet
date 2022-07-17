from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import datetime
import time
import os
import keyboard


#Loads chrome with default settings
opt=Options()
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")
opt.add_argument('--ignore-ssl-errors=yes')
opt.add_argument('--ignore-certificate-errors')
# Pass the argument 1 to allow and 2 to block
opt.add_experimental_option("prefs", { \
"profile.default_content_setting_values.media_stream_mic": 1,
"profile.default_content_setting_values.media_stream_camera": 1,
"profile.default_content_setting_values.geolocation": 1,
"profile.default_content_setting_values.notifications": 1
})

#Gives path to chrome webdriver and loads classroom webpage


class meet_bot:
	def __init__(self):
		self.bot = webdriver.Chrome(chrome_options=opt, executable_path='C:\Program Files (x86)\chromedriver.exe')
	def login(self,email,pas):
		bot = self.bot
		bot.get("https://accounts.google.com/ServiceLogin/signinchooser?ltmpl=meet&continue=https%3A%2F%2Fmeet.google.com%3Fhs%3D193&&o_ref=https%3A%2F%2Fwww.google.com%2F&_ga=2.238615491.291103277.1658079668-1292948687.1658079668&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
		time.sleep(2)
		email_in = bot.find_element("xpath", "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input")
		email_in.send_keys(email)
		next_btn = bot.find_element("xpath", "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button")
		next_btn.click()
		time.sleep(2)
		pas_in = bot.find_element("xpath, ""/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input")
		pas_in.send_keys(pas)
		next1_btn = bot.find_element("xpath", "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]")
		next1_btn.click()
		time.sleep(2)
	def join(self,meeting_link):
		bot = self.bot
		bot.get(meeting_link)
		time.sleep(1)
		diss_btn = bot.find_element("xpath", "/html/body/div/div[3]/div/div[2]/div[3]/div/span/span")
		diss_btn.click()
		keyboard.send("tab", do_press=True, do_release=True)
		keyboard.send("tab", do_press=True, do_release=True)
		keyboard.send("tab", do_press=True, do_release=True)
		keyboard.send("enter", do_press=True, do_release=True)
		time.sleep(2)
		keyboard.send("tab", do_press=True, do_release=True)
		keyboard.send("tab", do_press=True, do_release=True)
		keyboard.send("tab", do_press=True, do_release=True)
		keyboard.send("enter", do_press=True, do_release=True)
		time.sleep(2)
		join_btn = bot.find_element("xpath", "/html/body/div[1]/c-wiz/div/div/div[6]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/span")
		join_btn.click()




link = 'https://meet.google.com/fot-dqje-qgz'


obj = meet_bot()
obj.login("Shandonmith@gmail.com","Shadedog838")
obj.join(link)