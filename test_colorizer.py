from unittest import TestCase
from game import colorizer


class Test(TestCase):

    def test_colorizer_rgb_all_zeroes(self):
        expected_output = ("[38;2;0;0;0mYou say with earnest enthusiasm, \"Computer"
                           " Systems Technology Diploma, full time\"! [38;2;255;255;255m")
        actual_output = colorizer(0, 0, 0,
                                  'You say with earnest enthusiasm, "Computer Systems Technology '
                                  'Diploma, full time"!')
        self.assertEqual(expected_output, actual_output)

    def test_colorizer_rgb_largest_possible_number(self):
        expected_output = ("[38;2;255;255;255mYou say with great enthusiasm, \"Computer"
                           " Systems Technology Diploma, full time\"! [38;2;255;255;255m")
        actual_output = colorizer(255, 255, 255,
                                  'You say with great enthusiasm, "Computer Systems Technology '
                                  'Diploma, full time"!')
        self.assertEqual(expected_output, actual_output)

    def test_colorizer_rgb_middle_number(self):
        expected_output = ("[38;2;100;100;100mYou say with earnest enthusiasm, \"Computer"
                           " Systems Technology Diploma, full time\"! [38;2;255;255;255m")
        actual_output = colorizer(100, 100, 100,
                                  'You say with earnest enthusiasm, "Computer Systems Technology '
                                  'Diploma, full time"!')
        self.assertEqual(expected_output, actual_output)

    def test_colorizer_empty_string(self):
        expected_output = """[38;2;255;255;255m [38;2;255;255;255m"""
        actual_output = colorizer(255, 255, 255, '')
        self.assertEqual(expected_output, actual_output)
