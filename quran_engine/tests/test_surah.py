"""
Test File for Surah Class
-------------------------
This test file ensures the proper functionality of the Surah class, including:
- Adding Ayahs to a Surah.
- Aggregating total words in a Surah.
- Exporting the Surah to JSON.
"""

import unittest
from quran_engine.surah import Surah
from quran_engine.ayah import Ayah

class TestSurah(unittest.TestCase):

    def setUp(self):
        """Set up the test environment for each test case."""
        self.surah = Surah(1, "Al-Fatiha", 5, 7, "Meccan")

    def test_add_ayah(self):
        """Test that an Ayah can be added to the Surah."""
        ayah = Ayah(1, 1, "Sample Text", "Sample Text")
        self.surah.add_ayah(ayah)
        self.assertEqual(len(self.surah.to_dict()["ayahs"]), 1)
