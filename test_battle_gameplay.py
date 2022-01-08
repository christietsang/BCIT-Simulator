from unittest import TestCase
from unittest.mock import patch
from game import battle_gameplay


class Test(TestCase):

    @patch('game.calculate_damage', return_value=None)
    @patch('game.is_alive', return_value=True)
    @patch('game.character_flee_sequence', return_value=None)
    @patch('game.enumerate_skills', return_value='4')
    def test_battle_gameplay_character_flees(self, _, __, ___, ____):
        character = {'x-coordinate': 0, 'y-coordinate': 0, 'current_health': 3,
                     'experience': 1, 'name': 'Christie',
                     'reliability': 4, 'critical': 3, 'current_level': 1, 'goal_met': False,
                     'skill': ['Complain', 'Reason', 'Obfuscate'],
                     'stats': {'max_health': 20, 'max_damage': 7},
                     'experience_per_level': {'Opinionated Student': 0, 'Outspoken Set Rep': 70,
                                              'Assertive Leader': 200}}

        foe = {'x-coordinate': 0, 'y-coordinate': 0, 'current_health': 5, 'experience': 20,
               'reliability': 5, 'critical': 2, 'name': 'Pop Quiz', 'current_level': 1,
               'skill': ['Surprise', 'Confuse', 'Shock'],
               'stats': {'max_health': 5, 'max_damage': 5}}
        self.assertIsNone(battle_gameplay(foe, character))

    @patch('game.calculate_damage', return_value=None)
    @patch('game.is_alive', return_value=True)
    @patch('game.enumerate_skills', return_value='3')
    @patch('game.chance_generator', return_value=True)
    @patch('game.colorizer', side_effect=['', 'Foe has fled'])
    @patch('game.character_flee_sequence', return_value=None)
    def test_battle_gameplay_foe_flees(self, _, __, ___, ____, _____, _______):
        character = {'x-coordinate': 0, 'y-coordinate': 0, 'current_health': 3,
                     'experience': 1, 'name': 'Christie',
                     'reliability': 4, 'critical': 5, 'current_level': 1, 'goal_met': False,
                     'skill': ['Complain', 'Reason', 'Obfuscate'],
                     'stats': {'max_health': 20, 'max_damage': 7},
                     'experience_per_level': {'Opinionated Student': 0, 'Outspoken Set Rep': 70,
                                              'Assertive Leader': 200}}

        foe = {'x-coordinate': 0, 'y-coordinate': 0, 'current_health': 5, 'experience': 20,
               'reliability': 5, 'critical': 5, 'name': 'Pop Quiz', 'current_level': 1,
               'skill': ['Surprise', 'Confuse', 'Shock'],
               'stats': {'max_health': 5, 'max_damage': 5}}
        self.assertIsNone(battle_gameplay(foe, character))
