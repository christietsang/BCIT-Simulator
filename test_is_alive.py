from unittest import TestCase
from game import is_alive


class Test(TestCase):

    def test_is_alive_smallest_positive_number(self):
        expected_output = is_alive({"x-coordinate": 0, "y-coordinate": 0, "current_health": 1})
        self.assertEqual(True, expected_output)

    def test_is_alive_negative_number(self):
        expected_output = is_alive({"x-coordinate": 0, "y-coordinate": 0, "current_health": -50})
        self.assertEqual(False, expected_output)

    def test_is_not_alive_health_at_zero(self):
        expected_output = is_alive({"x-coordinate": 0, "y-coordinate": 0, "current_health": 0})
        self.assertEqual(False, expected_output)

    def test_is_alive_unchanged_character_dictionary(self):
        character_information = {"x-coordinate": 0, "y-coordinate": 0, "current_health": 5}
        is_alive(character_information)
        expected_character_information = {"x-coordinate": 0, "y-coordinate": 0, "current_health": 5}
        self.assertEqual(character_information, expected_character_information)
