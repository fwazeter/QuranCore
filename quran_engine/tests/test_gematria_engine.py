"""
Test File for Gematria Engine
-----------------------------
This test file ensures the proper functionality of the GematriaEngine class, including:
- Gematric value lookup for individual characters.
"""

import unittest
from quran_engine.gematria_engine import GematriaEngine

class TestGematriaEngine(unittest.TestCase):

    def test_gematric_value_lookup(self):
        """Test that the gematric value lookup works correctly."""
        self.assertEqual(GematriaEngine.get_gematric_value('ب'), 2)
        self.assertEqual(GematriaEngine.get_gematric_value('ي'), 10)
        self.assertEqual(GematriaEngine.get_gematric_value('غ'), 1000)
