#! /usr/bin/env python3.6

import unittest
from pencil import Pencil
from eraser import Eraser
from paper import Paper


class EraserTest(unittest.TestCase):

    def setUp(self):
        self.paper = Paper()

    def test_when_the_word_to_be_erased_is_not_found_nothing_should_be_erased(self):
        eraser = Eraser()
        pencil = Pencil(eraser=eraser)

        text = "Nothing to erase here"
        pencil.write(self.paper, text)
        pencil.erase(self.paper, "Something")

        self.assertEqual(text, self.paper.read())

    def test_when_pencil_eraser_degrades_fully_it_should_stop_erasing(self):
        eraser = Eraser(durability=4)
        pencil = Pencil(eraser=eraser)

        pencil.write(self.paper, "I am related to Buffalo Bill")
        pencil.erase(self.paper, "Bill")
        pencil.erase(self.paper, "Buffalo")

        self.assertEqual("I am related to Buffalo     ", self.paper.read())

    def test_erasing_should_erase_opposite_direction_of_the_written_order(self):
        eraser = Eraser(durability=3)
        pencil = Pencil(eraser=eraser)

        pencil.write(self.paper, "I am related to Buffalo Bill")
        pencil.erase(self.paper, "Bill")

        self.assertEqual("I am related to Buffalo B   ", self.paper.read())


