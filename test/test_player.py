import unittest
from unittest.mock import patch
from source.player import player_pon
class TestPlayerPonFunction(unittest.TestCase):

    @patch('builtins.input', side_effect=['1'])
    def test_player_pon_goo(self, mock_input):
        result = player_pon()
        self.assertEqual(result, "グー")

    @patch('builtins.input', side_effect=['2'])
    def test_player_pon_choki(self, mock_input):
        result = player_pon()
        self.assertEqual(result, "チョキ")

    @patch('builtins.input', side_effect=['3'])
    def test_player_pon_par(self, mock_input):
        result = player_pon()
        self.assertEqual(result, "パー")

    @patch('builtins.input', side_effect=['0', '1'])
    def test_player_pon_invalid_then_valid(self, mock_input):
        result = player_pon()
        self.assertEqual(result, "グー")
    
    @patch('builtins.input', side_effect=['4', '2'])
    def test_player_pon_invalid_then_valid(self, mock_input):
        result = player_pon()
        self.assertEqual(result, "チョキ")

if __name__ == '__main__':
    unittest.main()
