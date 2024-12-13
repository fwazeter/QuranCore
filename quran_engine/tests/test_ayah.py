"""
Test File for Ayah Class
------------------------
This test file ensures the proper functionality of the Ayah class, including:
- Adding words to an Ayah.
- Counting total words in an Ayah.
"""

import unittest
from quran_engine.ayah import Ayah
from quran_engine.word import Word

class TestAyah(unittest.TestCase):

    def setUp(self):
        """Set up the test environment for each test case."""
        self.ayah = Ayah(1, 1, "Sample Ayah", "Sample Ayah")

    def test_word_count(self):
        """Test that word count for an Ayah is accurate."""
        self.assertEqual(self.ayah.word_count(), 0)
        word = Word(1, "Word", None, "Noun")
        self.ayah.add_word(word)
        self.assertEqual(self.ayah.word_count(), 1)
