"""
Test File for Root Class
------------------------
This test file ensures the proper functionality of the Root class, including:
- Verifying correct root structure.
"""

import unittest
from quran_engine.root import Root

class TestRoot(unittest.TestCase):

    def setUp(self):
        """Set up the test environment for each test case."""
        self.root = Root(1, "سمو", "Exaltation")

    def test_root_structure(self):
        """Test that the root structure is properly formed."""
        self.assertEqual(self.root.to_dict()["text_arabic"], "سمو")
