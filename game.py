"""
Your name: Christie Tsang
Your student number: A01290679

All of your code must go in this file.
"""
import copy
import itertools
import random
import sys
import textwrap
from operator import add
from typing import Union
import time

MINIMUM_DIMENSIONS = 25


# <editor-fold desc="Initial Game Setup">
def print_welcome_banner() -> None:
    """
    Print colored ASCII art.
    """
    print(colorizer(255, 153, 255, r"""                                                                                          
,-----.  ,-----,--,--------.     ,---. ,--,--.   ,--,--. ,--,--.    ,---.,--------.,-----.,------.  
|  |) /_'  .--.|  '--.  .--'    '   .-'|  |   `.'   |  | |  |  |   /  O  '--.  .--'  .-.  |  .--. ' 
|  .-.  |  |   |  |  |  |       `.  `-.|  |  |'.'|  |  | |  |  |  |  .-.  | |  |  |  | |  |  '--'.' 
|  '--' '  '--'|  |  |  |       .-'    |  |  |   |  '  '-'  |  '--|  | |  | |  |  '  '-'  |  |\  \  
`------' `-----`--'  `--'       `-----'`--`--'   `--'`-----'`-----`--' `--' `--'   `-----'`--' '--'                                                                       
    """))


def initial_game_setup() -> dict:
    """
    Initiate game setup.

    :postcondition: correctly return a character dictionary representing the class the user has
                    selected
    :return: a well formed character dictionary containing the character statistics representing
            the class that the user has selected
    """
    print_welcome_banner()
    user_name = input(colorizer(149, 173, 215,
                                f'It is the first Monday after the Labour Day Weekend in '
                                f'September as you take your first step\npast the sliding doors '
                                f'of BCIT: Downtown Campus.Filled with excitement and anticipation,'
                                f'\nyou walk over to a smiling member of the Welcome Committee and '
                                f'introduce yourself. "Hello!,\nmy name is...\n\nInput your '
                                f'character name:'))
    print(colorizer(149, 173, 215, f'The smiley welcome person says, "Nice to meet you'
                                   f' {user_name}, we are excited to have\nyou here at BCIT. You '
                                   f'are in for a such a great time here.  Tell me, what program '
                                   f'are you studying?\n'))
    time.sleep(4)
    print(colorizer(149, 173, 215, f'You say with earnest enthusiasm, "Computer Systems '
                                   f'Technology Diploma, full time"!\n'))
    time.sleep(3)
    print(colorizer(149, 173, 215, 'Err... you see the smile on their face droop slightly.  But '
                                   'they quickly recover and\nsay, "Oh wow!... Yes... you are in '
                                   'for quite the ride, that is for certain. I am\ncurious, can '
                                   'you enter the number corresponding to the type of student you '
                                   'are?'))

    print(colorizer(223, 77, 174,
                    '\nThe Opinionated One: 1\n>>>This type of student has tons of opinions and is '
                    'never scared to share them.\nThis student is unpredictable and has higher '
                    'chance of doing critical damage, but is\nalso known to miss frequently.\n'

                    '\nThe High Achiever: 2\n>>>This student has organization and planning down '
                    'pat and their life is meticulously\nmaintained by a calendar and multiple '
                    'Excel spreadsheets. This student is evenly balanced\nin critical hits, '
                    'reliability, and odds of missing.\n'

                    '\nThe Super Social One: 3\n>>>Nothing matters more to this student than '
                    'having a good time with their friends!\nThis character is reliable but deals '
                    'low levels of damage. They also have high levels of\nhealth due to their '
                    'strong social support network.\n'

                    '\nThe Quasi Professional: 4\n>>> This student has 3 years experience in '
                    'python, 2 years in Java, and is fresh off an internship\nfrom Amazon. No one '
                    'really knows why they are in CST. ¯\\_(ツ)_/¯  This character is all\nor '
                    'nothing and will either.\n'))

    user_choice = user_input(["1", "2", "3", "4"], f'The welcome person smiles ruefully at you and '
                                                   f'says "I am sorry, but you have choose a '
                                                   f'number between 1 and 4.\nPlease try '
                                                   f'again, won\'t you?"\nInput: ')
    character_dictionary = make_character(user_choice)
    print(colorizer(149, 173, 215,
                    f'\nThe smiley committee member nods thoughtfully. "Who knows, maybe you will '
                    f'last longer than the rest of the\n students who flunked out last term...". '
                    f'\n\nSo, {user_name}, are you ready to start the term? Actually, it does not '
                    f'matter because BCIT waits for no one. One last thing\n- be aware of people '
                    f'stealing your Reese\'s Peanut Butter Cups.  If you run out, you\n'
                    f'automatically flunk out this term!  But you should be fine, right?\nLet\'s '
                    f'go!\n'))
    time.sleep(4)
    character_dictionary.update({'name': user_name})
    return character_dictionary


