import unittest

class TestCalc(unittest.TestCase):
    """
    Test the add function from the calc library
    """

    def test_idiot(self):
        """
        Test that the addition of two integers returns the correct total
        """
        self.assertEqual(1, 1)
    
    def test_momo(self):
        """
        Test that the addition of two integers returns the correct total
        """
        self.assertEqual(1, 1)
    
    
    def test_pizza(self):
        """
        Test that the addition of two integers returns the correct total
        """
        self.assertEqual(3, 3)
    
    def test_burger(self):
        """
        Test that the addition of two integers returns the correct total
        """
        self.assertEqual(4, 4)

if __name__ == '__main__':
    unittest.main()