# test_intotheblock.py
"""
Tests for IntoTheBlock module.
"""

import unittest
from intotheblock import IntoTheBlock

class TestIntoTheBlock(unittest.TestCase):
    """Test cases for IntoTheBlock class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = IntoTheBlock()
        self.assertIsInstance(instance, IntoTheBlock)
        
    def test_run_method(self):
        """Test the run method."""
        instance = IntoTheBlock()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