def make_character(user_choice: str) -> dict:
    """
    Create a character.

    :param user_choice: a string
    :precondition: must be a number between [1, 4], inclusive, as a string
    :postcondition: correctly generate and return the corresponding character dictionary,
                    which must be well formed
                    the skills and attributes of the corresponding class
    :return: a character dictionary
    """
    class_opinion = {'x-coordinate': 0, 'y-coordinate': 0, 'current_health': 20, 'experience': 1,
                     'reliability': 4, 'critical': 3, 'current_level': 1, 'goal_met': False,
                     'skill': ['Complain', 'Reason', 'Obfuscate'],
                     'stats': {'max_health': 20, 'max_damage': 7},
                     'experience_per_level': {'Opinionated Student': 0, 'Outspoken Set Rep': 70,
                                              'Assertive Leader': 120}}

    class_achieve = {'x-coordinate': 0, 'y-coordinate': 0, 'current_health': 66, 'experience': 1,
                     'reliability': 5, 'critical': 3, 'current_level': 1, 'goal_met': False,
                     'skill': ['Efficiency', 'Asked Questions', 'Time Management'],
                     'stats': {'max_health': 22, 'max_damage': 5},
                     'experience_per_level': {'High Achiever': 0, 'Budding Entrepreneur': 60,
                                              'Valedictorian': 130}}

    class_social = {'x-coordinate': 0, 'y-coordinate': 0, 'current_health': 99, 'experience': 1,
                    'reliability': 7, 'critical': 1, 'current_level': 1, 'goal_met': False,
                    'skill': ['Teamwork', 'Flattery', 'Call In Favours'],
                    'stats': {'max_health': 99, 'max_damage': 3},
                    'experience_per_level': {'Social Classmate': 0, 'Social Butterfly': 55,
                                             'Networking Guru': 110}}

    class_experience = {'x-coordinate': 0, 'y-coordinate': 0, 'current_health': 60, 'experience': 1,
                        'reliability': 1, 'critical': 5, 'current_level': 1, 'goal_met': False,
                        'skill': ['Past Projects', 'Networking', 'Wisdom'],
                        'stats': {'max_health': 60, 'max_damage': 15},
                        'experience_per_level': {'Experienced Student': 0,
                                                 'Proficient Programmer': 70, 'Qualified '
                                                                              'Developer': 125}}

    all_classes = {'1': class_opinion, '2': class_achieve, '3': class_social, '4': class_experience}
    return all_classes[user_choice]


def colorizer(red: int, blue: int, green: int, string: str) -> str:
    """
    Apply color formatting to string.

    :param red: an integer representing red in RGB color
    :param blue: an integer representing blue in RGB color
    :param green: an integer representing green in RGB color
    :param string: a string sequence
    :precondition: red must be an integer between [0, 255]
    :precondition: blue must be an integer between [0, 255]
    :precondition: green must be an integer between [0, 255]
    :precondition: string must be a string sequence
    :postcondition: correctly apply color formatting to a string sequence
    :return: a string
    """
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(red, blue, green, string)


def user_input(input_options, invalid_response: str, prompt: str = f'Input: ') -> str:
    """
    Prompt and validate user input.

    :param input_options: must be a sequence of string elements
    :param invalid_response: must be a string
    :param prompt: must be a string; prompt is an optional parameter
    :precondition: input_options must be a sequence of string elements, must be a non-empty sequence
    :precondition: invalid_response must be a non-empty string
    :precondition: prompt must be a string; if no arguments are passed, the default value is
                    'Input: '
    :postcondition: continue to prompt user for a valid response until user enters a value found in
                    user_input
    :return: the user's input as a string
    """
    user_choice = input(prompt)

    while user_choice not in input_options:
        user_choice = input(invalid_response)

    return user_choice


# </editor-fold>


# <editor-fold desc="Map Creation">
def select_random_room() -> str:
    """
    Generate randomized room descriptions.

    :postcondition: correctly generate randomly selected room descriptions as a string
    :return: a randomly selected string
    """
    rooms = [f'You walk in the hallways between the elevators and the anti-social high chairs '
             f'that\nface the wall.\n',

             f'You walk down a dimly lit hallway on the 6th floor and pass the lunch room on your '
             f'way to\nthe stairs.\n',

             f'On the way to the restroom, you pass by a gaggle of students from the other sets '
             f'mingling\nabout in the hallways.\n',

             f'You pull open the door and walk into a bustling classroom filled with chattering '
             f'students.\n',

             f'You tap your BCIT ID against the card reader and walk into a group study room.  '
             f'Inside,\nyou see a number of weary looking students hunched over their laptops with '
             f'their hands\ncradling their face.  You think to yourself that this is a familiar '
             f'sight at BCIT.\n',

             f'You walk into a brightly lit gym with padded floors. Each piece of new equipment '
             f'has been\nencircled with yellow caution tape with a piece of paper haphazardly taped'
             f' on top, stating\n"CLOSED DUE TO COVID". You wonder to yourself why you pay rec fees'
             f' when you can\'t even\nuse rec services.\n']
    return rooms[random.randint(0, 5)]


