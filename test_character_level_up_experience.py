from unittest import TestCase
from game import character_level_up_experience


class Test(TestCase):

    def test_character_level_up_experience_character_level_up_experience_reset(self):
        character = {'x-coordinate': 0, 'y-coordinate': 0, 'current_health': 20, 'experience': 100,
                     'reliability': 4, 'critical': 3, 'current_level': 1, 'goal_met': False,
                     'skill': ['Complain', 'Reason', 'Obfuscate'],
                     'stats': {'max_health': 20, 'max_damage': 7},
                     'experience_per_level': {'level1': 0, 'level2': 70,
                                              'level3': 200}}

        foe = {'x-coordinate': 0, 'y-coordinate': 0, 'current_health': 7, 'experience': 25,
               'reliability': 5, 'critical': 2, 'name': 'Communications Essay', 'current_level': 1,
               'skill': ['Boredom', 'Carpal Tunnel', 'Vocabulary'],
               'stats': {'max_health': 7, 'max_damage': 7}}
        character_level_up_experience(character, foe)
        expected = {'critical': 3,
                    'current_health': 40,
                    'current_level': 2,
                    'experience': 0,
                    'experience_per_level': {'level1': 0, 'level2': 70, 'level3': 200},
                    'goal_met': False,
                    'reliability': 4,
                    'skill': ['Complain', 'Reason', 'Obfuscate'],
                    'stats': {'max_health': 40, 'max_damage': 14},
                    'x-coordinate': 0,
                    'y-coordinate': 0}
        self.assertEqual(expected, character)

    def test_character_level_up_experience_no_level_up_experience_gained(self):
        character = {'x-coordinate': 1, 'y-coordinate': 0, 'current_health': 20, 'experience': 50,
                     'reliability': 4, 'critical': 3, 'current_level': 1, 'goal_met': False,
                     'skill': ['Complain', 'Reason', 'Obfuscate'],
                     'stats': {'max_health': 20, 'max_damage': 7},
                     'experience_per_level': {'Opinionated Student': 0, 'Outspoken Set Rep': 70,
                                              'Assertive Leader': 200}}

        foe = {'x-coordinate': 1, 'y-coordinate': 0, 'current_health': 7, 'experience': 5,
               'reliability': 5, 'critical': 2, 'name': 'Communications Essay', 'current_level': 1,
               'skill': ['Boredom', 'Carpal Tunnel', 'Vocabulary'],
               'stats': {'max_health': 7, 'max_damage': 7}}
        character_level_up_experience(character, foe)
        expected = {'critical': 3,
                    'current_health': 20,
                    'current_level': 1,
                    'experience': 55,
                    'experience_per_level': {'Assertive Leader': 200,
                                             'Opinionated Student': 0,
                                             'Outspoken Set Rep': 70},
                    'goal_met': False,
                    'reliability': 4,
                    'skill': ['Complain', 'Reason', 'Obfuscate'],
                    'stats': {'max_damage': 7, 'max_health': 20},
                    'x-coordinate': 1,
                    'y-coordinate': 0}
        self.assertEqual(expected, character)
