class Pencil:

    def __init__(self, durability=100, length=5):
        self.paper = ""
        self.durability = durability
        self.point = durability
        self.length = length

    def _dull_point(self, character):
        if character.islower():
            self.point -= 1
        elif character.isupper():
            self.point -= 2

    def write(self, text):
        for character in text:
            if self.point > 0:
                self.paper += character
                self._dull_point(character)
            else:
                self.paper += ' '

    def read(self):
        return self.paper

    def sharpen(self):
        if self.length > 0:
            self.point = self.durability

        self.length -= 1