def map_room_descriptions(rows: int, columns: int) -> dict:
    """
    Create board with rows and columns.

    :param rows: a positive, non-zero integer
    :param columns: a positive, non-zero integer
    :precondition: rows must be a positive, non-zero integer equal to or greater than 2
    :precondition: columns must be a positive, non-zero integer equal to or greater than 2
    :postcondition: create a correctly generated dictionary where each key is a unique set of
                    coordinates mapped to values represented by randomly selected string
                    descriptions
    :postcondition: all possible unique combinations of rows and columns will be assigned as
                    dictionary keys, where value in rows range from [0, rows], and value in
                    columns range from [0, columns]
    :postcondition: must create and return a dictionary that contains rows * columns number of keys
    :postcondition: dictionary is created with keys sorted from smallest to largest
    :return: a dictionary where each key is a tuple containing a set of coordinates and is paired
            with a value represented by a string

    # Rows and columns are smallest positive, non-zero integer
    >>> number_of_keys = map_room_descriptions(2, 2)
    >>> len(number_of_keys)
    4

    # Rows and columns are unequal numbers
    >>> number_of_keys = map_room_descriptions(3, 5)
    >>> len(number_of_keys)
    15
    """
    # Map randomly selected rooms to coordinates
    return {(row, column): select_random_room() for row in range(rows) for column in range(columns)}


def display_map(character: dict, room_descriptions: dict) -> None:
    """
    Print map to terminal.

    :param character: must be a well formed character dictionary
    :param room_descriptions: must be a dictionary with coordinates as keys and room
                                descriptions as values
    :precondition: character must be a well formed character dictionary containing the keys
                    "x-coordinate" and "y-coordinate" and the corresponding values are positive
                    or negative integers
    :precondition: room_descriptions must be a correctly generated dictionary where each key is a
                    unique set of coordinates and is mapped to values represented by randomly
                    selected string descriptions
    :postcondition: correctly print a 10 x 10 grid of symbols representing rooms in a map
    """
    displayed_symbols = generate_symbols(character, room_descriptions)
    for room, characters in enumerate(displayed_symbols):

        # Print and join symbols in the same row
        characters = displayed_symbols[room]
        if (room + 1) % 10 != 0:
            if characters == "⟐":
                print(colorizer(255, 0, 0, characters), end='')
            elif characters == "₪":
                print(colorizer(71, 71, 107, characters), end='')
            else:
                print(characters, end=' ')

        # Print symbol and move to a new line
        else:
            if characters == "₪":
                print(colorizer(71, 71, 107, characters))
            else:
                print(characters)


def generate_symbols(character: dict, room_descriptions: dict) -> list:
    """
    Append symbols that represent rooms to a list.

    :param character: must be a well formed character dictionary
    :param room_descriptions: must be a dictionary with coordinates as keys and room
                                descriptions as values
    :precondition: character must be a well formed character dictionary containing the keys
                    "x-coordinate" and "y-coordinate" and the corresponding values are positive
                    or negative integers
    :precondition: room_descriptions must be a correctly generated dictionary where each key is a
                    unique set of coordinates and is mapped to values represented by string
                    descriptions
    :postcondition: correctly append symbols to a list based on a symbol dictionary,
                    map coordinates, and room descriptions; character dictionary and
                    room_descriptions is unchanged
    :return: a list of string elements, where each element is a symbol
    """
    symbol_dictionary = {
        f'You walk in the hallways between the elevators and the anti-social high chairs '
        f'that\nface the wall.\n': '⊙',

        f'You walk down a dimly lit hallway on the 6th floor and pass the lunch room on your '
        f'way to\nthe stairs.\n': '⊙',

        f'On the way to the restroom, you pass by a gaggle of students from the other sets '
        f'mingling\nabout in the hallways.\n': '⊙',

        f'You pull open the door and walk into a bustling classroom filled with chattering '
        f'students.\n': '.',

        f'You tap your BCIT ID against the card reader and walk into a group study room.  '
        f'Inside,\nyou see a number of weary looking students hunched over their laptops with '
        f'their hands\ncradling their face.  You think to yourself that this is a familiar '
        f'sight at BCIT.\n': '⊗',

        f'You walk into a brightly lit gym with padded floors. Each piece of new equipment '
        f'has been\nencircled with yellow caution tape with a piece of paper haphazardly taped'
        f' on top, stating\n"CLOSED DUE TO COVID". You wonder to yourself why you pay rec fees'
        f' when you can\'t even\nuse rec services.\n': '+'}

    symbol_list = []
    displayed_map = range_of_displayed_coordinates(character)

    # Map symbols to empty list based on corresponding room descriptions
    for room in range(100):
        coordinates = displayed_map[room]

        if coordinates == (character['x-coordinate'], character['y-coordinate']):
            symbol_list.append("⟐")

        elif coordinates not in room_descriptions:
            symbol_list.append("₪")

        else:
            symbol_list.append(symbol_dictionary[room_descriptions[coordinates]])

    return symbol_list


def range_of_displayed_coordinates(character: dict) -> list:
    """
    Generate a list of the character's surrounding coordinates as a list of tuples.

    :param character: must be a well formed character dictionary
    :precondition: character must be a well formed character dictionary containing the keys
                    "x-coordinate" and "y-coordinate" and the corresponding values are positive
                    or negative integers
    :postcondition: correctly generate and return a list of 100 tuples - each containing two
                    positive integers, in the 10 by 10 grid encompassing the character's coordinates
    :postcondition: tuples are sorted smallest to largest
    :return: a list of 100 tuples representing coordinates
    """
    x_vector, y_vector = (character['x-coordinate'] - 4, character['y-coordinate'] - 4)

    # Create a list of coordinates around character's location
    return [(x, y) for x in range(x_vector, x_vector + 10) for y in range(y_vector, y_vector + 10)]


