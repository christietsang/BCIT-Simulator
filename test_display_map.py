from unittest import TestCase
from game import display_map
from unittest.mock import patch
import io


class Test(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_map_coordinates_are_zeroes(self, mock_output):
        characters = {"x-coordinate": 0, "y-coordinate": 0}
        descriptions = {(0, 0): f'You walk in the hallways between the elevators and the '
                                f'anti-social high chairs that\nface the wall.\n',
                        (0, 1): f'You walk down a dimly lit hallway on the 6th floor and pass the '
                                f'lunch room on your way to\nthe stairs.\n',
                        (1, 0): f'On the way to the restroom, you pass by a gaggle of students '
                                f'from the other sets mingling\nabout in the hallways.\n',
                        (1, 1): f'You pull open the door and walk into a bustling classroom filled '
                                f'with chattering students.\n',
                        (2, 1): f'You walk into a brightly lit gym with padded floors. Each '
                                f'piece '
                                f'of new equipment has been\nencircled with yellow caution tape '
                                f'with a piece of paper haphazardly taped on top, '
                                f'stating\n"CLOSED DUE TO COVID". You wonder to yourself why you '
                                f'pay rec fees when you can\'t even\nuse rec services.\n',
                        (2, 2): 'You tap your BCIT ID against the card reader and walk into '
                                'a group study room.  Inside,\nyou see a number of weary '
                                'looking students hunched over their laptops with their '
                                'hands\ncradling their face.  You think to yourself that this '
                                'is a familiar sight at BCIT.\n'}
        display_map(characters, descriptions)
        expected_output = (
            "[38;2;71;71;107m₪ [38;2;255;255;255m[38;2;71;71;107m₪ [38;2;255;255;255m"
            "[38;2;71;71;107m₪ [38;2;255;255;255m[38;2;71;71;107m₪ [38;2;255;255;255m"
            "[38;2;71;71;107m₪ [38;2;255;255;255m[38;2;71;71;107m₪ [38;2;255;255;255m"
            "[38;2;71;71;107m₪ [38;2;255;255;255m[38;2;71;71;107m₪ [38;2;255;255;255m"
            "[38;2;71;71;107m₪ [38;2;255;255;255m[38;2;71;71;107m₪ [38;2;255;255;255m\n"
            "[38;2;71;71;107m₪ [38;2;255;255;255m[38;2;71;71;107m₪ [38;2;255;255;255m"
            "[38;2;71;71;107m₪ [38;2;255;255;255m[38;2;71;71;107m₪ [38;2;255;255;255m"
            "[38;2;71;71;107m₪ [38;2;255;255;255m[38;2;71;71;107m₪ [38;2;255;255;255m"
            "[38;2;71;71;107m₪ [38;2;255;255;255m[38;2;71;71;107m₪ [38;2;255;255;255m"
            "[38;2;71;71;107m₪ [38;2;255;255;255m[38;2;71;71;107m₪ [38;2;255;255;255m\n"
            "[38;2;71;71;107m₪ [38;2;255;255;255m[38;2;71;71;107m₪ [38;2;255;255;255m"
            "[38;2;71;71;107m₪ [38;2;255;255;255m[38;2;71;71;107m₪ [38;2;255;255;255m"
            "[38;2;71;71;107m₪ [38;2;255;255;255m[38;2;71;71;107m₪ [38;2;255;255;255m"
            "[38;2;71;71;107m₪ [38;2;255;255;255m[38;2;71;71;107m₪ [38;2;255;255;255m"
            "[38;2;71;71;107m₪ [38;2;255;255;255m[38;2;71;71;107m₪ [38;2;255;255;255m\n"
            "[38;2;71;71;107m₪ [38;2;255;255;255m[38;2;71;71;107m₪ [38;2;255;255;255m"
            "[38;2;71;71;107m₪ [38;2;255;255;255m[38;2;71;71;107m₪ [38;2;255;255;255m"
            "[38;2;71;71;107m₪ [38;2;255;255;255m[38;2;71;71;107m₪ [38;2;255;255;255m"
            "[38;2;71;71;107m₪ [38;2;255;255;255m[38;2;71;71;107m₪ [38;2;255;255;255m"
            "[38;2;71;71;107m₪ [38;2;255;255;255m[38;2;71;71;107m₪ [38;2;255;255;255m\n"
            "[38;2;71;71;107m₪ [38;2;255;255;255m[38;2;71;71;107m₪ [38;2;255;255;255m"
            "[38;2;71;71;107m₪ [38;2;255;255;255m[38;2;71;71;107m₪ [38;2;255;255;255m"
            "[38;2;255;0;0m⟐ [38;2;255;255;255m⊙ [38;2;71;71;107m₪ [38;2;255;255;255m"
            "[38;2;71;71;107m₪ [38;2;255;255;255m[38;2;71;71;107m₪ [38;2;255;255;255m"
            "[38;2;71;71;107m₪ [38;2;255;255;255m\n"
            "[38;2;71;71;107m₪ [38;2;255;255;255m[38;2;71;71;107m₪ [38;2;255;255;255m"
            "[38;2;71;71;107m₪ [38;2;255;255;255m[38;2;71;71;107m₪ [38;2;255;255;255m⊙"
            " . [38;2;71;71;107m₪ [38;2;255;255;255m[38;2;71;71;107m₪ "
            "[38;2;255;255;255m[38;2;71;71;107m₪ [38;2;255;255;255m[38;2;71;71;107m₪ "
            "[38;2;255;255;255m\n"
            "[38;2;71;71;107m₪ [38;2;255;255;255m[38;2;71;71;107m₪ [38;2;255;255;255m"
            "[38;2;71;71;107m₪ [38;2;255;255;255m[38;2;71;71;107m₪ [38;2;255;255;255m"
            "[38;2;71;71;107m₪ [38;2;255;255;255m+ ⊗ [38;2;71;71;107m₪ "
            "[38;2;255;255;255m[38;2;71;71;107m₪ [38;2;255;255;255m[38;2;71;71;107m₪ "
            "[38;2;255;255;255m\n"
            "[38;2;71;71;107m₪ [38;2;255;255;255m[38;2;71;71;107m₪ [38;2;255;255;255m"
            "[38;2;71;71;107m₪ [38;2;255;255;255m[38;2;71;71;107m₪ [38;2;255;255;255m"
            "[38;2;71;71;107m₪ [38;2;255;255;255m[38;2;71;71;107m₪ [38;2;255;255;255m"
            "[38;2;71;71;107m₪ [38;2;255;255;255m[38;2;71;71;107m₪ [38;2;255;255;255m"
            "[38;2;71;71;107m₪ [38;2;255;255;255m[38;2;71;71;107m₪ [38;2;255;255;255m\n"
            "[38;2;71;71;107m₪ [38;2;255;255;255m[38;2;71;71;107m₪ [38;2;255;255;255m"
            "[38;2;71;71;107m₪ [38;2;255;255;255m[38;2;71;71;107m₪ [38;2;255;255;255m"
            "[38;2;71;71;107m₪ [38;2;255;255;255m[38;2;71;71;107m₪ [38;2;255;255;255m"
            "[38;2;71;71;107m₪ [38;2;255;255;255m[38;2;71;71;107m₪ [38;2;255;255;255m"
            "[38;2;71;71;107m₪ [38;2;255;255;255m[38;2;71;71;107m₪ [38;2;255;255;255m\n"
            "[38;2;71;71;107m₪ [38;2;255;255;255m[38;2;71;71;107m₪ [38;2;255;255;255m"
            "[38;2;71;71;107m₪ [38;2;255;255;255m[38;2;71;71;107m₪ [38;2;255;255;255m"
            "[38;2;71;71;107m₪ [38;2;255;255;255m[38;2;71;71;107m₪ [38;2;255;255;255m"
            "[38;2;71;71;107m₪ [38;2;255;255;255m[38;2;71;71;107m₪ [38;2;255;255;255m"
            "[38;2;71;71;107m₪ [38;2;255;255;255m[38;2;71;71;107m₪ "
            "[38;2;255;255;255m\n")
        self.assertEqual(expected_output, mock_output.getvalue())

    def test_display_map_character_dictionary_unchanged(self):
        characters = {"x-coordinate": 5, "y-coordinate": 6}
        descriptions = {(0, 0): f'You walk in the hallways between the elevators and the '
                                'anti-social high chairs that\nface the wall.\n'}
        display_map(characters, descriptions)
        expected_character_dictionary = {"x-coordinate": 5, "y-coordinate": 6}
        self.assertEqual(expected_character_dictionary, characters)

    def test_display_map_room_dictionary_unchanged(self):
        characters = {"x-coordinate": 5, "y-coordinate": 6}
        descriptions = {(0, 0): f'You walk in the hallways between the elevators and the '
                                'anti-social high chairs that\nface the wall.\n'}
        display_map(characters, descriptions)
        expected_room_dictionary = {(0, 0): f'You walk in the hallways between the elevators and '
                                            f'the anti-social high chairs that\nface the wall.\n'}
        self.assertEqual(expected_room_dictionary, descriptions)
