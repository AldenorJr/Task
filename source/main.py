import json
from seleniumwire import webdriver
from seleniumwire.utils import decode

browser = webdriver.Chrome()
browser.get('https://www.google.com/maps/place/Nema+Padaria+-+Visconde+de+Piraj%C3%A1/@-22.9841517,-43.2128543,15z/data=!3m1!5s0x9bd50757e02857:0x35aa6a9b37f5d532!4m8!3m7!1s0x9bd58a0cdc1487:0x4c1eb56d62eb469b!8m2!3d-22.9841517!4d-43.2128543!9m1!1b1!16s%2Fg%2F11j20tdp78?entry=ttu')

comentarios = []
looping = True
while looping:
    for request in browser.requests:
        if request.response is not None and request.response.body is not None:
            if 'listugcposts' in request.url:
                body = decode(request.response.body, request.response.headers.get('Content-Encoding', 'identity'))
                body = body.decode('utf-8').lstrip("')]}\\n")
                data = json.loads(body)

                for elemento in data[2]:
                    author = elemento[0][1][4][1][1]
                    author_image = elemento[0][1][4][1][2]
                    date = elemento[0][1][6]
                    comentario = elemento[0][2][1][0]
                    comentarios.append({
                        'author': author,
                        'author_image': author_image,
                        'date': date,
                        'comment': comentario
                    })
                looping = False
                break
    else: continue

for comentario in comentarios:
    print(comentario)

browser.quit()