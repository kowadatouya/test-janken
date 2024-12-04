import unittest
from unittest.mock import patch
from source.computer import computer_pon 

class TestComputerPonFunction(unittest.TestCase):

    @patch('random.choice', return_value='グー')
    def test_computer_pon_returns_goo(self, mock_choice):
        result = computer_pon()
        self.assertEqual(result, 'グー')

    @patch('random.choice', return_value='チョキ')
    def test_computer_pon_returns_choki(self, mock_choice):
        result = computer_pon()
        self.assertEqual(result, 'チョキ')

    @patch('random.choice', return_value='パー')
    def test_computer_pon_returns_paa(self, mock_choice):
        result = computer_pon()
        self.assertEqual(result, 'パー')

if __name__ == '__main__':
    unittest.main()