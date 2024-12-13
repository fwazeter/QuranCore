"""
Test File for Word Class
------------------------
This test file ensures the proper functionality of the Word class, including:
- Calculating gematric value for words.
"""

import unittest
from quran_engine.word import Word
from quran_engine.root import Root
from quran_engine.gematria_engine import GematriaEngine

class TestWord(unittest.TestCase):

    def setUp(self):
        """Set up the test environment for each test case."""
        self.word = Word(1, "بِسْمِ", Root(1, "سمو", "Exaltation"), "Noun")

    def test_gematric_value_calculation(self):
        """Test that gematric value of a word is calculated correctly."""
        expected_value = GematriaEngine.get_gematric_value("ب") + \
                         GematriaEngine.get_gematric_value("س") + \
                         GematriaEngine.get_gematric_value("م")
        self.assertEqual(self.word.get_gematric_value(), expected_value)
