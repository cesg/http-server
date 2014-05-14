import socket
import logging

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)


class Cliente(object):

    """
    Cliente para enviar peticiones http a un servidor
    """

    def __init__(self, host='', port=80):
        self.host = host
        self.port = port

    def start(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, int(self.port)))

    def menu(self):
        """
        Muestra el menu por la consola.
        """

        print('# Ingrese una opción')
        print('1) GET')
        print('0) EXIT')
        op = -1

        # while op == -1:
        try:
            op = int(input(': '))
            logging.debug(op)
            if op == 1:
                self.valida('GET', input('URL: http://'))
                # break
            else:
                print('Opción no valida')
        except ValueError:
            print('Opción no valida')

    def valida(self, method, url):
        """
        Valida la url a consultar al servidor.
        """

        logging.debug(
            'sending request, Method: %s, URL: %s', method, url)
        if url.find(':') != -1:
            self.port = url[url.find(':')+1:url.index('/')]
            self.host = url[:url.index(':')]
        else:
            self.host = url[:url.index('/')]

        self.resource = url[url.index('/'):]
        logging.debug('HOST: %s', self.host)
        logging.debug('PORT: %s', self.port)
        try:
            self.start()
            self.formato(method)
        except ConnectionRefusedError:
            print('Imposible conectar al servidor')

    def formato(self, method):
        """
        Da formato HTTP a la petición a enviar al servidor.
        """

        requestFormat = '{0} {1} HTTP/1.1'.format(method, self.resource)
        logging.debug(requestFormat)
        self.enviar(requestFormat.encode())

    def enviar(self, msg):
        """
        Envía el mensaje al servidor.
        """

        # if self.sock:
        self.sock.send(msg)
        response = self.sock.recv(1024).decode()
        logging.debug(response)

cliente = Cliente()
cliente.menu()
