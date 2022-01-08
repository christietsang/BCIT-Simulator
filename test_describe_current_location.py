import io
from unittest import TestCase
from unittest.mock import patch
from game import describe_current_location


class Test(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_current_location(self, mock_output):
        map_dictionary = {(0, 0): 'pizza', (0, 1): 'cookies', (1, 0): 'noodles', (1, 1): 'eggs'}
        character_dictionary = {"x-coordinate": 0, "y-coordinate": 0, "current_hp": 5}
        describe_current_location(map_dictionary, character_dictionary)
        expected_output = ("[38;2;255;255;179mpizza\n"
                           "A short and bubbly girl passes you at your elbow and tells you "
                           "cheerfully that you are location (0, 0) \n"
                           "Are people here always that friendly?\n"
                           " [38;2;255;255;255m\n")
        self.assertEqual(expected_output, mock_output.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_current_location_last_tuple(self, mock_output):
        map_dictionary = {(0, 0): 'pizza', (0, 1): 'cookies', (1, 0): 'noodles', (1, 1): 'eggs'}
        character_dictionary = {"x-coordinate": 1, "y-coordinate": 1, "current_hp": 5}
        describe_current_location(map_dictionary, character_dictionary)
        expected_output = ("[38;2;255;255;179meggs\n"
                           "A short and bubbly girl passes you at your elbow and tells you "
                           "cheerfully that you are location (1, 1) \n"
                           "Are people here always that friendly?\n"
                           " [38;2;255;255;255m\n")
        self.assertEqual(expected_output, mock_output.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_current_location_middle_tuple(self, mock_output):
        map_dictionary = {(0, 0): 'pizza', (0, 1): 'cookies', (1, 0): 'noodles', (1, 1): 'eggs'}
        character_dictionary = {"x-coordinate": 0, "y-coordinate": 1, "current_hp": 5}
        describe_current_location(map_dictionary, character_dictionary)
        expected_output = ("[38;2;255;255;179mcookies\n"
                           "A short and bubbly girl passes you at your elbow and tells you "
                           "cheerfully that you are location (0, 1) \n"
                           "Are people here always that friendly?\n"
                           " [38;2;255;255;255m\n")
        self.assertEqual(expected_output, mock_output.getvalue())

    def test_validate_move_character_dictionary_unchanged(self):
        map_dictionary = {(0, 0): 'pizza', (0, 1): 'cookies', (1, 0): 'noodles', (2, 2): 'eggs'}
        character_dictionary = {"x-coordinate": 0, "y-coordinate": 1, "current_hp": 5}
        describe_current_location(map_dictionary, character_dictionary)
        expected_location = {"x-coordinate": 0, "y-coordinate": 1, "current_hp": 5}
        self.assertEqual(expected_location, character_dictionary)

    def test_validate_move_board_unchanged(self):
        map_dictionary = {(0, 0): 'pizza', (0, 1): 'cookies', (1, 0): 'noodles', (1, 2): 'eggs'}
        character_dictionary = {"x-coordinate": 0, "y-coordinate": 1, "current_hp": 5}
        describe_current_location(map_dictionary, character_dictionary)
        expected_location = {(0, 0): 'pizza', (0, 1): 'cookies', (1, 0): 'noodles', (1, 2): 'eggs'}
        self.assertEqual(expected_location, map_dictionary)
