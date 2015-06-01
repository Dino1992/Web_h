from paste import reloader
from paste.httpserver import serve

TOP = "<div class='top'>Middleware TOP</div>"
BOTTOM =  "<div class='botton'>Middleware BOTTOM</div>"

class MiddleWareWork(object):
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        response = self.app(environ, start_response)[0]
        if response.find('<body>') >-1:
            header,body = response.split('<body>')
            data,htmlend = body.split('</body>')
            data = '<body>'+ TOP + data + BOTTOM+'</body>'
            yield header + data + htmlend
        else:
            yield TOP + response + BOTTOM
    

import os

def app(environ, start_response):
    
    path = environ['PATH_INFO']
    filePath = '.' + path  
    if not os.path.isfile(filePath):
        filePath ='./index.html' 

    fd = open(filePath,'r')
    fileContent = fd.read()

    fd.close()

    start_response('200 OK', [('Content-Type', 'text/html')])
    return [fileContent ]

app = MiddleWareWork(app)


if __name__ == '__main__':
    from paste import reloader
    from paste.httpserver import serve

    reloader.install()
    serve(app, host='127.0.0.1', port=8000)