# </editor-fold>


# <editor-fold desc="Character Movement">
def describe_current_location(room_descriptions: dict, character: dict) -> None:
    """
    Print text description of character's location.

    :param room_descriptions: must be a well formed dictionary
    :param character: must be a well formed character dictionary
    :precondition: room_descriptions must be a correctly generated dictionary where each key is a
                    unique set of coordinates and is mapped to values represented by randomly
                    selected string descriptions
    :precondition: character must be a well formed character dictionary containing the keys
                    "x-coordinate" and "y-coordinate" and the corresponding values are positive
                    or negative integers
    :postcondition: correctly print text description of character's current location
    :postcondition: character dictionary and room_descriptions dictionary must be unchanged
    """

    character_location = (character['x-coordinate'], character['y-coordinate'])

    print(colorizer(255, 255, 179, f'{room_descriptions[character_location]}\nA short and '
                                   f'bubbly girl passes you at your elbow and tells you cheerfully '
                                   f'that you are location {character_location} \nAre people here '
                                   f'always that friendly?\n'))


def direction_input() -> Union[tuple, str]:
    """
    Prompt user for direction input.

    "North" is represented by (-1, 0); "east" by (0, 1); "south" by (1, 0), "west" by (0, -1).

    :postcondition: accepts user input as dictionary key and returns the corresponding value as
                    either coordinate tuples, or a number as string
    :return: coordinates as a tuple, or a number as a string
    """
    movement_coordinates = {'w': (-1, 0), 'd': (0, 1), 's': (1, 0), 'a': (0, -1), '1': '1',
                            '2': '2', 'quit': '3'}

    user_choice = user_input(['w', 'a', 's', 'd', '1', '2', 'quit'], textwrap.fill(
        f'You shake your head in confusion.  Maybe it\'s because you haven not had coffee yet, but '
        f'you are sure there are very specific things you should be doing while at school.  '
        f'Maybe entering "1" will help you figure it out. \nInput: ', width=100,
        replace_whitespace=False),
                             colorizer(153, 204, 255, f'\nWhat do you want to do next? ('
                                                      f'Enter "w,a,s,d" to travel in that '
                                                      f'direction, or enter 1 to '
                                                      f'see a list of options)\n'))

    return movement_coordinates[user_choice]


def command_options(character: dict, user_command: str) -> None:
    """
    Print command options or character information for player.

    :param character: must be a character dictionary
    :param user_command: must be string
    :precondition: character must be a well formed character dictionary containing the keys
                    "x-coordinate" and "y-coordinate" and the corresponding values are positive
                    or negative integers; must contain the keys 'current_level'
    :precondition: user_command must either be '7' or '9'
    :postcondition: correctly print requested information for the player
    """
    if user_command == '1':
        print_travel_commands()  # Print list of valid options

    elif user_command == '2':  # Print character statistics
        current_level = character['current_level'] - 1
        #
        level_description = list(character['experience_per_level'].keys())[current_level]

        print(colorizer(153, 204, 255, f'\nCurrent Level: {current_level + 1} - {level_description}'
                                       f'\nHealth: {character["current_health"]} Peanut Butter Cups'
                                       f'\nExperience: {character["experience"]}'
                                       f'\nMax Damage: {character["stats"]["max_damage"]}'
                                       f'\nSkills: {character["skill"]}'))


def print_travel_commands() -> None:
    """
    Print valid input options to terminal.
    """
    print(colorizer(153, 204, 255, f'You take out the piece of paper the welcome committee member '
                                   f'gave to you and reference it for clues what to do next.\n'
                                   f'###################################################\n'
                                   f'                  COMMAND OPTIONS                   \n'
                                   f'###################################################\n'
                                   f'DIRECTION INPUT\n'
                                   f'a : West\n'
                                   f'w : North\n'
                                   f'd : East\n'
                                   f's : South\n'
                                   f'OTHER OPTIONS\n'
                                   f'1 : See Command options\n'
                                   f'2 : See your character stats\n'
                                   f'quit : Exit the game\n'))


def validate_move(room_descriptions: dict, character: dict, user_direction: tuple) -> bool:
    """
    Check if character's intended move is valid.

    :param room_descriptions: must be a well formed dictionary
    :param character: must be a well formed character dictionary
    :param user_direction: must be a tuple
    :precondition: room_descriptions must be a correctly generated dictionary where each key is a
                    unique set of coordinates and is mapped to string descriptions as values
    :precondition: character must be a well formed character dictionary containing the keys
                    "x-coordinate" and "y-coordinate" and the corresponding values are positive
                    integers
    :precondition: user_direction must be a tuple with two integers
    :postcondition: returns True if the sum of character coordinates and user_direction
                    coordinates exists as a key in room_descriptions dictionary, else False
    :postcondition: board and character dictionary must be unchanged
    :return: a Boolean value of either True or False

    # sum of two tuples exists in board dictionary
    >>> board = {(0, 0): 'text', (0, 1): 'text', (1, 0): 'text', (1, 1): 'text'}
    >>> char_location = {"x-coordinate": 0, "y-coordinate": 0, "current_health": 5}
    >>> users = (0, 1)
    >>> validate_move(board, char_location, users)
    True

    # sum of two tuples does not exist in board dictionary
    >>> board = {(0, 0): 'text', (0, 1): 'text', (1, 0): 'text', (1, 1): 'text'}
    >>> char_location = {"x-coordinate": 0, "y-coordinate": 4, "current_health": 5}
    >>> users = (0, 1)
    >>> validate_move(board, char_location, users)
    False
    """
    new_coordinates = calculate_new_coordinates(character, user_direction)
    return new_coordinates in room_descriptions.keys()


