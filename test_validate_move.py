from unittest import TestCase
from game import validate_move


class Test(TestCase):

    def test_validate_move_east(self):
        board = {(0, 0): 'text', (0, 1): 'text', (1, 0): 'text', (1, 1): 'text'}
        character_location = {"x-coordinate": 0, "y-coordinate": 0, "current_hp": 5}
        new_direction = (0, 1)
        self.assertTrue(validate_move(board, character_location, new_direction))

    def test_validate_move_east_is_invalid(self):
        board = {(0, 0): 'text', (0, 1): 'text', (1, 0): 'text', (1, 1): 'text'}
        character_location = {"x-coordinate": 0, "y-coordinate": 1, "current_hp": 5}
        new_direction = (0, 1)
        self.assertFalse(validate_move(board, character_location, new_direction))

    def test_validate_move_west(self):
        board = {(0, 0): 'text', (0, 1): 'text', (1, 0): 'text', (1, 1): 'text'}
        character_location = {"x-coordinate": 0, "y-coordinate": 1, "current_hp": 5}
        new_direction = (0, -1)
        self.assertTrue(validate_move(board, character_location, new_direction))

    def test_validate_move_west_is_invalid(self):
        board = {(0, 0): 'text', (0, 1): 'text', (1, 0): 'text', (1, 1): 'text'}
        character_location = {"x-coordinate": 0, "y-coordinate": 0, "current_hp": 5}
        new_direction = (0, -1)
        self.assertFalse(validate_move(board, character_location, new_direction))

    def test_validate_move_north(self):
        board = {(0, 0): 'text', (0, 1): 'text', (1, 0): 'text', (1, 1): 'text'}
        character_location = {"x-coordinate": 1, "y-coordinate": 0, "current_hp": 5}
        new_direction = (-1, 0)
        self.assertTrue(validate_move(board, character_location, new_direction))

    def test_validate_move_north_is_invalid(self):
        board = {(0, 0): 'text', (0, 1): 'text', (1, 0): 'text', (1, 1): 'text'}
        character_location = {"x-coordinate": 0, "y-coordinate": 0, "current_hp": 5}
        new_direction = (-1, 0)
        self.assertFalse(validate_move(board, character_location, new_direction))

    def test_validate_move_south(self):
        board = {(0, 0): 'text', (0, 1): 'text', (1, 0): 'text', (1, 1): 'text'}
        character_location = {"x-coordinate": 0, "y-coordinate": 0, "current_hp": 5}
        new_direction = (1, 0)
        self.assertTrue(validate_move(board, character_location, new_direction))

    def test_validate_move_south_is_invalid(self):
        board = {(0, 0): 'text', (0, 1): 'text', (1, 0): 'text', (1, 1): 'text'}
        character_location = {"x-coordinate": 1, "y-coordinate": 0, "current_hp": 5}
        new_direction = (1, 0)
        self.assertFalse(validate_move(board, character_location, new_direction))

    def test_validate_move_board_unchanged(self):
        initial_board = {(0, 0): 'text', (0, 1): 'text', (0, 2): 'text', (1, 0): 'text'}
        character_location = {"x-coordinate": 0, "y-coordinate": 0, "current_hp": 5}
        new_direction = (0, 3)
        validate_move(initial_board, character_location, new_direction)
        expected_board = {(0, 0): 'text', (0, 1): 'text', (0, 2): 'text', (1, 0): 'text'}
        self.assertEqual(initial_board, expected_board)

    def test_validate_move_character_location_unchanged(self):
        initial_board = {(0, 0): 'text', (0, 1): 'text', (1, 0): 'text', (1, 1): 'text'}
        character_location = {"x-coordinate": 1, "y-coordinate": 1, "current_hp": 5}
        new_direction = (0, -1)
        validate_move(initial_board, character_location, new_direction)
        expected_location = {"x-coordinate": 1, "y-coordinate": 1, "current_hp": 5}
        self.assertEqual(character_location, expected_location)