from bank_ocr import code_reader, validation, code_fixer


def handle_user_story_1_sub_menu():
    """
    Prints the "Analyze data from dummy file" task.
    """
    print(code_reader.handle_code_reading())


def handle_user_story_2_sub_menu():
    """
    Prints the result of the "Validate data from dummy file" task.
    """
    print(validation.handle_validation())


def handle_user_story_3_sub_menu():
    """
    Prints the "Handle wrong code" task.
    """
    print(validation.handle_wrong_code())


def handle_user_story_4_sub_menu():
    """
    Prints the "Try to fix wrong code" task.
    """
    code_fixer.handle_code_fix()
