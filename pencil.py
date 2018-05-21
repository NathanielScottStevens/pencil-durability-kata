#! /usr/bin/env python3.6
class Pencil:

    def __init__(self, point_durability=100, eraser_durability=100, length=5):
        self.point_durability = point_durability
        self.eraser_durability = eraser_durability
        self.length = length

        self._eraser = eraser_durability
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

    def read(self):
        return self._paper

    def erase(self, text):
        left_of_word, word, right_of_word = self._paper.rpartition(text)
        erased_text = ''

        for character in reversed(word):
            if self._eraser > 0:
                erased_text = ' ' + erased_text
                self._eraser -= 1
            else:
                erased_text = character + erased_text

        self._paper = left_of_word + erased_text + right_of_word

    def sharpen(self):
        if self.length > 0:
            self._point = self.point_durability
            self.length -= 1

    def edit(self, text):
        edit_position = self._find_first_blank_word_position(self._paper)

        for index, character in enumerate(text):
            current_edit_position = edit_position + index

            if current_edit_position >= len(self._paper):
                self._paper += character
            else:
                self._paper = self._replace_character(self._paper, character, current_edit_position)

    def _find_first_blank_word_position(self, text):
        return text.index('  ') + 1

    def _replace_character(self, text, character, position):
        new_character = character

        if text[position].isalpha():
            new_character = '@'

        return text[:position] + new_character + text[position + 1:]
