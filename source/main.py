from seleniumwire import webdriver
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
        chrome_options = webdriver.ChromeOptions()

        chrome_option_list = {
            "disable-extensions",
            "disable-gpu",
            "no-sandbox",
            "headless", # for Jenkins
            "disable-dev-shm-usage", # Jenkins
            "window-size=800x600", # Jenkins
            "window-size=800,600",
            "disable-setuid-sandbox",
            "allow-insecure-localhost",
            "no-cache",
            "user-data-dir=/tmp/user-data",
            "hide-scrollbars",
            "enable-logging",
            "log-level=0",
            "single-process",
            "data-path=/tmp/data-path",
            "ignore-certificate-errors",
            "homedir=/tmp",
            "disk-cache-dir=/tmp/cache-dir",
            "start-maximized",
            "disable-software-rasterizer",
            "ignore-certificate-errors-spki-list",
            "ignore-ssl-errors",
        }
        for chrome_option in chrome_option_list:
            chrome_options.add_argument(f"--{chrome_option}")

        selenium_options = {
            "request_storage_base_dir": "/tmp", # Use /tmp to store captured data
            "exclude_hosts": ""
        }
        self.browser = webdriver.Chrome(options=chrome_options, seleniumwire_options=selenium_options)
        self.loja = Loja('', 0, 0, 0)

    def execute(self, url):
        self.browser.get(url)
        self.footer = self.browser.find_element(By.CSS_SELECTOR, '.cVwbnc')
        self.actions = ActionChains(self.browser).move_to_element_with_offset(self.footer, 0, 0).click()
        Main.databaseInit()
        looping = True
        while looping:
            Main.use_scroll(self)
            Main.handle(self)
            print(len(self.comentarios),'/',str(self.loja.avaliacoes), ' avaliações', self.loja.name)
            if (len(self.comentarios) == int(self.loja.avaliacoes) and self.loja.avaliacoes != 0) or (len(self.comentarios) >= 1091):
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
main.execute('https://www.google.com/maps/place/Partage+Mossor%C3%B3+Shopping/@-5.1718739,-37.3764656,15z/data=!4m8!3m7!1s0x7ba06b8e9b5b56d:0xf4c6bae42ae65be!8m2!3d-5.1718739!4d-37.3764656!9m1!1b1!16s%2Fg%2F11bbxjc675?entry=ttu')