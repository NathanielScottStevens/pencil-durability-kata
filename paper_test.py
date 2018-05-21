#! /usr/bin/env python3.6

import unittest
from paper import Paper


class PaperTest(unittest.TestCase):

    def test_paper_can_be_written_to(self):
        paper = Paper()

        text = "I'm better than papyrus"
        paper.write(text)

        self.assertEqual(text, paper.read())
