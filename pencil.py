class Pencil:

    def __init__(self, durability=100):
        self.paper = ""
        self.durability = durability
        self.point = durability

    def write(self, text):
        for c in text:
            if self.point > 0:
                self.paper += c
                self.point -= 1
            else:
                self.paper += ' '

    def read(self):
        return self.paper