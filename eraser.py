#! /usr/bin/env python3.6

"""
I'm tempted to create a parent class for
pencil and eraser since they share the trait
of being degradable. If they both could be
sharpened I think this would be the right call
but, as is, I think it would complicate the code
without benefit.
"""
class Eraser:

    def __init__(self, durability=100):
        self.durability = durability
        self._remaining_eraser = durability

    def erase(self, paper, text):
        text_on_paper = paper.read()
        left_of_word, word, right_of_word = text_on_paper.rpartition(text)
        erased_text = ''

        for character in reversed(word):
            if self._remaining_eraser > 0:
                erased_text = ' ' + erased_text
                self._remaining_eraser -= 1
            else:
                erased_text = character + erased_text

        text = left_of_word + erased_text + right_of_word
        paper.write(text)