def calculate_new_coordinates(character: dict, user_direction: tuple) -> tuple:
    """
    Calculate new character coordinates.

    :param character: must be a dictionary
    :param user_direction: must be a tuple
    :precondition: character must be a well formed character dictionary containing the keys
                    "x-coordinate" and "y-coordinate" and the corresponding values are positive
                    or negative integers
    :precondition: user_direction must be a tuple with two integers
    :postcondition: correctly sum the character's existing coordinates and user_direction
                    coordinates to calculate the character's new location in the grid
    :postcondition: character dictionary must be unchanged
    :return: a tuple representing the character's new location in the grid

    # Calculate with large numbers
    >>> user_input_coordinates = (10, 15)
    >>> character_location = {"x-coordinate": 0, "y-coordinate": 1, "current_health": 5}
    >>> calculate_new_coordinates(character_location, user_input_coordinates)
    (10, 16)

    # Calculate with small numbers
    >>> user_input_coordinates = (0, 0)
    >>> character_location = {"x-coordinate": 0, "y-coordinate": 1, "current_health": 5}
    >>> calculate_new_coordinates(character_location, user_input_coordinates)
    (0, 1)
    """
    current_location = (character['x-coordinate'], character['y-coordinate'])
    new_coordinates = tuple(map(add, user_direction, current_location))  # Add coordinates together
    return new_coordinates


def move_character(character: dict, user_direction: tuple) -> None:
    """
    Update character dictionary with new coordinates.

    :param character: must be a dictionary
    :param user_direction: must be a tuple
    :precondition: character must be a well formed character dictionary containing the keys
                    "x-coordinate" and "y-coordinate" and the corresponding values are positive
                    or negative integers
    :precondition: user_direction must be a tuple with two integers
    :postcondition: correctly update character dictionary with new coordinates
    """
    new_coordinates = calculate_new_coordinates(character, user_direction)

    character["x-coordinate"] = new_coordinates[0]
    character["y-coordinate"] = new_coordinates[1]


def print_invalid_movement() -> None:
    """
    Inform player their input for movement is invalid.
    """
    print(textwrap.fill(f'You tap your BCIT ID against the card reader, but the door in '
                        f'front of you stays resolutely closed.  You shrug, thinking that '
                        f'it is for the best anyways as you have a nagging feeling that if '
                        f'someone had let you travel that way, you would automatically fail '
                        f'your assignment with Chris.  And that would NOT be good, no, '
                        f'not at all.\n'))


# </editor-fold>


# <editor-fold desc="Foes and Combat">
def health_regeneration(character: dict) -> None:
    """
    Regenerate character health.

    :param character: must be a well formed dictionary
    :precondition: character must be a well formed dictionary with the keys 'current_health' and
                    'max_health'
    :postcondition: correctly increase character's current health if character's current_health
    is less than their max_health
    """
    # Regenerate health if character's health is less than the maximum
    if character['current_health'] < character['stats']['max_health']:
        regenerate = character['current_level'] + 1
        character['current_health'] += regenerate

        # Ensure character health does not exceed the maximum
        if character['current_health'] > character['stats']['max_health']:
            character['current_health'] = character['stats']['max_health']

        print(colorizer(223, 77, 174, f'You have regained {regenerate} Peanut Butter Cup. You now '
                                      f'have {character["current_health"]} left.'))


def scale_foe_to_level(character: dict) -> dict:
    """
    Scale foe's stats based on character's current level.

    :param character: must be a well formed character dictionary
    :precondition: character must be a well formed character dictionary containing the key
                    current_level; and it's corresponding value must be an integer
    :postcondition: correctly increase the foe's level and stats if the foe's level is less than
                    the character's current level
    :return: a foe dictionary
    """
    # Generate a foe
    foe = make_foes(character)

    if foe['name'] == 'Finals':

        return foe

    elif foe['current_level'] < character['current_level']:
        difference = character['current_level'] - foe['current_level']

        # Increase foe's level, health, damage based on character's level
        foe['current_level'] += difference
        foe['current_health'] *= (difference + 1)

        foe['stats']['max_damage'] *= (difference + 1)
        foe['stats']['max_health'] *= (difference + 1)

    return foe


