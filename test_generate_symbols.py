from unittest import TestCase
from game import generate_symbols


class Test(TestCase):

    def test_generate_symbols_all_tuples_out_of_range_except_character_location(self):
        characters = {"x-coordinate": 0, "y-coordinate": 0}
        descriptions = {(0, 0): f'You walk in the hallways between the elevators and the '
                                'anti-social high chairs that\nface the wall.\n'}
        actual_output = generate_symbols(characters, descriptions)
        expected_output = ['₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪',
                           '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪',
                           '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪',
                           '₪', '₪', '⟐', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪',
                           '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪',
                           '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪',
                           '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪',
                           '₪', '₪']
        self.assertEqual(expected_output, actual_output)

    def test_generate_symbols_multiple_symbols_negative_coordinates(self):
        characters = {"x-coordinate": -5, "y-coordinate": -5}
        descriptions = {(0, 0): f'You walk in the hallways between the elevators and the '
                                f'anti-social high chairs that\nface the wall.\n',
                        (0, 1): f'You walk down a dimly lit hallway on the 6th floor and pass the '
                                f'lunch room on your way to\nthe stairs.\n',
                        (1, 0): f'On the way to the restroom, you pass by a gaggle of students '
                                f'from the other sets mingling\nabout in the hallways.\n',
                        (1, 1): f'You pull open the door and walk into a bustling classroom filled '
                                f'with chattering students.\n',
                        (-5, -5): f'You walk into a brightly lit gym with padded floors. Each '
                                  f'piece '
                                  f'of new equipment has been\nencircled with yellow caution tape '
                                  f'with a piece of paper haphazardly taped on top, '
                                  f'stating\n"CLOSED DUE TO COVID". You wonder to yourself why you '
                                  f'pay rec fees when you can\'t even\nuse rec services.\n',
                        (0, 2): 'You tap your BCIT ID against the card reader and walk into '
                                'a group study room.  Inside,\nyou see a number of weary '
                                'looking students hunched over their laptops with their '
                                'hands\ncradling their face.  You think to yourself that this '
                                'is a familiar sight at BCIT.\n'}
        actual_output = generate_symbols(characters, descriptions)
        expected_output = ['₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪',
                           '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪',
                           '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪',
                           '₪', '₪', '⟐', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪',
                           '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪',
                           '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪',
                           '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪',
                           '₪', '⊙']
        self.assertEqual(expected_output, actual_output)

    def test_generate_symbols_multiple_symbols_positive_coordinates(self):
        characters = {"x-coordinate": 10, "y-coordinate": 10}
        descriptions = {(7, 9): f'You walk in the hallways between the elevators and the '
                                f'anti-social high chairs that\nface the wall.\n',
                        (9, 8): f'You walk down a dimly lit hallway on the 6th floor and pass the '
                                f'lunch room on your way to\nthe stairs.\n',
                        (6, 6): f'On the way to the restroom, you pass by a gaggle of students '
                                f'from the other sets mingling\nabout in the hallways.\n',
                        (7, 8): f'You pull open the door and walk into a bustling classroom filled '
                                'with chattering students.\n',
                        (8, 7): f'You walk into a brightly lit gym with padded floors. Each '
                                f'piece '
                                f'of new equipment has been\nencircled with yellow caution tape '
                                f'with a piece of paper haphazardly taped on top, '
                                f'stating\n"CLOSED DUE TO COVID". You wonder to yourself why you '
                                f'pay rec fees when you can\'t even\nuse rec services.\n',
                        (7, 7): f'You tap your BCIT ID against the card reader and walk into '
                                f'a group study room.  Inside,\nyou see a number of weary '
                                f'looking students hunched over their laptops with their '
                                f'hands\ncradling their face.  You think to yourself that this '
                                f'is a familiar sight at BCIT.\n'}
        actual_output = generate_symbols(characters, descriptions)
        expected_output = ['⊙', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '⊗', '.', '⊙',
                           '₪', '₪', '₪', '₪', '₪', '₪', '₪', '+', '₪', '₪', '₪', '₪', '₪', '₪',
                           '₪', '₪', '₪', '₪', '⊙', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪',
                           '₪', '₪', '⟐', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪',
                           '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪',
                           '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪',
                           '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪', '₪',
                           '₪', '₪']
        self.assertEqual(expected_output, actual_output)

    def test_generate_symbols_character_unchanged(self):
        characters = {"x-coordinate": 5, "y-coordinate": 5}
        descriptions = {(7, 9): f'You walk in the hallways between the elevators and the '
                                f'anti-social high chairs that\nface the wall.\n',
                        (9, 8): f'You walk down a dimly lit hallway on the 6th floor and pass the '
                                f'lunch room on your way to\nthe stairs.\n',
                        (6, 6): f'On the way to the restroom, you pass by a gaggle of students '
                                f'from the other sets mingling\nabout in the hallways.\n',
                        (7, 8): f'You pull open the door and walk into a bustling classroom filled '
                                'with chattering students.\n',
                        (8, 7): f'You walk into a brightly lit gym with padded floors. Each '
                                f'piece '
                                f'of new equipment has been\nencircled with yellow caution tape '
                                f'with a piece of paper haphazardly taped on top, '
                                f'stating\n"CLOSED DUE TO COVID". You wonder to yourself why you '
                                f'pay rec fees when you can\'t even\nuse rec services.\n',
                        (7, 7): f'You tap your BCIT ID against the card reader and walk into '
                                f'a group study room.  Inside,\nyou see a number of weary '
                                f'looking students hunched over their laptops with their '
                                f'hands\ncradling their face.  You think to yourself that this '
                                f'is a familiar sight at BCIT.\n'}
        generate_symbols(characters, descriptions)
        expected_character_dictionary = {"x-coordinate": 5, "y-coordinate": 5}
        self.assertEqual(expected_character_dictionary, characters)

    def test_generate_symbols_room_dictionary_unchanged(self):
        characters = {"x-coordinate": 5, "y-coordinate": 6}
        descriptions = {(0, 0): f'You walk in the hallways between the elevators and the '
                                'anti-social high chairs that\nface the wall.\n'}
        generate_symbols(characters, descriptions)
        expected_room_dictionary = {(0, 0): f'You walk in the hallways between the elevators and '
                                            f'the anti-social high chairs that\nface the wall.\n'}
        self.assertEqual(expected_room_dictionary, descriptions)
