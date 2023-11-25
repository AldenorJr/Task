from seleniumwire import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from controller.ComentarioController import ComentarioController
from controller.LojaController import LojaController

from models.LojaModel import Loja

browser = webdriver.Chrome()
browser.get('https://www.google.com/maps/place/Nema+Padaria+-+Visconde+de+Piraj%C3%A1/@-22.9841517,-43.2128543,15z/data=!3m1!5s0x9bd50757e02857:0x35aa6a9b37f5d532!4m8!3m7!1s0x9bd58a0cdc1487:0x4c1eb56d62eb469b!8m2!3d-22.9841517!4d-43.2128543!9m1!1b1!16s%2Fg%2F11j20tdp78?entry=ttu')

looping = True
comentarios = []
loja = Loja('', 0, 0)
footer = browser.find_element(By.CSS_SELECTOR, '.cVwbnc')
actions = ActionChains(browser).move_to_element_with_offset(footer, 0, 0).click()

class Main:
    def handle():
        global loja
        for request in browser.requests:
            if request.response is not None and request.response.body is not None:
                if '/maps/preview/place' in request.url:
                    if loja.name == '': loja = LojaController.execute(request)
                if 'listugcposts' in request.url:
                    Main.push_comentarios(ComentarioController.execute(request))
    
    def push_comentarios(comentariolista):
        for comentario in comentariolista:
            found = False
            for comentariosearch in comentarios:
                if comentariosearch.comment == comentario.comment and comentariosearch.author == comentario.author:
                    found = True
                    break
            if not found:
                comentarios.append(comentario)
    def use_scroll():
        global footer
        global actions
        for _ in range(7):
            actions = actions.send_keys(Keys.PAGE_DOWN)
        actions.perform()
while looping:
    time.sleep(1)
    Main.use_scroll()
    Main.handle()
    print(len(comentarios), '/', str(loja.avaliacoes), '')
    if len(comentarios) == loja.avaliacoes and loja.avaliacoes != 0:
        looping = False

for coment in comentarios:
    print(coment.rating, ' ')
browser.quit()