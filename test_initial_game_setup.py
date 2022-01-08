from unittest import TestCase
import io
from unittest.mock import patch
from game import initial_game_setup


class Test(TestCase):

    @patch('game.print_welcome_banner', return_value=None)
    @patch('builtins.input', side_effect=["joey wheeler", "1"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_initial_game_setup_update_user_name_to_dictionary(self, mock_output, _, __):
        initial_game_setup()
        expected_output = (
            "[38;2;149;173;215mThe smiley welcome person says, \"Nice to meet you joey wheeler, "
            "we are excited to have\n"
            "you here at BCIT. You are in for a such a great time here.  Tell me, what program are "
            "you studying?\n"
            " [38;2;255;255;255m\n"
            "[38;2;149;173;215mYou say with earnest enthusiasm, \"Computer Systems Technology "
            "Diploma, full time\"!\n"
            " [38;2;255;255;255m\n"
            "[38;2;149;173;215mErr... you see the smile on their face droop slightly.  But "
            "they quickly recover and\n"
            "say, \"Oh wow!... Yes... you are in for quite the ride, that is for certain. I am\n"
            "curious, can you enter the number corresponding to the type of student you are? "
            "[38;2;255;255;255m\n"
            "[38;2;223;77;174m\n"
            "The Opinionated One: 1\n"
            ">>>This type of student has tons of opinions and is never scared to share them.\n"
            "This student is unpredictable and has higher chance of doing critical damage, but is\n"
            "also known to miss frequently.\n"
            "\n"
            "The High Achiever: 2\n"
            ">>>This student has organization and planning down pat and their life is "
            "meticulously\n"
            "maintained by a calendar and multiple Excel spreadsheets. This student is evenly "
            "balanced\n"
            "in critical hits, reliability, and odds of missing.\n"
            "\n"
            "The Super Social One: 3\n"
            ">>>Nothing matters more to this student than having a good time with their friends!\n"
            "This character is reliable but deals low levels of damage. They also have high "
            "levels of\n"
            "health due to their strong social support network.\n"
            "\n"
            "The Quasi Professional: 4\n"
            ">>> This student has 3 years experience in python, 2 years in Java, and is fresh "
            "off an internship\n"
            "from Amazon. No one really knows why they are in CST. ¯\_(ツ)_/¯  This character "
            "is all\n"
            "or nothing and will either.\n"
            " [38;2;255;255;255m\n"
            "[38;2;149;173;215m\n"
            "The smiley committee member nods thoughtfully. \"Who knows, maybe you will last "
            "longer than the rest of the\n"
            " students who flunked out last term...\". \n"
            "\n"
            "So, joey wheeler, are you ready to start the term? Actually, it does not matter "
            "because BCIT waits for no one. One last thing\n"
            "- be aware of people stealing your Reese's Peanut Butter Cups.  If you run out, you\n"
            "automatically flunk out this term!  But you should be fine, right?\n"
            "Let's go!\n"
            " [38;2;255;255;255m\n")
        self.assertEqual(expected_output, mock_output.getvalue())
