#! /usr/bin/env python3.6

import unittest
from pencil import Pencil
from paper import Paper


class PencilTest(unittest.TestCase):

    def setUp(self):
        self.paper = Paper()

    def test_pencil_should_write_text(self):
        pencil = Pencil()

        text = "What possessed the first man to ride a horse?"
        pencil.write(self.paper, text)

        self.assertEqual(text, self.paper.read())

    def test_when_pencil_writes_additional_text_it_should_append_to_existing_text(self):
        pencil = Pencil()

        text_part_a = "I'm not the kind of man "
        text_part_b = "who can just walk into a bouncy castle."

        pencil.write(self.paper, text_part_a)
        pencil.write(self.paper, text_part_b)

        expected = text_part_a + text_part_b

        self.assertEqual(expected, self.paper.read())

    def test_when_pencil_is_completely_dull_it_should_write_spaces(self):
        pencil = Pencil(point_durability=0)
        pencil.write(self.paper, "text")
        self.assertEqual("    ", self.paper.read())

    def test_when_pencil_writes_lowercase_letters_it_should_degrade_by_one(self):
        pencil = Pencil(point_durability=2)
        pencil.write(self.paper, "text")
        self.assertEqual("te  ", self.paper.read())

    def test_when_pencil_writes_uppercase_letters_it_should_degrade_by_two(self):
        pencil = Pencil(point_durability=4)
        pencil.write(self.paper, "Text")
        self.assertEqual("Tex ", self.paper.read())

    def test_when_pencil_writes_whitespace_it_should_not_degrade(self):
        pencil = Pencil(point_durability=4)
        text = """a b 
                  c d"""
        pencil.write(self.paper, text)
        self.assertEqual(text, self.paper.read())

    """
    First off, this was definitely a bad test before since I missed adding
    in that last space to the expected string and a phenomenal catch on your part.
    
    However, I feel like the assertion you're hinting towards is something with the essence of:
    self.assertEqual(4, pencil._point)
    Which would be much simpler. I've done it this way to ensure that I'm 
    testing behaviour not implementation. If you write these tests in any other
    way then they become more brittle and would potentially require the
    tests to be rewritten in order to refactor. If a required feature was to
    get the current wear on the eraser/pencil then this would, of course, become moot.
    
    However, if indeed this is insufficient to fully test the behaviour then that's
    a grave concern. I'm not seeing that but would love an example!
    """
    def test_when_pencil_is_sharpened_it_regains_full_durability(self):
        pencil = Pencil(point_durability=4)

        pencil.write(self.paper, "text")
        pencil.sharpen()
        pencil.write(self.paper, "texts")

        self.assertEqual("texttext ", self.paper.read())

    def test_pencil_cannot_be_sharpened_past_its_length(self):
        pencil = Pencil(point_durability=1, length=2)

        for c in "text":
            pencil.write(self.paper, c)
            pencil.sharpen()

        self.assertEqual("tex ", self.paper.read())

    def test_editing_should_replace_erased_word_with_new_text(self):
        pencil = Pencil()

        pencil.write(self.paper, "An       a day keeps the doctor away")
        pencil.edit(self.paper, "onion")

        self.assertEqual("An onion a day keeps the doctor away", self.paper.read())

    def test_when_new_word_is_too_long_it_should_replace_characters_with_at_symbol(self):
        pencil = Pencil()

        pencil.write(self.paper, "An       a day keeps the doctor away")
        pencil.edit(self.paper, "artichoke")

        self.assertEqual("An artich@k@ay keeps the doctor away", self.paper.read())

    def test_when_new_word_goes_beyond_end_of_paper_it_should_be_appended_to_the_end(self):
        pencil = Pencil()

        pencil.write(self.paper, "A short phrase")
        pencil.erase(self.paper, "phrase")
        pencil.edit(self.paper, "sentence")

        self.assertEqual("A short sentence", self.paper.read())
