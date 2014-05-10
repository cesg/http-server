from threading import Thread
import logging
import datetime
from request import Request


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
                pass
            elif request.request == 'POST':
                pass

            self.sc.send('HTTP/1.1 200 OK\n'.encode())
            self.sc.send(
                'Content-Type: text/html\n''Content-Type: text/html\n'
                .encode())
            self.sc.send('\n'.encode())
            self.sc.send('Hola mundo'.encode())
        self.sc.close()

    def printConsole(self, mensaje):
        """
        Imprime una cadena por la consola
        """

        now = datetime.datetime.today()
        print(now.strftime("%m/%d/%Y %I:%M:%S"), mensaje, sep=' : ')
