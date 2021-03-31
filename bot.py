from selenium import webdriver
from selenium.webdriver.common.keys import keys
import time
import random

class Instagrambot:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.drive = webdrive.Firefox(executable_path="C:\Users\DANIEL SANTOS\Documents\geckodriver.exe")) 

    def login(self):
        drive = self.drive
        drive.get("https://www.instagram.com")

Dany = Instagrambot("98992055321","dany781@")
Dany.login()