def make_foes(character: dict) -> dict:
    """
    Generate a foe.

    :param character: must be a well formed character dictionary
    :precondition: character must be a well formed character dictionary containing the keys
                    "x-coordinate" and "y-coordinate" and the corresponding values are positive
                    or negative integers
    :postcondition: correctly return a foe dictionary representing the skills and attributes of a
                    foe from the character's corresponding region
    :return: a dictionary representing the skills and attributes of a foe
    """
    pop_quiz = {'x-coordinate': 0, 'y-coordinate': 0, 'current_health': 7, 'experience': 20,
                'reliability': 5, 'critical': 2, 'name': 'Pop Quiz', 'current_level': 1,
                'skill': ['Surprise', 'Confuse', 'Shock'],
                'stats': {'max_health': 3, 'max_damage': 2}}

    essay = {'x-coordinate': 0, 'y-coordinate': 0, 'current_health': 10, 'experience': 25,
             'reliability': 5, 'critical': 2, 'name': 'Communications Essay', 'current_level': 1,
             'skill': ['Boredom', 'Carpal Tunnel', 'Vocabulary'],
             'stats': {'max_health': 6, 'max_damage': 5}}

    clean_staff = {'x-coordinate': 0, 'y-coordinate': 0, 'current_health': 10, 'experience': 35,
                   'reliability': 5, 'critical': 2, 'name': 'Cleaning Lady', 'current_level': 1,
                   'skill': ['Chemicals', 'Eject from Building', 'Cleaning Equipment'],
                   'stats': {'max_health': 7, 'max_damage': 7}}

    midterm = {'x-coordinate': 0, 'y-coordinate': 0, 'current_health': 12, 'experience': 50,
               'reliability': 5, 'critical': 2, 'name': 'Midterm', 'current_level': 1,
               'skill': ['Extreme Stress', 'Time Pressure', 'Midterm'],
               'stats': {'max_health': 9, 'max_damage': 8}}

    boss = {'x-coordinate': 0, 'y-coordinate': 0, 'current_health': 50, 'experience': 60,
            'reliability': 5, 'critical': 4, 'name': 'Finals', 'current_level': 3,
            'skill': ['Extreme Stress', 'Time Pressure', 'Sleep Deprivation'],
            'stats': {'max_health': 60, 'max_damage': 17}}

    all_classes = [pop_quiz, essay, clean_staff, midterm]

    # Check for character's current coordinates
    new_coordinates = (character['x-coordinate'], character['y-coordinate'])

    if new_coordinates == (20, 21):
        return boss

    # Return only specific foes if character coordinates are between (0, 0) and (12, 12), inclusive
    elif new_coordinates in list((itertools.product(range(13), repeat=2))):
        return all_classes[random.randint(0, 1)]

    elif new_coordinates in list((itertools.product(range(13, 26), repeat=2))):
        return all_classes[random.randint(1, 2)]

    else:
        return all_classes[random.randint(2, 3)]


def chance_generator(character: dict) -> bool:
    """
    Create a 20% chance for an event to occur.

    :param character: must be a well formed character dictionary
    :precondition: character must be a well formed character dictionary containing the keys
                    "x-coordinate" and "y-coordinate" and the corresponding values are positive
                    or negative integers
    :postcondition: must return True if character coordinates are (20, 21)
    :postcondition: return True if randomly generated number within the range [1,5], inclusive, is
                    equal to 1, else False
    :return: a Boolean value of either True or False
    """
    # Character will always fight when encountering boss
    if (character['x-coordinate'], character['y-coordinate']) == (20, 21):
        return True

    else:
        return random.randint(1, 5) == 1


def fight_or_flee(foe: dict, character: dict) -> None:
    """
    Asks character if they want to fight or flee from foe.

    :param foe: must be a well formed foe dictionary
    :param character: must be a well formed character dictionary
    :precondition: foe must be a well formed foe dictionary
    :precondition: character must be a well formed character dictionary containing the keys
                "x-coordinate" and "y-coordinate" and the corresponding values are positive
                or negative integers
    :postcondition: correctly route character to the corresponding battle or flee dialogue based on
                    user input
    :postcondition: character will not be given a choice to flee if the foe is 'Finals'
    """
    if foe['name'] == 'Finals':
        print(colorizer(
            198, 45, 45, f'You push open the double doors and stride into the classroom, '
                         f'ready for your finals.\nBefore you, stands your Final Exam. You '
                         f'gulp in anticipation. Which of the following attacks would\nyou like to '
                         f'choose?'))

        battle_gameplay(foe, character)

    else:
        user_choice = user_input(['1', '2'], colorizer(
            198, 45, 45, f'\nThe {foe["name"]} gestures at you, saying "I know it is a tough '
                         f'decision but\nyou gotta decide. Are we doing this today or '
                         f'what?\n 1 : Yes   //   2 : No\n Input: '), colorizer(
            198, 45, 45,
            f'You have encountered a {foe["name"]}, are you ready to face it? \n1 : '
            f'Yes   //   2 : No\nInput: '))

        if user_choice == '1':
            battle_gameplay(foe, character)

        else:
            character_flee_sequence(foe, character)


