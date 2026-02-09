"""
Tests for GALIB-Dev package.
"""

import unittest
import sys
import os

# Add parent directory to path to import galib
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import galib


class TestGalibBasic(unittest.TestCase):
    """Basic tests for galib package."""
    
    def test_some_function(self):
        """Test some_function returns expected message."""
        result = galib.some_function()
        self.assertIsInstance(result, str)
        self.assertIn("GALIB-Dev", result)
        
    def test_hello_world(self):
        """Test hello_world returns expected message."""
        result = galib.hello_world()
        self.assertIsInstance(result, str)
        self.assertIn("Hello", result)
        
    def test_version(self):
        """Test version is defined."""
        self.assertTrue(hasattr(galib, '__version__'))
        self.assertIsInstance(galib.__version__, str)


if __name__ == '__main__':
    unittest.main()
