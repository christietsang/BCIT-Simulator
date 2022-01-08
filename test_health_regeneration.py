from unittest import TestCase
from game import health_regeneration
import io
from unittest.mock import patch


class Test(TestCase):

    def test_health_regeneration_health_is_zero(self):
        character = {'x-coordinate': 0, 'y-coordinate': 0, 'current_health': 0, 'experience': 1,
                     'reliability': 5, 'critical': 2, 'current_level': 3, 'goal_met': False,
                     'skill': ['Complain', 'Reason', 'Obfuscate'],
                     'stats': {'max_health': 30, 'max_damage': 7}}
        health_regeneration(character)
        expected_output = {'x-coordinate': 0, 'y-coordinate': 0, 'current_health': 4,
                           'experience': 1, 'reliability': 5, 'critical': 2, 'current_level': 3,
                           'goal_met': False, 'skill': ['Complain', 'Reason', 'Obfuscate'],
                           'stats': {'max_health': 30, 'max_damage': 7}}
        self.assertEqual(expected_output, character)

    def test_health_regeneration_no_health_regeneration(self):
        character = {'x-coordinate': 0, 'y-coordinate': 0, 'current_health': 30, 'experience': 1,
                     'reliability': 5, 'critical': 2, 'current_level': 3, 'goal_met': False,
                     'skill': ['Complain', 'Reason', 'Obfuscate'],
                     'stats': {'max_health': 30, 'max_damage': 7}}
        health_regeneration(character)
        expected_output = {'x-coordinate': 0, 'y-coordinate': 0, 'current_health': 30,
                           'experience': 1, 'reliability': 5, 'critical': 2, 'current_level': 3,
                           'goal_met': False, 'skill': ['Complain', 'Reason', 'Obfuscate'],
                           'stats': {'max_health': 30, 'max_damage': 7}}
        self.assertEqual(expected_output, character)

    def test_health_regeneration_almost_full_health(self):
        character = {'x-coordinate': 0, 'y-coordinate': 0, 'current_health': 29, 'experience': 1,
                     'reliability': 5, 'critical': 2, 'current_level': 3, 'goal_met': False,
                     'skill': ['Complain', 'Reason', 'Obfuscate'],
                     'stats': {'max_health': 30, 'max_damage': 7}}
        health_regeneration(character)
        expected_output = {'experience': 1, 'reliability': 5, 'critical': 2, 'current_level': 3,
                           'x-coordinate': 0, 'y-coordinate': 0, 'current_health': 30,
                           'goal_met': False, 'skill': ['Complain', 'Reason', 'Obfuscate'],
                           'stats': {'max_health': 30, 'max_damage': 7}}
        self.assertEqual(expected_output, character)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_health_regeneration_health_regeneration_printed_message(self, mock_output):
        character = {'x-coordinate': 0, 'y-coordinate': 0, 'current_health': 15, 'experience': 1,
                     'reliability': 5, 'critical': 2, 'current_level': 3, 'goal_met': False,
                     'stats': {'max_health': 30, 'max_damage': 7}}
        health_regeneration(character)
        expected_output = "[38;2;223;77;174mYou have regained 4 Peanut Butter Cup. " \
                          "You now have 19 left. [38;2;255;255;255m\n"
        self.assertEqual(expected_output, mock_output.getvalue())
