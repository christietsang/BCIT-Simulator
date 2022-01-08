from unittest import TestCase
from unittest.mock import patch
from game import fight_or_flee


class Test(TestCase):

    @patch('game.battle_gameplay', return_value=None)
    def test_fight_or_flee_boss_fight(self, _):
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

        character = {'x-coordinate': 2, 'y-coordinate': 3, 'current_health': 20,
                     'reliability': 4, 'experience': 1, 'critical': 3,
                     'current_level': 1, 'name': 'Christie',
                     'goal_met': False, 'skill': ['Complain', 'Reason', 'Obfuscate'],
                     'stats': {'max_health': 20, 'max_damage': 7},
                     'experience_per_level': {'Opinionated Student': 0,
                                              'Outspoken Set Rep': 70,
                                              'Assertive Leader': 200}}
        self.assertIsNone(fight_or_flee(foe, character))

    @patch('game.battle_gameplay', return_value=None)
    @patch('game.user_input', return_value='1')
    def test_fight_or_flee_regular_foe_fight(self, _, __):
        foe = {'critical': 3,
               'current_health': 7,
               'current_level': 1,
               'experience': 25,
               'name': 'Midterm',
               'reliability': 5,
               'skill': ['Boredom', 'Carpal Tunnel', 'Vocabulary'],
               'stats': {'max_damage': 7, 'max_health': 7},
               'x-coordinate': 0,
               'y-coordinate': 0}

        character = {'x-coordinate': 2, 'y-coordinate': 3, 'current_health': 20,
                     'reliability': 4, 'experience': 1, 'critical': 3,
                     'current_level': 1, 'name': 'Christie',
                     'goal_met': False, 'skill': ['Complain', 'Reason', 'Obfuscate'],
                     'stats': {'max_health': 30, 'max_damage': 7},
                     'experience_per_level': {'Opinionated Student': 0,
                                              'Outspoken Set Rep': 70,
                                              'Assertive Leader': 200}}
        self.assertIsNone(fight_or_flee(foe, character))

    @patch('game.battle_gameplay', return_value=None)
    @patch('game.user_input', return_value='2')
    def test_fight_or_flee_character_flee(self, _, __):
        foe = {'critical': 2,
               'current_health': 7,
               'current_level': 1,
               'experience': 25,
               'name': 'Midterm',
               'reliability': 5,
               'skill': ['Boredom', 'Carpal Tunnel', 'Vocabulary'],
               'stats': {'max_damage': 7, 'max_health': 7},
               'x-coordinate': 0,
               'y-coordinate': 0}

        character = {'x-coordinate': 2, 'y-coordinate': 3, 'current_health': 20,
                     'reliability': 4, 'experience': 1, 'critical': 3,
                     'current_level': 1, 'name': 'Christie',
                     'goal_met': False, 'skill': ['Complain', 'Reason', 'Obfuscate'],
                     'stats': {'max_health': 30, 'max_damage': 7},
                     'experience_per_level': {'Opinionated Student': 0,
                                              'Outspoken Set Rep': 70,
                                              'Assertive Leader': 200}}
        self.assertIsNone(fight_or_flee(foe, character))
