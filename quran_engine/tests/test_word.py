"""
Test File for Word Class
------------------------
This test file ensures the proper functionality of the Word class, including:
- Calculating gematric value for words.
- Ensuring proper serialization and deserialization of Word instances.
- Verifying correct usage of getters and setters.

To run tests, go to QuranCore directory and run this command:
    python -m unittest discover -s quran_engine/tests -p "test_word.py"
"""

import unittest
import logging
from unittest.mock import MagicMock
from quran_engine.word import Word
from quran_engine.root import Root

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class TestWord(unittest.TestCase):
    """
    **TestWord** tests the **Word class** to ensure that its methods behave as expected.

    **Attributes:**
        word (Word): An instance of the Word class being tested.
        root (Root): A mock instance of the Root class associated with the Word.
    """

    def setUp(self):
        """
        **Setup method for TestWord.**

        **Purpose:**
        Initializes mock dependencies and an instance of the Word being tested.

        **Attributes:**
            self.word (Word): An instance of the Word class being tested.
            self.root (Root): A mock instance of the Root class associated with the Word.
        """
        self.root = Root('ر ح م', 'mercy')
        self.word = Word(1, 'رَحْمَٰنِ', self.root, 298)
        logging.info('Setup complete for Word: %s', self.word.get_text_arabic())

    def test_getters_and_setters(self):
        """
        **Test for the getters and setters of the Word class.**

        **Purpose:**
        Verifies that the getters and setters for id, text, root, and gematria are working as expected.

        **Process:**
            1. Set new values for id, Arabic text, root, and gematria.
            2. Use the corresponding getters to retrieve the values.
            3. Assert that the retrieved values match the set values.

        **Attributes:**
            new_id (int): The new id to be set.
            new_text (str): The new Arabic text to be set.
            new_gematria (int): The new gematria value to be set.
            new_root (Root): A new mock Root instance.
        """
        new_id = 2
        new_text = 'رَحِيمِ'
        new_gematria = 350
        new_root = Root('ر ح م', 'mercy')

        self.word.set_id(new_id)
        self.word.set_text_arabic(new_text)
        self.word.set_gematria(new_gematria)
        self.word.set_root(new_root)

        self.assertEqual(self.word.get_id(), new_id)
        self.assertEqual(self.word.get_text_arabic(), new_text)
        self.assertEqual(self.word.get_gematria(), new_gematria)
        self.assertEqual(self.word.get_root(), new_root)

    def test_to_dict(self):
        """
        **Test for the to_dict method of the Word class.**

        **Purpose:**
        Ensures that the Word instance can be serialized into a dictionary.

        **Process:**
            1. Call the to_dict method on the Word instance.
            2. Assert that the resulting dictionary contains the correct keys and structure.

        **Attributes:**
            word_dict (dict): The serialized dictionary representation of the Word.
        """
        word_dict = self.word.to_dict()

        self.assertIn('id', word_dict)
        self.assertIn('text_arabic', word_dict)
        self.assertIn('gematria', word_dict)
        self.assertIn('root', word_dict)

        self.assertEqual(word_dict['id'], 1)
        self.assertEqual(word_dict['text_arabic'], 'رَحْمَٰنِ')
        self.assertEqual(word_dict['gematria'], 298)
        self.assertEqual(word_dict['root']['text'], 'ر ح م')
        self.assertEqual(word_dict['root']['meaning'], 'mercy')

    def test_calculate_gematria(self):
        """
        **Test for the calculate_gematria method of the Word class.**

        **Purpose:**
        Verifies that the gematria calculation is accurate.

        **Process:**
            1. Call the calculate_gematria method on the Word instance.
            2. Assert that the calculated gematria matches the expected value.

        **Attributes:**
            calculated_gematria (int): The calculated gematria for the Arabic text.
        """
        self.word.set_text_arabic('بِسْمِ')
        calculated_gematria = self.word.calculate_gematria()
        expected_gematria = 102  # Example expected gematria for 'بِسْمِ'
        self.assertEqual(calculated_gematria, expected_gematria)

    def test_set_text_arabic_with_none(self):
        """
        **Test for set_text_arabic when the input is None.**

        **Purpose:**
        Ensures that setting the Arabic text to None does not cause errors.

        **Process:**
            1. Call set_text_arabic with None.
            2. Assert that the Arabic text is set to an empty string.

        **Attributes:**
            text_arabic (str): The Arabic text to be set.
        """
        self.word.set_text_arabic(None)
        self.assertEqual(self.word.get_text_arabic(), '')

    def test_set_text_arabic_with_empty_string(self):
        """
        **Test for set_text_arabic when the input is an empty string.**

        **Purpose:**
        Ensures that setting the Arabic text to an empty string does not cause errors.

        **Process:**
            1. Call set_text_arabic with an empty string.
            2. Assert that the Arabic text is set to an empty string.

        **Attributes:**
            text_arabic (str): The Arabic text to be set.
        """
        self.word.set_text_arabic('')
        self.assertEqual(self.word.get_text_arabic(), '')


if __name__ == '__main__':
    unittest.main()
