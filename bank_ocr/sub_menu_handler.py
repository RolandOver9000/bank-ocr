import util
from bank_ocr import code_reader, validation


def handle_user_story_1_sub_menu():
    """
    Prints the options of the sub-menu and get the user input.
    """
    options = ["Analyze data from dummy file"]
    util.print_menu("Code reader menu", options, "Exit program")
    user_input = util.get_input()
    handle_user_input(user_input)


def handle_user_story_2_sub_menu():
    """
    Prints the options of the sub-menu and get the user input.
    """
    options = ["Validate data from dummy file"]
    util.print_menu("Validation menu", options, "Exit program")
    user_input = util.get_input()
    handle_user_input(user_input)


def handle_user_input(user_input):
    """
    Navigates to the chosen process.
    :param user_input: string
    """
    if user_input == "1":
        print(code_reader.handle_process())
    elif user_input == "2":
        print(validation.handle_process())
