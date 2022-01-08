from unittest import TestCase
from unittest.mock import patch

from game import scale_foe_to_level


class Test(TestCase):

    @patch('game.make_foes', return_value={'critical': 2,
                                           'current_health': 7,
                                           'current_level': 2,
                                           'experience': 25,
                                           'name': 'Communications Essay',
                                           'reliability': 5,
                                           'skill': ['Boredom', 'Carpal Tunnel', 'Vocabulary'],
                                           'stats': {'max_damage': 14, 'max_health': 14},
                                           'x-coordinate': 0,
                                           'y-coordinate': 0})
    def test_scale_foe_to_level_scale_up_one_level(self, _):
        character = {'x-coordinate': 0, 'y-coordinate': 0, 'current_health': 29, 'experience': 1,
                     'reliability': 5, 'critical': 2, 'current_level': 3, 'goal_met': False}
        actual_output = scale_foe_to_level(character)
        expected_output = {'critical': 2,
                           'current_health': 14,
                           'current_level': 3,
                           'experience': 25,
                           'name': 'Communications Essay',
                           'reliability': 5,
                           'skill': ['Boredom', 'Carpal Tunnel', 'Vocabulary'],
                           'stats': {'max_damage': 28, 'max_health': 28},
                           'x-coordinate': 0,
                           'y-coordinate': 0}

        self.assertEqual(expected_output, actual_output)

    @patch('game.make_foes', return_value={'critical': 2,
                                           'current_health': 7,
                                           'current_level': 0,
                                           'experience': 25,
                                           'name': 'Communications Essay',
                                           'reliability': 5,
                                           'skill': ['Boredom', 'Carpal Tunnel', 'Vocabulary'],
                                           'stats': {'max_damage': 14, 'max_health': 14},
                                           'x-coordinate': 0,
                                           'y-coordinate': 0})
    def test_scale_foe_to_level_scale_up_two_levels(self, _):
        character = {'x-coordinate': 0, 'y-coordinate': 0, 'current_health': 29, 'experience': 1,
                     'reliability': 5, 'critical': 2, 'current_level': 3, 'goal_met': False}
        actual_output = scale_foe_to_level(character)
        expected_output = {'critical': 2,
                           'current_health': 28,
                           'current_level': 3,
                           'experience': 25,
                           'name': 'Communications Essay',
                           'reliability': 5,
                           'skill': ['Boredom', 'Carpal Tunnel', 'Vocabulary'],
                           'stats': {'max_damage': 56, 'max_health': 56},
                           'x-coordinate': 0,
                           'y-coordinate': 0}

        self.assertEqual(expected_output, actual_output)

    @patch('game.make_foes', return_value={'critical': 2,
                                           'current_health': 7,
                                           'current_level': 2,
                                           'experience': 25,
                                           'name': 'Communications Essay',
                                           'reliability': 5,
                                           'skill': ['Boredom', 'Carpal Tunnel', 'Vocabulary'],
                                           'stats': {'max_damage': 14, 'max_health': 14},
                                           'x-coordinate': 0,
                                           'y-coordinate': 0})
    def test_scale_foe_to_level_no_scaling(self, _):
        character = {'x-coordinate': 0, 'y-coordinate': 0, 'current_health': 31, 'experience': 1,
                     'reliability': 5, 'critical': 2, 'current_level': 1, 'goal_met': False}

        actual_output = scale_foe_to_level(character)

        expected_output = {'critical': 2,
                           'current_health': 7,
                           'current_level': 2,
                           'experience': 25,
                           'name': 'Communications Essay',
                           'reliability': 5,
                           'skill': ['Boredom', 'Carpal Tunnel', 'Vocabulary'],
                           'stats': {'max_damage': 14, 'max_health': 14},
                           'x-coordinate': 0,
                           'y-coordinate': 0}
        self.assertEqual(expected_output, actual_output)

    @patch('game.make_foes', return_value={'critical': 2,
                                           'current_health': 40,
                                           'current_level': 3,
                                           'experience': 60,
                                           'name': 'Finals',
                                           'reliability': 5,
                                           'skill': ['Extreme Stress', 'Time Pressure',
                                                     'Sleep Deprivation'],
                                           'stats': {'max_damage': 5, 'max_health': 70},
                                           'x-coordinate': 0,
                                           'y-coordinate': 0})
    def test_scale_foe_to_level_no_scaling_boss(self, _):
        character = {'x-coordinate': 20, 'y-coordinate': 21, 'current_health': 28, 'experience': 1,
                     'reliability': 5, 'critical': 2, 'current_level': 2, 'goal_met': False}
        actual_output = scale_foe_to_level(character)

        expected_output = {'critical': 2,
                           'current_health': 40,
                           'current_level': 3,
                           'experience': 60,
                           'name': 'Finals',
                           'reliability': 5,
                           'skill': ['Extreme Stress', 'Time Pressure', 'Sleep Deprivation'],
                           'stats': {'max_damage': 5, 'max_health': 70},
                           'x-coordinate': 0,
                           'y-coordinate': 0}

        self.assertEqual(expected_output, actual_output)
