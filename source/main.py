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
        Main.databaseInit()
        looping = True
        while looping:
            time.sleep(randint(0, 3))
            Main.use_scroll(self)
            Main.handle(self)
            print(len(self.comentarios),'/',str(self.loja.avaliacoes), ' avaliações', self.loja.name)
            if (len(self.comentarios) == int(self.loja.avaliacoes) and self.loja.avaliacoes != 0) or (len(self.comentarios) == 1100):
                looping = False
                LojaDataBase.saveLoja(self.loja)
        self.browser.quit()
    def databaseInit():
        LojaDataBase.createTable()
        ComentarioDatabase.createTable()
    def handle(self):
        for request in self.browser.requests:
            if request.response is not None and request.response.body is not None:
                if '/maps/preview/place' in request.url:
                    if self.loja.name == '': 
                        self.loja = LojaController.execute(request)
                        self.comentarios = ComentarioDatabase.getComentariosByLoja(self.loja.id)
                if 'listugcposts' in request.url:
                    Main.push_comentarios(self, ComentarioController.execute(request, self.loja.id))
    
    def push_comentarios(self, comentariolista):
        for comentario in comentariolista:
            found = False
            for comentariosearch in self.comentarios:
                if comentariosearch.comment == comentario.comment and comentariosearch.author == comentario.author:
                    found = True
                    break
            if not found:
                self.comentarios.append(comentario)
                ComentarioDatabase.insertComentario(comentario)
    def use_scroll(self):
        actions = self.actions
        for _ in range(randint(7, 10)):
            actions = actions.send_keys(Keys.PAGE_DOWN)
        actions.perform()

main = Main()
time.sleep(1)
main.execute('https://www.google.com/maps/place/Nema+Padaria+-+Leblon/@-22.9850962,-43.2264946,15z/data=!4m8!3m7!1s0x9bd51fff4cc717:0x930f8a469526651c!8m2!3d-22.9852248!4d-43.2265298!9m1!1b1!16s%2Fg%2F11r_sq0mzp?entry=ttu')