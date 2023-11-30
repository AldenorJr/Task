from seleniumwire.utils import decode
import json
from models.ComentarioModel import Comentario

class ComentarioController:
    def execute(request, loja_id):
        body = decode(request.response.body, request.response.headers.get('Content-Encoding', 'identity'))
        body = body.decode('utf-8').lstrip("')]}\\n")
        data = json.loads(body)
        comentarios = []
        for elemento in data[2]:
            author = elemento[0][1][4][1][1]
            author_image = elemento[0][1][4][1][2]
            date = elemento[0][1][6]
            comment = ''
            language = ''
            try:
                comment = elemento[0][2][1][0]
                language = elemento[0][2][1][1]
            except:
                comment = ''
                language = ''
            avalation = elemento[0][2][0][0]
            comentario = Comentario(author, author_image, avalation, comment, language, loja_id, date, 0)
            comentarios.append(comentario)
        return comentarios