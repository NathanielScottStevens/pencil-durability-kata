import unittest
from pencil import Pencil


class PencilTest(unittest.TestCase):

    def test_writes_text(self):
        pencil = Pencil()

        text = "What possessed the first man to ride a horse?"
        pencil.write(text)

        self.assertEqual(text, pencil.read())


