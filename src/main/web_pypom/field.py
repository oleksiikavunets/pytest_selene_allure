class Field:

    def __init__(self, el):
        self.el = el


    def send_keys(self, string):
        self.el.send_keys(string)