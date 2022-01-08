import io
from unittest import TestCase
from unittest.mock import patch
from game import character_flee_sequence


class Test(TestCase):
    @patch('game.chance_generator', return_value=True)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_character_flee_sequence_escape_with_no_damage(self, mock_output, _):
        character = {'x-coordinate': 0, 'y-coordinate': 1, 'current_health': 20,
                     'reliability': 4, 'experience': 1, 'critical': 3,
                     'current_level': 1,
                     'goal_met': False, 'skill': ['Complain', 'Reason', 'Obfuscate'],
                     'stats': {'max_health': 20, 'max_damage': 7}}
        foe = {'critical': 2,
               'current_health': 7,
               'current_level': 1,
               'experience': 25,
               'name': 'Pop Quiz',
               'reliability': 5,
               'skill': ['Boredom', 'Whiplash', 'Vocabulary'],
               'stats': {'max_damage': 7, 'max_health': 7},
               'x-coordinate': 0,
               'y-coordinate': 0}
        character_flee_sequence(foe, character)
        expected = (
            "You manage to successfully escape the"
            " Pop Quiz without them taking any of your\n"
            " precious Reese's Peanut Butter Cups.\n")
        self.assertEqual(expected, mock_output.getvalue())

    @patch('game.chance_generator', return_value=False)
    @patch('random.randint', return_value=2)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_character_flee_sequence_unsuccessful_escape(self, mock_output, _, __):
        character = {'x-coordinate': 0, 'y-coordinate': 2, 'current_health': 20,
                     'reliability': 4, 'experience': 1, 'critical': 3,
                     'current_level': 1,
                     'goal_met': False, 'skill': ['Complain', 'Reason', 'Obfuscate'],
                     'stats': {'max_health': 20, 'max_damage': 7}}
        foe = {'critical': 2,
               'current_health': 7,
               'current_level': 1,
               'experience': 20,
               'name': 'Midterm',
               'reliability': 5,
               'skill': ['Boredom', 'Fright', 'Vocabulary'],
               'stats': {'max_damage': 7, 'max_health': 7},
               'x-coordinate': 0,
               'y-coordinate': 0}
        character_flee_sequence(foe, character)
        expected = ("The Midterm gestures at you menacingly and starts gliding towards you.\n"
                    "You turn around and run in the opposite direction at full speed.  In\n"
                    "the haste of your departure, you feel 2 Reese's Peanut Butter Cups\n"
                    "fall out of your pocket. Oh dear. You need those to make it through\n"
                    "the term alive. You vow to yourself to come up with a better way next\n"
                    "term to store your chocolate. You now have 18 Reese's Peanut Butter\n"
                    "Cups left.\n")
        self.assertEqual(expected, mock_output.getvalue())

    @patch('random.randint', return_value=2)
    @patch('game.chance_generator', return_value=False)
    def test_character_flee_sequence_character_dictionary_reduced_health(self, _, __):
        character = {'x-coordinate': 1, 'y-coordinate': 2, 'current_health': 20,
                     'reliability': 4, 'experience': 1, 'critical': 3,
                     'current_level': 1,
                     'goal_met': False, 'skill': ['Complain', 'Reason', 'Obfuscate'],
                     'stats': {'max_health': 20, 'max_damage': 7}}
        character_old_current_hp = character['current_health']
        foe = {'critical': 2,
               'current_health': 7,
               'current_level': 1,
               'experience': 35,
               'name': 'Communications Essay',
               'reliability': 5,
               'skill': ['Boredom', 'Carpal Tunnel', 'Vocabulary'],
               'stats': {'max_damage': 7, 'max_health': 7},
               'x-coordinate': 0,
               'y-coordinate': 0}
        character_flee_sequence(foe, character)
        expected = character['current_health'] < character_old_current_hp
        self.assertTrue(expected)

    @patch('game.chance_generator', return_value=True)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_character_flee_sequence_character_dictionary_health_unchanged(self, mock_output, _):
        character = {'x-coordinate': 1, 'y-coordinate': 1, 'current_health': 20,
                     'reliability': 4, 'experience': 1, 'critical': 3,
                     'current_level': 1,
                     'goal_met': False, 'skill': ['Complain', 'Reason', 'Obfuscate'],
                     'stats': {'max_health': 20, 'max_damage': 7}}
        character_old_current_hp = character['current_health']
        foe = {'critical': 2,
               'current_health': 7,
               'current_level': 1,
               'experience': 30,
               'name': 'Communications Essay',
               'reliability': 5,
               'skill': ['Boredom', 'Carpal Tunnel', 'Vocabulary'],
               'stats': {'max_damage': 7, 'max_health': 7},
               'x-coordinate': 0,
               'y-coordinate': 0}
        character_flee_sequence(foe, character)
        expected = character['current_health'] == character_old_current_hp
        self.assertTrue(expected)
