import io
from unittest import TestCase
from unittest.mock import patch
from game import enumerate_skills


class Test(TestCase):
    @patch('builtins.input', side_effect=['1', '2'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_enumerate_skills_foe_is_not_a_boss(self, mock_output, _):
        character = {'x-coordinate': 0, 'y-coordinate': 0, 'current_health': 0, 'experience': 1,
                     'reliability': 5, 'critical': 2, 'current_level': 3, 'goal_met': False,
                     'skill': ['Complain', 'Reason', 'Obfuscate'],
                     'stats': {'max_health': 30, 'max_damage': 7}}
        foe = {'critical': 2,
               'current_health': 7,
               'current_level': 1,
               'experience': 25,
               'name': 'Communications Essay',
               'reliability': 5,
               'skill': ['Boredom', 'Carpal Tunnel', 'Vocabulary'],
               'stats': {'max_damage': 7, 'max_health': 7},
               'x-coordinate': 0,
               'y-coordinate': 0}
        expected = (
            "[38;2;198;45;45m1 [38;2;255;255;255m [38;2;198;45;45mComplain "
            "[38;2;255;255;255m\n"
            "[38;2;198;45;45m2 [38;2;255;255;255m [38;2;198;45;45mReason "
            "[38;2;255;255;255m\n"
            "[38;2;198;45;45m3 [38;2;255;255;255m [38;2;198;45;45mObfuscate "
            "[38;2;255;255;255m\n"
            "[38;2;198;45;45m4 [38;2;255;255;255m [38;2;198;45;45mFlee "
            "[38;2;255;255;255m\n")
        enumerate_skills(character, foe)
        self.assertEqual(expected, mock_output.getvalue())

    @patch('builtins.input', side_effect=['1', '2'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_enumerate_skills_foe_is_the_boss(self, mock_output, _):
        character = {'x-coordinate': 20, 'y-coordinate': 21, 'current_health': 0, 'experience': 1,
                     'reliability': 5, 'critical': 2, 'current_level': 3, 'goal_met': False,
                     'skill': ['Complain', 'Reason', 'Obfuscate'],
                     'stats': {'max_health': 30, 'max_damage': 7}}
        foe = {'critical': 2,
               'current_health': 7,
               'current_level': 1,
               'experience': 25,
               'name': 'Finals',
               'reliability': 5,
               'skill': ['Boredom', 'Carpal Tunnel', 'Vocabulary'],
               'stats': {'max_damage': 7, 'max_health': 7},
               'x-coordinate': 0,
               'y-coordinate': 0}
        expected = (
            "[38;2;198;45;45m1 [38;2;255;255;255m [38;2;198;45;45mComplain "
            "[38;2;255;255;255m\n"
            "[38;2;198;45;45m2 [38;2;255;255;255m [38;2;198;45;45mReason "
            "[38;2;255;255;255m\n"
            "[38;2;198;45;45m3 [38;2;255;255;255m [38;2;198;45;45mObfuscate "
            "[38;2;255;255;255m\n")
        enumerate_skills(character, foe)
        self.assertEqual(expected, mock_output.getvalue())
