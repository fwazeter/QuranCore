"""
Test File for GematriaEngine Class
----------------------------------
This test file ensures the proper functionality of the GematriaEngine class, including:
- Calculating gematric value for Arabic words.
- Handling special cases such as None or empty text.

To run tests, go to QuranCore directory and run this command:
    python -m unittest discover -s quran_engine/tests -p "test_gematria_engine.py"
"""

import unittest
import logging
from quran_engine.gematria_engine import GematriaEngine

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class TestGematriaEngine(unittest.TestCase):
    """
    **TestGematriaEngine** tests the **GematriaEngine class** to ensure that its methods behave as expected.

    **Attributes:**
        gematria_engine (GematriaEngine): An instance of the GematriaEngine class being tested.
    """

    def setUp(self):
        """
        **Setup method for TestGematriaEngine.**

        **Purpose:**
        Initializes an instance of the GematriaEngine being tested.

        **Attributes:**
            self.gematria_engine (GematriaEngine): An instance of the GematriaEngine class being tested.
        """
        self.gematria_engine = GematriaEngine()
        logging.info('Setup complete for GematriaEngine')

    def test_calculate_gematria(self):
        """
        **Test for the calculate_gematria method of the GematriaEngine class.**

        **Purpose:**
        Verifies that the gematria calculation is accurate for a simple Arabic word.

        **Process:**
            1. Call the calculate_gematria method with a known Arabic text.
            2. Assert that the calculated gematria matches the expected value.

        **Attributes:**
            input_text (str): The Arabic text for which the gematria is calculated.
            calculated_gematria (int): The calculated gematria for the Arabic text.
            expected_gematria (int): The expected gematria value.
        """
        input_text = 'بسم'
        calculated_gematria = self.gematria_engine.calculate_gematria(input_text)
        expected_gematria = 102  # Example gematria value for 'بسم'
        logging.info('Testing calculate_gematria for input "%s", expected: %d, calculated: %d', input_text, expected_gematria, calculated_gematria)
        self.assertEqual(calculated_gematria, expected_gematria)

    def test_calculate_gematria_empty_string(self):
        """
        **Test for the calculate_gematria method with an empty string.**

        **Purpose:**
        Verifies that the gematria calculation returns 0 for an empty string.

        **Process:**
            1. Call the calculate_gematria method with an empty string.
            2. Assert that the result is 0.

        **Attributes:**
            calculated_gematria (int): The calculated gematria for an empty string.
        """
        calculated_gematria = self.gematria_engine.calculate_gematria('')
        logging.info('Testing calculate_gematria with empty string, expected: 0, calculated: %d', calculated_gematria)
        self.assertEqual(calculated_gematria, 0)

    def test_calculate_gematria_none(self):
        """
        **Test for the calculate_gematria method with None as input.**

        **Purpose:**
        Verifies that the gematria calculation returns 0 when None is passed.

        **Process:**
            1. Call the calculate_gematria method with None.
            2. Assert that the result is 0.

        **Attributes:**
            calculated_gematria (int): The calculated gematria for None input.
        """
        calculated_gematria = self.gematria_engine.calculate_gematria(None)
        logging.info('Testing calculate_gematria with None input, expected: 0, calculated: %d', calculated_gematria)
        self.assertEqual(calculated_gematria, 0)

    def test_calculate_gematria_with_special_characters(self):
        """
        **Test for the calculate_gematria method with special characters in the text.**

        **Purpose:**
        Verifies that non-Arabic characters are ignored in the gematria calculation.

        **Process:**
            1. Call the calculate_gematria method with a string containing special characters.
            2. Assert that only the gematria of valid Arabic characters is included.

        **Attributes:**
            input_text (str): The Arabic text with special characters.
            calculated_gematria (int): The calculated gematria for the Arabic text.
            expected_gematria (int): The expected gematria value.
        """
        input_text = 'بِسْم123'
        calculated_gematria = self.gematria_engine.calculate_gematria(input_text)
        expected_gematria = 102  # Only the Arabic characters should be considered
        logging.info('Testing calculate_gematria with input "%s", expected: %d, calculated: %d', input_text, expected_gematria, calculated_gematria)
        self.assertEqual(calculated_gematria, expected_gematria)

    def test_calculate_gematria_with_full_ayah(self):
        """
        **Test for the calculate_gematria method with a full ayah.**

        **Purpose:**
        Verifies that the gematria calculation works correctly for a complete ayah.

        **Process:**
            1. Call the calculate_gematria method with an Arabic ayah.
            2. Assert that the gematria is calculated correctly for all characters.

        **Attributes:**
            input_text (str): The Arabic text of the ayah.
            calculated_gematria (int): The calculated gematria for the ayah.
            expected_gematria (int): The expected gematria value.
        """
        input_text = 'بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ'
        calculated_gematria = self.gematria_engine.calculate_gematria(input_text)
        expected_gematria = 786  # Example gematria value for 'بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ'
        logging.info('Testing calculate_gematria for ayah "%s", expected: %d, calculated: %d', input_text, expected_gematria, calculated_gematria)
        self.assertEqual(calculated_gematria, expected_gematria)


if __name__ == '__main__':
    unittest.main()
