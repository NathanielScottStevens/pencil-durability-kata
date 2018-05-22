#! /usr/bin/env python3.6

from eraser import Eraser

'''
I normally do not comment up my code based on the advice
of the clean code manifesto. However, for ease of kata review,
I'm commenting the hell out of this.

Also, please don't hear any of my comments as being confrontational
or something of the like. I'm just starved for these types of conversations
in my current job and I'm dumping it all into this kata...sorry.
'''
class Pencil:

    def __init__(self, point_durability=100, length=5, eraser=Eraser(durability=100)):
        self.point_durability = point_durability
        self.length = length
        self.eraser = eraser

        self._point = point_durability

    def write(self, paper, text):
        new_text = paper.read()

        for character in text:
            if self._point > 0:
                new_text += character
                self._dull_point(character)
            else:
                new_text += ' '

        paper.write(new_text)

    def _dull_point(self, character):
        if character.islower():
            self._point -= 1
        elif character.isupper():
            self._point -= 2

    def erase(self, paper, text):
        self.eraser.erase(paper, text)

    def sharpen(self):
        if self.length > 0:
            self._point = self.point_durability
            self.length -= 1

    def edit(self, paper, text):
        new_text = paper.read()
        edit_position = self._find_first_blank_word_position(new_text)

        for index, character in enumerate(text):
            current_edit_position = edit_position + index

            if current_edit_position >= len(new_text):
                new_text += character
            else:
                new_text = self._replace_character(new_text, character, current_edit_position)

        paper.write(new_text)

    def _find_first_blank_word_position(self, text):
        return text.index('  ') + 1

    def _replace_character(self, text, character, position):
        new_character = character

        if text[position].isalpha():
            new_character = '@'

        return text[:position] + new_character + text[position + 1:]
