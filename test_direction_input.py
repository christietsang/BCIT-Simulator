from unittest import TestCase
from unittest.mock import patch
from game import direction_input


class Test(TestCase):

    @patch('builtins.input', side_effect=["w"])
    def test_direction_input_north(self, _):
        actual_output = direction_input()
        expected_output = (-1, 0)
        self.assertEqual(expected_output, actual_output)

    @patch('builtins.input', side_effect=["a"])
    def test_direction_input_west(self, _):
        actual_output = direction_input()
        expected_output = (0, -1)
        self.assertEqual(expected_output, actual_output)

    @patch('builtins.input', side_effect=["d"])
    def test_direction_input_east(self, _):
        actual_output = direction_input()
        expected_output = (0, 1)
        self.assertEqual(expected_output, actual_output)

    @patch('builtins.input', side_effect=["s"])
    def test_direction_input_south(self, _):
        actual_output = direction_input()
        expected_output = (1, 0)
        self.assertEqual(expected_output, actual_output)

    @patch('builtins.input', side_effect=["1"])
    def test_direction_input_numerical_input(self, _):
        actual_output = direction_input()
        expected_output = '1'
        self.assertEqual(expected_output, actual_output)