def character_flee_sequence(foe: dict, character: dict) -> None:
    """
    Determine if character takes damage when fleeing.

    :param foe: must be a well formed foe dictionary
    :param character: must be a well formed character dictionary
    :precondition: character must be a well formed character dictionary containing the key
                    'current_health'
    :precondition: foe must be a well formed foe dictionary containing the keys 'name', 'stats', 
                    and the key 'max_damage' within a nested dictionary
    :postcondition: reduce current_health in character dictionary if chance generator is equal to
                    False; else, the character escapes without losing health
    """
    if chance_generator(character):
        print(f'You manage to successfully escape the {foe["name"]} without them taking any of '
              f'your\n precious Reese\'s Peanut Butter Cups.')

    else:
        lost_health = random.randint(1, foe['stats']['max_damage'])
        character['current_health'] -= lost_health

        # Prevents character health from being negative
        if character['current_health'] < 0:
            character['current_health'] = 0

        character_health = character['current_health']

        print(textwrap.fill(
            f'The {foe["name"]} gestures at you menacingly and starts gliding towards you. You '
            f'turn around and run in the opposite direction at full speed.  In the haste of your '
            f'departure, you feel {lost_health} Reese\'s Peanut Butter Cups fall out of your '
            f'pocket. Oh dear. You need those to make it through the term alive. You vow to '
            f'yourself to come up with a better way next term to store your chocolate. You now have'
            f' {character_health} Reese\'s Peanut Butter Cups left.'))


def enumerate_skills(character: dict, foe: dict) -> str:
    """
    Print numbered list of character skills.

    :param character: must be a well formed character dictionary
    :param foe: must be a well formed foe dictionary
    :precondition: character must be a well formed character dictionary containing the key
                    'skills' where the corresponding value is a list
    :precondition: foe must be a well formed foe dictionary containing the key 'name'
    :postcondition: correctly enumerate and print the skills of a character
    :postcondition: list of skills printed must not contain 'flee' if the foe is 'Finals'
    :postcondition: character and foe dictionary must be unchanged
    :return: a single string element
    """
    attack_choices = []
    if foe['name'] == 'Finals':
        regular_skills = (character["skill"])  # No option to flee when facing boss

    else:
        regular_skills = copy.copy(character["skill"])
        regular_skills.append('Flee')

    for index, skill in enumerate(regular_skills, start=1):
        print(colorizer(198, 45, 45, str(index)), colorizer(198, 45, 45, skill))
        attack_choices.append(str(index))  # Enumerate character skills

    user_choice = user_input(attack_choices,
                             f'\nYou make a sudden jerking motion then stare at your '
                             f'hands in confusion.  You should probably use one of the '
                             f'skills you know, \nSelect which skill you would like to '
                             f'use: \nInput: ')
    return user_choice


def calculate_damage(attacker: dict, target: dict) -> None:
    """
    Calculate damage in character and foe battle.

    :param attacker: must be a well formed character or foe dictionary
    :param target: must be a well formed character or foe dictionary
    :precondition: attacker must be a well formed character or foe dictionary containing the keys
                    'name', 'reliability', 'critical', and 'stats'; the corresponding value for
                    stats  must  contain the nested key 'max_damage'
    :precondition: target must be a well formed character or foe dictionary containing the keys
                    'current_health' and 'name'
    :postcondition: correctly calculate damage in the character and foe battle
    :postcondition: damage must be correctly subtracted from the target's current_health
    :postcondition: target must not have negative health at the end of the battle
    """
    regular_attack = attacker['reliability']
    critical_hit = attacker['critical']

    # Create opportunity for critical hit
    if random.randint(1, 8) in range(1, critical_hit + 1):
        damage = attacker['stats']['max_damage']

    # Create opportunity for a regular hit
    elif random.randint(1, 8) in range(1, regular_attack + 1):
        damage = random.randint(critical_hit, attacker['stats']['max_damage'])

    else:
        damage = int(attacker['stats']['max_damage'] / 3)

    # Subtract health from target
    target['current_health'] -= damage

    # Prevents target health from being negative
    if target['current_health'] < 0:
        target['current_health'] = 0

    if attacker['name'] in ['Pop Quiz', 'Communications Essay', 'Cleaning Lady', 'Midterm',
                            'Finals']:
        print(colorizer(198, 45, 45, f'{attacker["name"]} used '
                                     f'{attacker["skill"][random.randint(0, 2)]} to steal'
                                     f' {damage} Reese\'s Peanut Butter Cups from {target["name"]}'
                                     f'\n'))

    else:
        print(colorizer(198, 45, 45, f'\n{attacker["name"]} dealt {damage} damage to '
                                     f'{target["name"]}\n'))


