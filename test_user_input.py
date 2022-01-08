from unittest import TestCase
from unittest.mock import patch
from game import user_input


class Test(TestCase):

    @patch('builtins.input', side_effect=['2'])
    def test_user_input_immediate_valid_response(self, _):
        input_options = ['1', '2']
        invalid = 'Invalid'
        user_prompt = 'Prompt'
        expected_output = '2'
        actual_output = user_input(input_options, invalid, user_prompt)
        self.assertEqual(expected_output, actual_output)

    @patch('builtins.input', side_effect=['4', '4', '3'])
    def test_user_input_valid_response_multiple_attempts(self, _):
        input_options = ['1', '2', '3']
        invalid = 'Your response is invalid'
        user_prompt = 'This is your input: '
        expected_output = '3'
        actual_output = user_input(input_options, invalid, user_prompt)
        self.assertEqual(expected_output, actual_output)

    @patch('builtins.input', side_effect=['grapes', 'apple'])
    def test_user_input_tuple_as_sequence(self, _):
        input_options = ('apple', 'banana', 'cherry')
        invalid = 'Your response is invalid'
        user_prompt = 'This is your input: '
        expected_output = 'apple'
        actual_output = user_input(input_options, invalid, user_prompt)
        self.assertEqual(expected_output, actual_output)
