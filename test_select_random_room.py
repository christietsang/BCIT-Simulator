from unittest import TestCase
from unittest.mock import patch
from game import select_random_room


class Test(TestCase):

    @patch('random.randint', return_value=3)
    def test_select_middle_random_room(self, _):
        actual_output = select_random_room()
        expected_output = 'You pull open the door and walk into a bustling classroom filled ' \
                          'with chattering students.\n'
        self.assertEqual(expected_output, actual_output)

    @patch('random.randint', return_value=5)
    def test_select_last_random_room(self, _):
        actual_output = select_random_room()
        expected_output = 'You walk into a brightly lit gym with padded floors. Each piece of ' \
                          'new equipment has been\nencircled with yellow caution tape with a ' \
                          'piece of paper haphazardly taped on top, stating\n"CLOSED DUE TO ' \
                          'COVID". You wonder to yourself why you pay rec fees when you can\'t ' \
                          'even\nuse rec services.\n'
        self.assertEqual(expected_output, actual_output)

    @patch('random.randint', return_value=0)
    def test_select_first_random_room(self, _):
        actual_output = select_random_room()
        expected_output = 'You walk in the hallways between the elevators and the anti-social ' \
                          'high chairs that\nface the wall.\n'
        self.assertEqual(expected_output, actual_output)
