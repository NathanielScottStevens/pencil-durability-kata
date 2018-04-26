import unittest
from pencil import Pencil


class PencilTest(unittest.TestCase):

    def test_should_write_text(self):
        pencil = Pencil()

        text = "What possessed the first man to ride a horse?"
        pencil.write(text)

        self.assertEqual(text, pencil.read())

    def test_when_pencil_writes_additional_text_it_should_append_to_existing_text(self):
        pencil = Pencil()

        text_part_a = "I'm not the kind of man "
        text_part_b = "who can just walk into a bouncy castle."

        pencil.write(text_part_a)
        pencil.write(text_part_b)

        expected = text_part_a + text_part_b

        self.assertEqual(expected, pencil.read())

    def test_when_pencil_is_completely_dull_it_should_write_spaces(self):
        pencil = Pencil(durability=0)
        pencil.write("text")
        self.assertEqual("    ", pencil.read())

    def test_when_pencil_writes_lowercase_letters_it_should_degrade_by_one(self):
        pencil = Pencil(durability=2)
        pencil.write("text")
        self.assertEqual("te  ", pencil.read())

    def test_when_pencil_writes_uppercase_letters_it_should_degrade_by_two(self):
        pencil = Pencil(durability=4)
        pencil.write("Text")
        self.assertEqual("Tex ", pencil.read())

    def test_when_pencil_writes_whitespace_it_should_not_degrade(self):
        pencil = Pencil(durability=14)
        text = """text on 
                  two lines"""
        pencil.write(text)
        self.assertEqual(text, pencil.read())


