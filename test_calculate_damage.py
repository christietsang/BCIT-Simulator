import io
from unittest import TestCase
from unittest.mock import patch
from game import calculate_damage


class Test(TestCase):

    @patch('random.randint', return_value=1)
    def test_calculate_damage_target_dictionary_changed(self, _):
        attacker = {'critical': 2,
                    'name': 'Finals',
                    'reliability': 5,
                    'skill': ['Boredom', 'Confusion', 'Vocabulary'],
                    'stats': {'max_damage': 7, 'max_health': 7}}

        target = {
            'current_health': 8,
            'name': 'Finals',
            'skill': ['Boredom', 'Confusion', 'Vocabulary'],
            'stats': {'max_damage': 7, 'max_health': 7}}

        calculate_damage(attacker, target)
        expected = {'current_health': 1,
                    'name': 'Finals',
                    'skill': ['Boredom', 'Confusion', 'Vocabulary'],
                    'stats': {'max_damage': 7, 'max_health': 7}}
        actual = target
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=1)
    def test_calculate_damage_negative_health(self, _):
        attacker = {'critical': 2,
                    'name': 'Finals',
                    'reliability': 5,
                    'skill': ['Boredom', 'Difficulty', 'Vocabulary'],
                    'stats': {'max_damage': 7, 'max_health': 7}}

        target = {
            'current_health': 6,
            'name': 'Finals',
            'skill': ['Boredom', 'Difficulty', 'Vocabulary'],
            'stats': {'max_damage': 7, 'max_health': 7}}

        calculate_damage(attacker, target)
        expected = {'current_health': 0,
                    'name': 'Finals',
                    'skill': ['Boredom', 'Difficulty', 'Vocabulary'],
                    'stats': {'max_damage': 7, 'max_health': 7}}
        actual = target
        self.assertEqual(expected, actual)

    @patch('game.colorizer', return_value="[38;2;198;45;45mFinals used Carpal Tunnel to steal"
                                          " 7 Reese's Peanut Butter Cups from Finals\n"
                                          " [38;2;255;255;255m\n")
    @patch('random.randint', return_value=1)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_calculate_damage_attacker_is_character_print_output(self, mock_output, _, __):
        attacker = {'critical': 2,
                    'name': 'Finals',
                    'reliability': 5,
                    'skill': ['Boredom', 'Carpal Tunnel', 'Vocabulary'],
                    'stats': {'max_damage': 7, 'max_health': 7}}

        target = {
            'current_health': 6,
            'name': 'Finals',
            'skill': ['Boredom', 'Carpal Tunnel', 'Vocabulary'],
            'stats': {'max_damage': 7, 'max_health': 7}}

        calculate_damage(attacker, target)
        expected = (
            "[38;2;198;45;45mFinals used Carpal Tunnel to steal"
            " 7 Reese's Peanut Butter Cups from Finals\n"
            " [38;2;255;255;255m\n\n")
        self.assertEqual(expected, mock_output.getvalue())

    @patch('game.colorizer',
           return_value="[38;2;198;45;45mMidterm used Time Pressure to steal 20 Reese's Peanut "
                        "Butter Cups from Christie\n[38;2;255;255;255m\n")
    @patch('random.randint', return_value=1)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_calculate_damage_attacker_is_foe_print_output(self, mock_output, _, __):
        attacker = {'x-coordinate': 0, 'y-coordinate': 0, 'current_health': 30, 'experience': 50,
                    'reliability': 5, 'critical': 2, 'name': 'Midterm', 'current_level': 1,
                    'skill': ['Extreme Stress', 'Time Pressure', 'Midterm'],
                    'stats': {'max_health': 30, 'max_damage': 20}}

        target = {'x-coordinate': 0, 'y-coordinate': 0, 'current_health': 30, 'experience': 1,
                  'reliability': 5, 'critical': 2, 'current_level': 3, 'goal_met': False,
                  'name': 'Christie',
                  'skill': ['Complain', 'Reason', 'Obfuscate'],
                  'stats': {'max_health': 30, 'max_damage': 7},
                  'experience_per_level': {'Opinionated Student': 0, 'Outspoken Set Rep': 2,
                                           'Assertive Leader': 3}}

        calculate_damage(attacker, target)
        expected = (
            "[38;2;198;45;45mMidterm used Time Pressure to steal 20 Reese's Peanut Butter Cups "
            "from Christie\n"
            "[38;2;255;255;255m\n\n")
        self.assertEqual(expected, mock_output.getvalue())
