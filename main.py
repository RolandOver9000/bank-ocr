import util
import sys

from bank_ocr.sub_menu_handler import handle_user_story_1_sub_menu


def choose():
    user_input = util.get_input()
    if user_input == "1":
        handle_user_story_1_sub_menu()
    elif user_input == "0":
        sys.exit(0)
    else:
        raise KeyError("There is no such option.")


def handle_menu():
    options = ["User story 1",
               "User story 2",
               "User story 3",
               "User story 4",
               "User story 5"]

    util.print_menu("Main menu", options, "Exit program")


def main():
#    while True:
    handle_menu()
    try:
        choose()
    except KeyError as err:
        util.print_error_message(str(err))


if __name__ == '__main__':
    main()
