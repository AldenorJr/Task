from seleniumwire.utils import decode
import json
from models.LojaModel import Loja

class LojaController:
    def execute(request):
        body = decode(request.response.body, request.response.headers.get('Content-Encoding', 'identity'))
        body = body.decode('utf-8').lstrip(")]}'\n")
        data = json.loads(body)
        avaliacoes = data[6][4][8]
        nota = data[6][4][7]
        name = data[6][11]
        loja = Loja(name, nota, avaliacoes)
        return loja