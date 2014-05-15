from threading import Thread
import logging
import datetime
from request import Request
from htmlFile import HTMLFile

logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)


class ClientThread(Thread):

    """
    Cliente
    """

    def __init__(self, clientInfo, buffer=1024):
        Thread.__init__(self)
        self.sc = clientInfo[0]
        self.addr = clientInfo[1]
        self.buffer = buffer

    def run(self):

        request = Request(self.sc.recv(self.buffer).decode())
        if request.esValida():
            logging.debug(
                'Request Method: %s, URL: %s', request.request, request.url)
            if request.request == 'GET':
                response = self.peticionGet(request.url)
                self.sc.send(response.encode())
            elif request.request == 'POST':
                pass

        self.sc.close()

    def peticionGet(self, url):

        f = HTMLFile(url[1:])
        if f.valida():
            response = 'HTTP/1.1 200 OK\n'
            response += 'Content-Type: text/html\n'
            response += '\n'
            response += f.leer()
            return response
        else:
            logging.error(f.error)
            return 'HTTP/1.1 404 OK\n'

    def printConsole(self, mensaje):
        """
        Imprime una cadena por la consola
        """

        now = datetime.datetime.today()
        print(now.strftime("%m/%d/%Y %I:%M:%S"), mensaje, sep=' : ')
