import logging

logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)


class HTMLFile(object):

    """
    docstring for HTMLFile
    """

    def __init__(self, nombre):
        self.nombre = nombre

    def valida(self):
        try:
            self.f = open(self.nombre, 'r')
        except IOError as e:
            self.error = str(e)
            return False

        return True

    def leer(self):
        return self.f.read()
