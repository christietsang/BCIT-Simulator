from unittest import TestCase
from game import move_character


class Test(TestCase):

    def test_move_character_x_coordinate_add_large_numbers_south(self):
        char_dictionary = ({"x-coordinate": 15, "y-coordinate": 30, "current_hp": 5})
        coordinates = (15, 0)
        move_character(char_dictionary, coordinates)
        updated_dictionary = ({"x-coordinate": 30, "y-coordinate": 30, "current_hp": 5})
        self.assertEqual(char_dictionary, updated_dictionary)

    def test_move_character_y_coordinate_add_small_numbers_east(self):
        char_dictionary = ({"x-coordinate": 1, "y-coordinate": 1, "current_hp": 5})
        coordinates = (0, 1)
        move_character(char_dictionary, coordinates)
        updated_dictionary = ({"x-coordinate": 1, "y-coordinate": 2, "current_hp": 5})
        self.assertEqual(char_dictionary, updated_dictionary)

    def test_move_character_move_north(self):
        char_dictionary = ({"x-coordinate": 1, "y-coordinate": 1, "current_hp": 5})
        coordinates = (-1, 0)
        move_character(char_dictionary, coordinates)
        updated_dictionary = ({"x-coordinate": 0, "y-coordinate": 1, "current_hp": 5})
        self.assertEqual(char_dictionary, updated_dictionary)

    def test_move_character_move_west(self):
        char_dictionary = ({"x-coordinate": 0, "y-coordinate": 15, "current_hp": 5})
        coordinates = (0, -10)
        move_character(char_dictionary, coordinates)
        updated_dictionary = ({"x-coordinate": 0, "y-coordinate": 5, "current_hp": 5})
        self.assertEqual(char_dictionary, updated_dictionary)

    def test_move_character_move_where_coordinates_are_zero(self):
        char_dictionary = ({"x-coordinate": 0, "y-coordinate": 1, "current_hp": 5})
        coordinates = (0, -1)
        move_character(char_dictionary, coordinates)
        updated_dictionary = ({"x-coordinate": 0, "y-coordinate": 0, "current_hp": 5})
        self.assertEqual(char_dictionary, updated_dictionary)
