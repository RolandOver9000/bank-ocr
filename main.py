import util
import sys

from bank_ocr import sub_menu_handler


def choose():
    user_input = util.get_input()
    if user_input == "1":
        sub_menu_handler.handle_user_story_1_sub_menu()
    elif user_input == "2":
        sub_menu_handler.handle_user_story_2_sub_menu()
    elif user_input == "0":
        sys.exit(0)
    else:
        raise KeyError("There is no such option.")


def handle_menu():
    options = ["Analyze data from dummy file (User story 1)",
               "Validate data from dummy file (User story 2)",
               "User story 3",
               "User story 4",
               "User story 5"]

    util.print_menu("Main menu", options, "Exit program")


def main():
    handle_menu()
    try:
        choose()
    except KeyError as err:
        util.print_error_message(str(err))


if __name__ == '__main__':
    main()
