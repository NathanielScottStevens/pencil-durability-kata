class Pencil:

    def __init__(self, point_durability=100, eraser_durability=100, length=5):
        self.point_durability = point_durability
        self.eraser_durability = eraser_durability
        self.length = length

        self._paper = ""
        self._eraser = eraser_durability
        self._point = point_durability

    def write(self, text):
        for character in text:
            if self._point > 0:
                self._paper += character
                self._dull_point(character)
            else:
                self._paper += ' '

    def _dull_point(self, character):
        if character.islower():
            self._point -= 1
        elif character.isupper():
            self._point -= 2

    def read(self):
        return self._paper

    def erase(self, text):
        partition = self._paper.rpartition(text)
        erased_text = ''

        for character in reversed(text):
            if self.eraser_durability > 0:
                erased_text = ' ' + erased_text
                self.eraser_durability -= 1
            else:
                erased_text = character + erased_text

        self._paper = partition[0] + erased_text + partition[2]

    def sharpen(self):
        if self.length > 0:
            self._point = self.point_durability

        self.length -= 1




