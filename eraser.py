#! /usr/bin/env python3.6


class Eraser:

    def __init__(self, durability=100):
        self.durability = durability
        self._eraser = durability

    def erase(self, paper, text):
        left_of_word, word, right_of_word = paper.read().rpartition(text)
        erased_text = ''

        for character in reversed(word):
            if self._eraser > 0:
                erased_text = ' ' + erased_text
                self._eraser -= 1
            else:
                erased_text = character + erased_text

        text = left_of_word + erased_text + right_of_word
        paper.write(text)


