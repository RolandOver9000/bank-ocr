def print_menu(title, list_options, exit_message):
    """
    Displays a menu.

    Args:
        title (str): menu title
        list_options (list): list of strings - options that will be shown in menu
        exit_message (str): the last option with (0) (example: "Back to main menu")

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    if not title.endswith(":"):
        title += ":"

    print(f"\n{title}")

    option_indent = ' ' * 4

    for index, option in enumerate(list_options):
        print(f"{option_indent}({index + 1}) {option}")

    print(f"{option_indent}(0) {exit_message}")


def print_error_message(message):
    """
    Displays an error message (example: ``Error: @message``)

    Args:
        message (str): error message to be displayed

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    print(f"\nError: {message}")


def get_input():
    """
    Gets an input from the user.

    Returns:
        The entered input from the user.
    """
    label = "Please enter a number: "
    indent = " " * 4
    return input(f"\n{indent}{label}")
