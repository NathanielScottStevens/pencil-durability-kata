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
        pencil = Pencil(point_durability=0)
        pencil.write("text")
        self.assertEqual("    ", pencil.read())

    def test_when_pencil_writes_lowercase_letters_it_should_degrade_by_one(self):
        pencil = Pencil(point_durability=2)
        pencil.write("text")
        self.assertEqual("te  ", pencil.read())

    def test_when_pencil_writes_uppercase_letters_it_should_degrade_by_two(self):
        pencil = Pencil(point_durability=4)
        pencil.write("Text")
        self.assertEqual("Tex ", pencil.read())

    def test_when_pencil_writes_whitespace_it_should_not_degrade(self):
        pencil = Pencil(point_durability=14)
        text = """text on 
                  two lines"""
        pencil.write(text)
        self.assertEqual(text, pencil.read())

    def test_when_pencil_is_sharpened_it_regains_full_durability(self):
        pencil = Pencil(point_durability=4)

        pencil.write("text")
        pencil.sharpen()
        pencil.write("text")

        self.assertEqual("texttext", pencil.read())

    def test_pencil_cannot_be_sharpened_past_its_length(self):
        pencil = Pencil(point_durability=1, length=2)

        for c in "text":
            pencil.write(c)
            pencil.sharpen()

        self.assertEqual("tex ", pencil.read())

    def test_when_pencil_erases_it_should_remove_last_occurrence_of_word(self):
        pencil = Pencil()

        pencil.write("I say I say I say how can you say that")
        pencil.erase("say")

        self.assertEqual("I say I say I say how can you     that", pencil.read())

    def test_when_pencil_eraser_degrades_fully_it_should_stop_erasing(self):
        pencil = Pencil(eraser_durability=4)

        pencil.write("I am related to Buffalo Bill")
        pencil.erase("Bill")
        pencil.erase("Buffalo")

        self.assertEqual("I am related to Buffalo     ", pencil.read())

    def test_erasing_should_erase_opposite_of_the_written_order(self):
        pencil = Pencil(eraser_durability=3)

        pencil.write("I am related to Buffalo Bill")
        pencil.erase("Bill")

        self.assertEqual("I am related to Buffalo B   ", pencil.read())
