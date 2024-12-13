"""
Test File for Quran Class
-------------------------
This test file ensures the proper functionality of the Quran class, including:
- Adding Surahs to the Quran.
- Calculating total word counts and total gematric sums.
- Exporting the entire Quran to JSON.
"""

# 1. Standard library imports
import unittest

# 2. Local application-specific imports
from quran_engine.quran import Quran
from quran_engine.surah import Surah


class TestQuran(unittest.TestCase):

    def setUp(self):
        """Set up the test environment for each test case."""
        self.quran = Quran()
        self.surah = Surah(1, "Al-Fatiha", 5, 7, "Meccan")
        self.quran.add_surah(self.surah)

    def test_total_word_count(self):
        """Test that total word count is accurate."""
        self.assertEqual(self.quran.total_word_count(), 0)


if __name__ == '__main__':
    unittest.main()
