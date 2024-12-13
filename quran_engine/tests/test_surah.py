"""
Test File for Surah Class
-------------------------
This test file ensures the proper functionality of the Surah class, including:
- Adding Ayahs to a Surah.
- Aggregating total words in a Surah.
- Exporting the Surah to JSON.

To run tests, go to QuranCore directory and run this command:
    python -m unittest discover -s quran_engine/tests -p "test_surah.py"
"""
import unittest
import logging
from unittest.mock import MagicMock
from quran_engine.surah import Surah

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class TestSurah(unittest.TestCase):
    """
    **TestSurah** tests the **Surah class** to ensure that its methods behave as expected.

    **Attributes:**
        mock_ayah (MagicMock): A mock version of the Ayah class.
        surah (Surah): An instance of the Surah class being tested.
    """

    def setUp(self):
        """
        **Setup method for TestSurah.**

        **Purpose:**
        Initializes mock dependencies and an instance of the Surah being tested.

        **Attributes:**
            self.mock_ayah (MagicMock): A mock version of the Ayah class.
            self.surah (Surah): An instance of the Surah class being tested.
        """
        self.mock_ayah = MagicMock()
        self.surah = Surah(1, 'Al-Fatiha', 1, 7, 'Meccan', self.mock_ayah)
        logging.info('Setup complete for Surah: %s', self.surah.get_name())

    def test_getters_and_setters(self):
        """
        **Test for the getters and setters of the Surah class.**

        **Purpose:**
        Verifies that the getters and setters for id, name, and classification are working as expected.

        **Process:**
            1. Set new values for id, name, and classification.
            2. Use the corresponding getters to retrieve the values.
            3. Assert that the retrieved values match the set values.

        **Attributes:**
            new_id (int): The new id to be set.
            new_name (str): The new name to be set.
            new_classification (str): The new classification to be set.
        """
        new_id = 2
        new_name = 'Al-Baqara'
        new_classification = 'Medinan'

        self.surah.set_id(new_id)
        self.assertEqual(self.surah.get_id(), new_id)

        self.surah.set_name(new_name)
        self.assertEqual(self.surah.get_name(), new_name)

        self.surah.set_classification(new_classification)
        self.assertEqual(self.surah.get_classification(), new_classification)

    def test_add_and_get_ayahs(self):
        """
        **Test for the add_ayah and get_ayahs methods of the Surah class.**

        **Purpose:**
        Verifies that Ayahs can be added and retrieved properly.

        **Process:**
            1. Create a mock Ayah object.
            2. Add the mock Ayah to the Surah.
            3. Retrieve the list of Ayahs from the Surah.
            4. Assert that the Ayah appears in the list.

        **Attributes:**
            mock_ayah (MagicMock): A mock instance of an Ayah object.
        """
        mock_ayah = self.mock_ayah()
        self.surah.add_ayah(mock_ayah)
        self.assertIn(mock_ayah, self.surah.get_ayahs())

    def test_total_word_count(self):
        """
        **Test for the total_word_count method of the Surah class.**

        **Purpose:**
        Verifies that the total word count for all Ayahs in the Surah is calculated correctly.

        **Process:**
            1. Create mock Ayah objects with a word_count method that returns a known value.
            2. Add these Ayahs to the Surah.
            3. Call the total_word_count method.
            4. Assert that the total word count matches the expected value.

        **Attributes:**
            mock_ayah1 (MagicMock): A mock instance of an Ayah with a known word count.
            mock_ayah2 (MagicMock): Another mock instance of an Ayah with a known word count.
        """
        mock_ayah1 = MagicMock()
        mock_ayah2 = MagicMock()
        mock_ayah1.word_count.return_value = 5
        mock_ayah2.word_count.return_value = 3

        self.surah.add_ayah(mock_ayah1)
        self.surah.add_ayah(mock_ayah2)

        total_count = self.surah.total_word_count()
        self.assertEqual(total_count, 8)

    def test_to_dict(self):
        """
        **Test for the to_dict method of the Surah class.**

        **Purpose:**
        Ensures that the Surah instance can be serialized into a dictionary.

        **Process:**
            1. Add a mock Ayah with a to_dict method to the Surah.
            2. Call the to_dict method on the Surah instance.
            3. Assert that the resulting dictionary contains the correct keys and structure.

        **Attributes:**
            mock_ayah (MagicMock): A mock instance of an Ayah object with a to_dict method.
        """
        mock_ayah = self.mock_ayah()
        mock_ayah.to_dict.return_value = {'position': 1,
                                          'text_arabic': 'بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ'}

        self.surah.add_ayah(mock_ayah)
        surah_dict = self.surah.to_dict()

        self.assertIn('id', surah_dict)
        self.assertIn('name', surah_dict)
        self.assertIn('ayahs', surah_dict)
        self.assertEqual(len(surah_dict['ayahs']), 1)


if __name__ == '__main__':
    unittest.main()
