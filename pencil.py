class Pencil:

    def __init__(self, durability=100):
        self.paper = ""
        self.durability = durability
        self.point = durability

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
        self.point = self.durability
