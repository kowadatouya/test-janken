import unittest
from unittest.mock import patch
import io
import sys

from source.computer import computer_pon
from source.janken_judge import judge
from source.player import player_pon
from source.janken_main import main
class TestJankenMain(unittest.TestCase):

    @patch('player.player_pon', return_value='グー')
    @patch('computer.computer_pon', return_value='チョキ')
    def test_main_player_wins(self, mock_computer, mock_player):
        captured_output = io.StringIO()
        sys.stdout = captured_output

        main()

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        self.assertIn("あなたの総合勝利です！", output)

    @patch('player.player_pon', return_value='チョキ')
    @patch('computer.computer_pon', return_value='グー')
    def test_main_computer_wins(self, mock_computer, mock_player):
        captured_output = io.StringIO()
        sys.stdout = captured_output

        main()

        sys.stdout = sys.__stdout__ 
        output = captured_output.getvalue()

        self.assertIn("コンピュータの総合勝利です！", output)

if __name__ == '__main__':
    unittest.main()