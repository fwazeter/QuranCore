"""
Test File for Ayah Class
------------------------
This test file ensures the proper functionality of the Ayah class, including:
- Adding words to an Ayah.
- Counting total words in an Ayah.

To run tests, go to QuranCore directory and run this command:
    python -m unittest discover -s quran_engine/tests -p "test_ayah.py"

"""
import unittest
import logging
from unittest.mock import MagicMock
from quran_engine.ayah import Ayah

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class TestAyah(unittest.TestCase):
    """
    **TestAyah** tests the **Ayah class** to ensure that its methods behave as expected.

    **Attributes:**
        ayah (Ayah): An instance of the Ayah class being tested.
    """

    def setUp(self):
        """
        **Setup method for TestAyah.**

        **Purpose:**
        Initializes an instance of the Ayah being tested.

        **Attributes:**
            self.ayah (Ayah): An instance of the Ayah class being tested.
        """
        self.ayah = Ayah(1, 1, 'بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ', 'Bismillah',
                         'In the name of Allah')
        logging.info('Setup complete for Ayah: %s', self.ayah.get_text_arabic())

    def test_getters_and_setters(self):
        """
        **Test for the getters and setters of the Ayah class.**

        **Purpose:**
        Verifies that the getters and setters for id, position, text, and translation are working as expected.

        **Process:**
            1. Set new values for id, position, Arabic text, sanitized text, and translation.
            2. Use the corresponding getters to retrieve the values.
            3. Assert that the retrieved values match the set values.

        **Attributes:**
            new_id (int): The new id to be set.
            new_position (int): The new position to be set.
            new_text (str): The new Arabic text to be set.
            new_sanitized_text (str): The new sanitized text to be set.
            new_translation (str): The new translation to be set.
        """
        new_id = 2
        new_position = 2
        new_text = 'الحمد لله رب العالمين'
        new_sanitized_text = 'Alhamdu lillahi rabbil alameen'
        new_translation = 'All praise is due to Allah, the Lord of all that exists'

        self.ayah.set_id(new_id)
        self.ayah.set_position(new_position)
        self.ayah.set_text_arabic(new_text)
        self.ayah.set_sanitized_text(new_sanitized_text)
        self.ayah.set_translation(new_translation)

        self.assertEqual(self.ayah.get_id(), new_id)
        self.assertEqual(self.ayah.get_position(), new_position)
        self.assertEqual(self.ayah.get_text_arabic(), new_text)
        self.assertEqual(self.ayah.get_sanitized_text(), new_sanitized_text)
        self.assertEqual(self.ayah.get_translation(), new_translation)

    def test_word_count(self):
        """
        **Test for the word_count method of the Ayah class.**

        **Purpose:**
        Verifies that the word count for the Ayah is calculated correctly.

        **Process:**
            1. Call the word_count method on the Ayah instance.
            2. Assert that the number of words in the Arabic text matches the expected count.

        **Attributes:**
            word_count (int): The total count of words in the Ayah.
        """
        self.ayah.set_text_arabic('هذا اختبار بسيط')
        self.assertEqual(self.ayah.word_count(), 3)

    def test_word_count_empty_text(self):
        """
        **Test for the word_count method when the Arabic text is empty.**

        **Purpose:**
        Ensures that the word count method returns 0 for an empty string.

        **Process:**
            1. Set the Arabic text of the Ayah to an empty string.
            2. Call the word_count method and assert that the count is 0.

        **Attributes:**
            word_count (int): The word count of the empty Arabic text.
        """
        self.ayah.set_text_arabic('')
        self.assertEqual(self.ayah.word_count(), 0)

    def test_word_count_none_text(self):
        """
        **Test for the word_count method when the Arabic text is None.**

        **Purpose:**
        Ensures that the word count method returns 0 when the Arabic text is None.

        **Process:**
            1. Set the Arabic text of the Ayah to None.
            2. Call the word_count method and assert that the count is 0.

        **Attributes:**
            word_count (int): The word count of the None Arabic text.
        """
        self.ayah.set_text_arabic(None)  # Set Arabic text to None
        word_count = self.ayah.word_count()  # Call word count method
        self.assertEqual(word_count, 0)  # Ensure the result is 0

    def test_to_dict(self):
        """
        **Test for the to_dict method of the Ayah class.**

        **Purpose:**
        Ensures that the Ayah instance can be serialized into a dictionary.

        **Process:**
            1. Call the to_dict method on the Ayah instance.
            2. Assert that the resulting dictionary contains the correct keys and structure.

        **Attributes:**
            ayah_dict (dict): The serialized dictionary representation of the Ayah.
        """
        ayah_dict = self.ayah.to_dict()

        self.assertIn('id', ayah_dict)
        self.assertIn('position', ayah_dict)
        self.assertIn('text_arabic', ayah_dict)
        self.assertIn('sanitized_text', ayah_dict)
        self.assertIn('translation', ayah_dict)

        self.assertEqual(ayah_dict['id'], 1)
        self.assertEqual(ayah_dict['position'], 1)
        self.assertEqual(ayah_dict['text_arabic'], 'بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ')
        self.assertEqual(ayah_dict['translation'], 'In the name of Allah')


if __name__ == '__main__':
    unittest.main()
