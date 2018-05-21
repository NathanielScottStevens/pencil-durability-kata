#! /usr/bin/env python3.6


class Paper:

    def __init__(self):
        self.text = ''

    # I'm torn between having a write/read function and
    # just using a more traditional getter
    # and setter. Somehow this seems a tad more semantic
    # though it also seems a little silly in a different light.
    # Thoughts!?
    def write(self, text):
        self.text = text

    def read(self):
        return self.text
