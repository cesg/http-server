import configparser
import logging
import socket
from clientThread import ClientThread

logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)


class Server(object):

    """
    docstring for Server
    """

    def __init__(self):
        super(Server, self).__init__()
        config = configparser.ConfigParser()
        config.read('server.conf')
        self.host = config['CONFIG']['host']
        self.port = int(config['CONFIG']['port'])
        self.max_conect = int(config['CONFIG']['max'])

    def start(self):
        logging.debug(
            'Server iniciado HOST: %s , PORT: %s', self.host, self.port)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.host, self.port))
        self.sock.listen(self.max_conect)
        logging.debug('esperando conexiones...')

        while True:
            clientInfo = self.sock.accept()
            logging.debug('cliente conectado desde %s', clientInfo[1])
            client = ClientThread(clientInfo)
            client.start()
        self.sock.close()


try:
    server = Server()
    server.start()
except Exception as e:
    logging.exception(e)
