from unittest import TestCase
from game import calculate_new_coordinates


class Test(TestCase):

    def test_calculate_new_coordinates_large_numbers(self):
        new_coordinates = (30, 10)
        current_location = {"x-coordinate": 10, "y-coordinate": 16, "current_hp": 5}
        actual_output = calculate_new_coordinates(current_location, new_coordinates)
        expected_output = (40, 26)
        self.assertEqual(expected_output, actual_output)

    def test_calculate_new_coordinates_negative_coordinates(self):
        new_coordinates = (-1, 0)
        current_location = {"x-coordinate": 5, "y-coordinate": 0, "current_hp": 5}
        actual_output = calculate_new_coordinates(current_location, new_coordinates)
        expected_output = (4, 0)
        self.assertEqual(expected_output, actual_output)

    def test_calculate_new_coordinates_large_negative_numbers(self):
        new_coordinates = (-50, -100)
        current_location = {"x-coordinate": 5, "y-coordinate": 0, "current_hp": 5}
        actual_output = calculate_new_coordinates(current_location, new_coordinates)
        expected_output = (-45, -100)
        self.assertEqual(expected_output, actual_output)

    def test_calculate_new_coordinates_sum_to_zeroes(self):
        new_coordinates = (-1, 0)
        current_location = {"x-coordinate": 1, "y-coordinate": 0, "current_hp": 5}
        actual_output = calculate_new_coordinates(current_location, new_coordinates)
        expected_output = (0, 0)
        self.assertEqual(expected_output, actual_output)

    def test_calculate_new_coordinates_no_movement(self):
        new_coordinates = (0, 0)
        current_location = {"x-coordinate": 1, "y-coordinate": 0, "current_hp": 5}
        actual_output = calculate_new_coordinates(current_location, new_coordinates)
        expected_output = (1, 0)
        self.assertEqual(expected_output, actual_output)

    def test_calculate_new_coordinates_character_dictionary_unchanged(self):
        character_location = {"x-coordinate": 0, "y-coordinate": 0, "current_hp": 5}
        new_coordinates = (0, 3)
        calculate_new_coordinates(character_location, new_coordinates)
        expected_location = {"x-coordinate": 0, "y-coordinate": 0, "current_hp": 5}
        self.assertEqual(character_location, expected_location)
