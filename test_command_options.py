from unittest import TestCase
from unittest.mock import patch
from game import command_options
import io


class Test(TestCase):

    @patch('game.print_travel_commands', return_value=None)
    def test_command_options_user_enters_one(self, _):
        user_input = '1'
        character = {'x-coordinate': 2, 'y-coordinate': 3, 'current_health': 20,
                     'reliability': 4, 'experience': 1, 'critical': 3,
                     'current_level': 1, 'name': 'Christie',
                     'goal_met': False, 'skill': ['Complain', 'Reason', 'Obfuscate'],
                     'stats': {'max_health': 20, 'max_damage': 7},
                     'experience_per_level': {'Opinionated Student': 0,
                                              'Outspoken Set Rep': 70,
                                              'Assertive Leader': 200}}
        self.assertIsNone(command_options(character, user_input))

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_command_options_user_enters_two(self, mock_output):
        user_input = '2'
        character = {'x-coordinate': 2, 'y-coordinate': 3, 'current_health': 20,
                     'reliability': 4, 'experience': 1, 'critical': 3,
                     'current_level': 1, 'name': 'Christie',
                     'goal_met': False, 'skill': ['Complain', 'Reason', 'Obfuscate'],
                     'stats': {'max_health': 20, 'max_damage': 7},
                     'experience_per_level': {'Opinionated Student': 0,
                                              'Outspoken Set Rep': 70,
                                              'Assertive Leader': 200}}
        command_options(character, user_input)
        expected_output = ("[38;2;153;204;255m\n"
                           "Current Level: 1 - Opinionated Student\n"
                           "Health: 20 Peanut Butter Cups\n"
                           "Experience: 1\n"
                           "Max Damage: 7\n"
                           "Skills: ['Complain', 'Reason', 'Obfuscate'] [38;2;255;255;255m\n")
        self.assertEqual(expected_output, mock_output.getvalue())
