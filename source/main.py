from seleniumwire import webdriver
import time
from random import randint

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from controller.ComentarioController import ComentarioController
from controller.LojaController import LojaController

from database.storage.ComentarioDatabase import ComentarioDatabase
from database.storage.LojaDatabase import LojaDataBase

from models.LojaModel import Loja

class Main:

    global comentarios
    global loja
    global actions
    global footer
    global browser

    def __init__(self):
        self.comentarios = []
        self.browser = webdriver.Chrome()
        self.loja = Loja('', 0, 0, 0)

    def execute(self, url):
        self.browser.get(url)
        self.footer = self.browser.find_element(By.CSS_SELECTOR, '.cVwbnc')
        self.actions = ActionChains(self.browser).move_to_element_with_offset(self.footer, 0, 0).click()
        Main.initDatabase()
        looping = True
        while looping:
            time.sleep(randint(0, 3))
            Main.use_scroll(self)
            Main.handle(self)
            print(len(self.comentarios),'/',str(self.loja.avaliacoes), ' avaliações', self.loja.name)
            if (len(self.comentarios) == self.loja.avaliacoes and self.loja.avaliacoes != 0) or (len(self.comentarios) == 1100):
                looping = False
                LojaDataBase.saveLoja(self.loja)
        self.browser.quit()
    def initDatabase():
        LojaDataBase.createTable()
        ComentarioDatabase.createTable()
    def handle(self):
        for request in self.browser.requests:
            if request.response is not None and request.response.body is not None:
                if '/maps/preview/place' in request.url:
                    if self.loja.name == '': self.loja = LojaController.execute(request)
                if 'listugcposts' in request.url:
                    Main.push_comentarios(self, ComentarioController.execute(request))
    
    def push_comentarios(self, comentariolista):
        for comentario in comentariolista:
            found = False
            for comentariosearch in self.comentarios:
                if comentariosearch.comment == comentario.comment and comentariosearch.author == comentario.author:
                    found = True
                    break
            if not found:
                self.comentarios.append(comentario)
    def use_scroll(self):
        actions = self.actions
        for _ in range(randint(7, 10)):
            actions = actions.send_keys(Keys.PAGE_DOWN)
        actions.perform()

main = Main()
time.sleep(1)
main.execute('https://www.google.com/maps/place/Nema+Padaria+-+Visconde+de+Piraj%C3%A1/@-22.9841517,-43.2128543,15z/data=!3m1!5s0x9bd50757e02857:0x35aa6a9b37f5d532!4m8!3m7!1s0x9bd58a0cdc1487:0x4c1eb56d62eb469b!8m2!3d-22.9841517!4d-43.2128543!9m1!1b1!16s%2Fg%2F11j20tdp78?entry=ttu')