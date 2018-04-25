class Pencil:

    def __init__(self):
        self.paper = ""

    def write(self, text):
        self.paper += text

    def read(self):
        return self.paper