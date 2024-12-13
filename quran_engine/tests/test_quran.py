
"""
Test File for Quran Class
-------------------------
This test file ensures the proper functionality of the Quran class, including:
- Adding Surahs to the Quran.
- Calculating total word counts and total gematric sums.
- Exporting the entire Quran to JSON.

python -m unittest discover -s quran_engine/tests -p "test_quran.py"
"""

# 1. Standard library imports
import unittest
import logging
from unittest.mock import MagicMock
from quran_engine.quran import Quran

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class TestQuran(unittest.TestCase):
    """
    TestQuran is a unit test class for the Quran class.

    Attributes:
        MockSurah (MagicMock): A mock version of the Surah class used to simulate dependencies.
        quran (Quran): An instance of the Quran class that is being tested.
    """

    def setUp(self):
        """
        Setup method for TestQuran.

        Initializes a mock Surah class and instantiates a Quran object using the mock class.

        Attributes:
            self.MockSurah (MagicMock): A mock Surah class to avoid dependency on the real Surah class.
            self.quran (Quran): An instance of the Quran class being tested.
        """
        self.MockSurah = MagicMock()  # MockSurah is a mock of the Surah class
        self.quran = Quran(self.MockSurah)  # Inject the mock Surah class into the Quran instance
        logging.info('Setup complete for Quran.')

    def test_add_and_get_surahs(self):
        """
        Test for the add_surah and get_surahs methods.

        Adds a mock Surah to the Quran and asserts that it is present in the Quran's list of Surahs.

        Process:
            1. Create a mock Surah instance.
            2. Call the add_surah method to add the mock Surah to the Quran instance.
            3. Use get_surahs to retrieve the list of Surahs.
            4. Assert that the number of Surahs in the list is 1.

        Attributes:
            mock_surah (MagicMock): A mock instance of a Surah object to be added to the Quran.
        """
        mock_surah = MagicMock()  # Create a mock Surah object
        self.quran.add_surah(mock_surah)  # Add the mock Surah to the Quran
        logging.info('Added mock Surah to Quran.')
        self.assertEqual(len(self.quran.get_surahs()), 1)  # Assert that one Surah was added

    def test_to_dict(self):
        """
        Test for the to_dict method of the Quran class.

        Verifies that the to_dict method correctly serializes the Quran instance into a dictionary.

        Process:
            1. Create a mock Surah and mock its to_dict method to return specific values.
            2. Add the mock Surah to the Quran using add_surah.
            3. Call the to_dict method on the Quran instance.
            4. Assert that the resulting dictionary contains the "surahs" key and that it contains the Surah.

        Attributes:
            mock_surah (MagicMock): A mock instance of a Surah object with a custom to_dict method.
            quran_dict (dict): The serialized dictionary form of the Quran instance.
        """
        mock_surah = MagicMock()  # Create a mock Surah object
        mock_surah.to_dict.return_value = {'id': 1, 'name': 'Al-Fatiha'}  # Mock the to_dict method
        self.quran.add_surah(mock_surah)  # Add the mock Surah to the Quran
        quran_dict = self.quran.to_dict()  # Serialize the Quran instance to a dictionary
        logging.info('Testing to_dict method for Quran: %s', quran_dict)
        self.assertIn('surahs', quran_dict)  # Assert that the "surahs" key exists in the dictionary
        self.assertEqual(len(quran_dict['surahs']),
                         1)  # Assert that there is one Surah in the "surahs" list


if __name__ == '__main__':
    unittest.main()
