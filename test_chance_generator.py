from unittest import TestCase
from unittest.mock import patch
from game import chance_generator


class Test(TestCase):

    @patch('random.randint', return_value=1)
    def test_chance_generator_check_if_false(self, _):
        characters = {'x-coordinate': 0, 'y-coordinate': 0}
        actual_output = chance_generator(characters)
        self.assertTrue(actual_output)

    def test_chance_generator_character_coordinates_True(self):
        characters = {'x-coordinate': 20, 'y-coordinate': 21}
        actual_output = chance_generator(characters)
        self.assertTrue(actual_output)

    @patch('random.randint', return_value=5)
    def test_chance_generator_check_if_true(self, _):
        characters = {'x-coordinate': 0, 'y-coordinate': 0}
        actual_output = chance_generator(characters)
        self.assertFalse(actual_output)
