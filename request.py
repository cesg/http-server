class Request(object):

    """
    docstring for Request
    """

    def __init__(self, arg):
        # super(Request, self).__init__()
        self.arg = arg
        if self.esValida():
            self.decode()

    def decode(self):
        self.requestList = self.arg.split('\r\n')
        head = self.requestList[0].split(' ')
        self.request = head[0]
        self.url = head[1]

    def esValida(self):
        return self.arg != ''