def battle_gameplay(foe: dict, character: dict) -> None:
    """
    Facilitate a battle between character and foe.

    :param character: must be a well formed character dictionary
    :param foe: must be a well formed foe dictionary
    :precondition: character must be a well formed character dictionary containing the keys 'name',
                    'current_health', 'current_level', 'goal_met'
    :precondition: foe must be a well formed foe dictionary containing the key 'current_health' and
                    'name'
    :postcondition: correctly alternate between foe and character attacks until current_health
                    for one entity is 0, or either the character or foe flees
    :postcondition: set goal_met in character dictionary to True if character battles and
                    defeats 'Finals'
    :postcondition: set goal_met in character dictionary to True if character battles and
                    defeats 'Finals'
    """
    while is_alive(character) and is_alive(foe):
        # Print character skills
        user_choice = enumerate_skills(character, foe)

        if user_choice in ['1', '2', '3']:
            calculate_damage(character, foe)

            if is_alive(foe):
                calculate_damage(foe, character)

            print(colorizer(198, 45, 45,
                            f'{character["name"]} has {character["current_health"]} Reese\'s '
                            f'Peanut Butter Cups left.\n\nYour {foe["name"]} has '
                            f'{foe["current_health"]} health left.'))  # Print health information

            # Create opportunity for foe to flee
            if chance_generator(character) and foe['name'] != 'Finals' and is_alive(character) \
                    and is_alive(foe):
                print(colorizer(198, 45, 45, f'\n{foe["name"]} has fled'))
                return

        else:
            character_flee_sequence(foe, character)  # Character chooses to flee
            return

        if not is_alive(foe) and foe['name'] == 'Finals':
            character['goal_met'] = True

        elif not is_alive(foe):
            character_level_up_experience(character, foe)


def character_level_up_experience(character: dict, foe: dict) -> None:
    """
    Update experience and level in character dictionary.

    :param character: must be a well formed character dictionary
    :param foe: must be a well formed foe dictionary
    :precondition: character must be a well formed character dictionary containing the keys
                    'experience', 'current_level', 'experience_per_level', 'stats'
    :precondition: foe must be a well formed foe dictionary containing the key 'experience' and
                    'name'
    :postcondition: correctly update character experience in character dictionary
    :postcondition: correctly increase current_level in character dictionary if character has
                    met the experience threshold
    :postcondition: correctly increase the character's stats in the character dictionary if
                    character levels up
    """
    # Update character's experience
    character['experience'] += foe['experience']
    print(f'\n{foe["name"]} has died and you have gained {foe["experience"]} experience.\n')

    if character['current_level'] < 3:
        experience_needed = character['experience_per_level']

        # Check if character experience meets the threshold to level up
        if character['experience'] >= list(experience_needed.values())[character['current_level']]:

            for index in character['stats']:
                character['stats'][index] *= 2

            #Increase character statistics
            character['current_level'] += 1
            character['experience'] = 0
            character['current_health'] = character['stats']['max_health']

            print(f'Congratulations, you have leveled up to {character["current_level"]}.  Your '
                  f'new stats are:\n{character["stats"]}.\nYour pocket has been completely '
                  f'filled to the brim with Reese\'s.  Yummy.')


# </editor-fold>


# <editor-fold desc="Game End">
def is_alive(entity: dict) -> bool:
    """
    Check if the entity's current health is greater than 0.

    :param entity: must be a character or foe dictionary
    :precondition: entity must be a well formed character or foe dictionary containing the keys
                "x-coordinate" and "y-coordinate" and the corresponding values are positive
                or negative integers
    :postcondition: must correctly return True if curren_health is strictly greater than 0,
                    else False
    :postcondition: dictionary must be unchanged
    :return: a Boolean value of either True or False

    # current_health is a large integer
    >>> is_alive({"x-coordinate": 0, "y-coordinate": 0, "current_health": 100})
    True

    # current_health is equal to 0
    >>> is_alive({"x-coordinate": 0, "y-coordinate": 0, "current_health": 0})
    False
    """
    return entity['current_health'] > 0


def print_character_death() -> None:
    """
    Print description of character death.
    """
    print(f'Your foe leers at you triumphantly and crows in victory. "I eat CST students for\n'
          f'breakfast, and you are no exception.  Better luck next time!". You go home licking\n'
          f'your wounds and contemplate whether you will re-enroll again next term.\n GAME OVER.')


def print_user_exit() -> None:
    """
    Print thank you and good bye message.
    """
    print('Thank you for playing, and goodbye!')
    sys.exit()


def print_win_game() -> None:
    """
    Congratulate player for winning the game.
    """
    print('You smile triumphantly as you leave the exam room, having defeated your final exam\n'
          'with gusto.  All the students and teachers stand up to applaud you as you leave.  Wow.\n'
          'They are so impressed.  With these grades, you will get into co-op for sure.\n'
          'Congratulations, you won the game!')


# </editor-fold>


def game():  # called from main
    """
    Drive the main game loop.
    """
    rows = MINIMUM_DIMENSIONS
    columns = MINIMUM_DIMENSIONS
    board = map_room_descriptions(rows, columns)
    character = initial_game_setup()
    while is_alive(character) and not character['goal_met']:
        describe_current_location(board, character)  # Tells user where they are
        display_map(character, board)
        direction = direction_input()
        if direction in ['1', '2']:
            command_options(character, direction)
            continue
        elif direction in ['3']:
            print_user_exit()
        valid_move = validate_move(board, character, direction)
        if valid_move is True:
            health_regeneration(character)
            move_character(character, direction)
            if chance_generator(character):
                foe = scale_foe_to_level(character)
                fight_or_flee(foe, character)
        else:
            print_invalid_movement()
    if is_alive(character) is False:
        print_character_death()
    else:
        print_win_game()


def main():
    """
    Drive the program.
    """
    game()


if __name__ == "__main__":
    main()
