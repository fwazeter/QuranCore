"""
Test File for Root Class
------------------------
This test file ensures the proper functionality of the Root class, including:
- Verifying correct root structure.
- Testing getter and setter methods.
- Ensuring proper serialization and deserialization of Root instances.

To run tests, go to QuranCore directory and run this command:
    python -m unittest discover -s quran_engine/tests -p "test_root.py"
"""

import unittest
import logging
from unittest.mock import MagicMock
from quran_engine.root import Root

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class TestRoot(unittest.TestCase):
    """
    **TestRoot** tests the **Root class** to ensure that its methods behave as expected.

    **Attributes:**
        root (Root): An instance of the Root class being tested.
    """

    def setUp(self):
        """
        **Setup method for TestRoot.**

        **Purpose:**
        Initializes an instance of the Root being tested.

        **Attributes:**
            self.root (Root): An instance of the Root class being tested.
        """
        self.root = Root('ر ح م', 'mercy')
        logging.info('Setup complete for Root with text: %s and meaning: %s', self.root.get_text(), self.root.get_meaning())

    def test_getters_and_setters(self):
        """
        **Test for the getters and setters of the Root class.**

        **Purpose:**
        Verifies that the getters and setters for text and meaning are working as expected.

        **Process:**
            1. Set new values for text and meaning.
            2. Use the corresponding getters to retrieve the values.
            3. Assert that the retrieved values match the set values.

        **Attributes:**
            new_text (str): The new root text to be set.
            new_meaning (str): The new meaning of the root to be set.
        """
        new_text = 'ك ت ب'
        new_meaning = 'writing'

        self.root.set_text(new_text)
        logging.info('Testing set_text and get_text with value "%s"', new_text)
        self.assertEqual(self.root.get_text(), new_text)

        self.root.set_meaning(new_meaning)
        logging.info('Testing set_meaning and get_meaning with value "%s"', new_meaning)
        self.assertEqual(self.root.get_meaning(), new_meaning)

    def test_to_dict(self):
        """
        **Test for the to_dict method of the Root class.**

        **Purpose:**
        Ensures that the Root instance can be serialized into a dictionary.

        **Process:**
            1. Call the to_dict method on the Root instance.
            2. Assert that the resulting dictionary contains the correct keys and structure.

        **Attributes:**
            root_dict (dict): The serialized dictionary representation of the Root.
        """
        root_dict = self.root.to_dict()
        logging.info('Testing to_dict method for Root: %s', root_dict)

        expected = {'text': 'ر ح م', 'meaning': 'mercy'}
        self.assertEqual(root_dict, expected)

    def test_set_text_with_none(self):
        """
        **Test for set_text when the input is None.**

        **Purpose:**
        Ensures that setting the root text to None does not cause errors and is converted to an empty string.

        **Process:**
            1. Call set_text with None.
            2. Assert that the root text is set to an empty string.

        **Attributes:**
            root_text (str): The root text to be set.
        """
        self.root.set_text(None)
        logging.info('Testing set_text with None, expected empty string')
        self.assertEqual(self.root.get_text(), '')

    def test_set_meaning_with_none(self):
        """
        **Test for set_meaning when the input is None.**

        **Purpose:**
        Ensures that setting the root meaning to None does not cause errors and is converted to an empty string.

        **Process:**
            1. Call set_meaning with None.
            2. Assert that the root meaning is set to an empty string.

        **Attributes:**
            root_meaning (str): The root meaning to be set.
        """
        self.root.set_meaning(None)
        logging.info('Testing set_meaning with None, expected empty string')
        self.assertEqual(self.root.get_meaning(), '')


if __name__ == '__main__':
    unittest.main()
