from unittest import TestCase
from game import make_character


class Test(TestCase):

    def test_make_character_first(self):
        user_choice = '1'
        actual_output = make_character(user_choice)
        expected_output = {'x-coordinate': 0, 'y-coordinate': 0, 'current_health': 20,
                           'reliability': 4, 'experience': 1, 'critical': 3, 'current_level': 1,
                           'goal_met': False, 'skill': ['Complain', 'Reason', 'Obfuscate'],
                           'stats': {'max_health': 20, 'max_damage': 7},
                           'experience_per_level': {'Opinionated Student': 0,
                                                    'Outspoken Set Rep': 70,
                                                    'Assertive Leader': 120}}
        self.assertEqual(expected_output, actual_output)

    def test_make_character_last(self):
        user_choice = '4'
        actual_output = make_character(user_choice)
        expected_output = {'critical': 5,
                           'current_health': 60,
                           'current_level': 1,
                           'experience': 1,
                           'experience_per_level': {'Experienced Student': 0,
                                                    'Proficient Programmer': 70,
                                                    'Qualified Developer': 125},
                           'goal_met': False,
                           'reliability': 1,
                           'skill': ['Past Projects', 'Networking', 'Wisdom'],
                           'stats': {'max_damage': 15, 'max_health': 60},
                           'x-coordinate': 0,
                           'y-coordinate': 0}
        self.assertEqual(expected_output, actual_output)
