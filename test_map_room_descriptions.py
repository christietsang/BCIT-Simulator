from unittest import TestCase
from unittest.mock import patch
from game import map_room_descriptions


class Test(TestCase):

    def test_map_room_descriptions_large_length_keys(self):
        actual_output = len(map_room_descriptions(50, 50))
        expected_output = 2500
        self.assertEqual(expected_output, actual_output)

    def test_map_room_descriptions_smallest_length_keys(self):
        actual_output = len(map_room_descriptions(2, 2))
        expected_output = 4
        self.assertEqual(expected_output, actual_output)

    @patch('random.randint', return_value=0)
    def test_map_room_descriptions_of_unequal_key_lengths(self, _):
        actual_output = map_room_descriptions(3, 2)
        expected_output = {(0, 0): f'You walk in the hallways between the elevators and the '
                                   f'anti-social high chairs that\nface the wall.\n',
                           (0, 1): f'You walk in the hallways between the elevators and the '
                                   f'anti-social high chairs that\nface the wall.\n',
                           (1, 0): f'You walk in the hallways between the elevators and the '
                                   f'anti-social high chairs that\nface the wall.\n',
                           (1, 1): f'You walk in the hallways between the elevators and the '
                                   f'anti-social high chairs that\nface the wall.\n',
                           (2, 0): f'You walk in the hallways between the elevators and the '
                                   f'anti-social high chairs that\nface the wall.\n',
                           (2, 1): f'You walk in the hallways between the elevators and the '
                                   f'anti-social high chairs that\nface the wall.\n'}
        self.assertEqual(expected_output, actual_output)

    @patch('random.randint', return_value=5)
    def test_map_room_descriptions_last_element_in_list(self, _):
        actual_output = map_room_descriptions(1, 1)
        expected_output = {(0, 0): f'You walk into a brightly lit gym with padded floors. Each '
                                   f'piece of new equipment has been\nencircled with yellow '
                                   f'caution tape with a piece of paper haphazardly taped on top, '
                                   f'stating\n"CLOSED DUE TO COVID". You wonder to yourself why '
                                   f'you pay rec fees when you can\'t even\nuse rec services.\n'}
        self.assertEqual(expected_output, actual_output)
