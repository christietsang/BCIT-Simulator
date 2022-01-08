from unittest import TestCase
from unittest.mock import patch
from game import make_foes


class Test(TestCase):
    def test_make_foes_boss(self):
        character = {'x-coordinate': 20, 'y-coordinate': 21}
        expected = {'critical': 4,
                    'current_health': 50,
                    'current_level': 3,
                    'experience': 60,
                    'name': 'Finals',
                    'reliability': 5,
                    'skill': ['Extreme Stress', 'Time Pressure', 'Sleep Deprivation'],
                    'stats': {'max_damage': 17, 'max_health': 60},
                    'x-coordinate': 0,
                    'y-coordinate': 0}
        actual = make_foes(character)
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=1)
    def test_make_foes_first_region_zero_to_thirteen(self, _):
        character = {'x-coordinate': 3, 'y-coordinate': 3}
        expected = {'critical': 2,
                    'current_health': 10,
                    'current_level': 1,
                    'experience': 25,
                    'name': 'Communications Essay',
                    'reliability': 5,
                    'skill': ['Boredom', 'Carpal Tunnel', 'Vocabulary'],
                    'stats': {'max_damage': 5, 'max_health': 6},
                    'x-coordinate': 0,
                    'y-coordinate': 0}
        actual = make_foes(character)
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=2)
    def test_make_foes_second_region_thirteen_to_twenty_five(self, _):
        character = {'x-coordinate': 15, 'y-coordinate': 14}
        expected = {'critical': 2,
                    'current_health': 10,
                    'current_level': 1,
                    'experience': 35,
                    'name': 'Cleaning Lady',
                    'reliability': 5,
                    'skill': ['Chemicals', 'Eject from Building', 'Cleaning Equipment'],
                    'stats': {'max_damage': 7, 'max_health': 7},
                    'x-coordinate': 0,
                    'y-coordinate': 0}
        actual = make_foes(character)
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=3)
    def test_make_foes_all_other_regions(self, _):
        character = {'x-coordinate': 0, 'y-coordinate': 24}
        expected = {'critical': 2,
                    'current_health': 12,
                    'current_level': 1,
                    'experience': 50,
                    'name': 'Midterm',
                    'reliability': 5,
                    'skill': ['Extreme Stress', 'Time Pressure', 'Midterm'],
                    'stats': {'max_damage': 8, 'max_health': 9},
                    'x-coordinate': 0,
                    'y-coordinate': 0}
        actual = make_foes(character)
        self.assertEqual(expected, actual)
