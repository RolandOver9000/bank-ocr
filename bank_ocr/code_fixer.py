from bank_ocr import validation, code_reader

NUMBER_OF_CHARACTERS_IN_LINE = 27
NUMBER_OF_DIGIT_PRINT_LINE = 3
NUMBER_OF_DIGITS = 9
DIGIT_CHARACTER_COLUMN = 3
SEGMENTS_IN_DIGIT = 7
DICT_OF_STRING_DIGITS = {
    " _ "
    "| |"
    "|_|": 0,
    "   "
    "  |"
    "  |": 1,
    " _ "
    " _|"
    "|_ ": 2,
    " _ "
    " _|"
    " _|": 3,
    "   "
    "|_|"
    "  |": 4,
    " _ "
    "|_ "
    " _|": 5,
    " _ "
    "|_ "
    "|_|": 6,
    " _ "
    "  |"
    "  |": 7,
    " _ "
    "|_|"
    "|_|": 8,
    " _ "
    "|_|"
    " _|": 9
}


def is_code_valid(processed_code):
    """
    :param processed_code: String of the code in number format.
    Returns:
        A boolean based on the code validation.
    """
    return True if validation.validate(processed_code) else False


def try_to_fix_digit(digit):
    """
    Cuts the string digit to 3 parts and
    :param digit: String representation of a digit.
    Returns:
        A string that can be the fixed digit if it is possible, otherwise returns a ? .
    """
    segment_counter = 0
    print(digit)
    for line_counter in range(NUMBER_OF_DIGIT_PRINT_LINE):
        line_of_digit = digit[line_counter * DIGIT_CHARACTER_COLUMN:(line_counter * DIGIT_CHARACTER_COLUMN) + 3]
    pass


def get_invalid_number_indexes_from_code(processed_code):
    """
    Gets the indexes of the invalid digits.
    :param processed_code: String representation of processed bank code.
    Returns:
        List if index(es) that are in the processed_code.
    """
    invalid_digit_indexes = []
    for index, character in enumerate(processed_code):
        if character == "?":
            invalid_digit_indexes.append(index)
    return invalid_digit_indexes


def handle_invalid_digits(code, processed_code):
    """
    Manages the process of invalid digit repair.
    :param code: String representation of digit code.
    :param processed_code: String representation of processed (numeric) code.
    Returns:
        A code that
    """
    invalid_digit_indexes = get_invalid_number_indexes_from_code(processed_code)
    for invalid_digit_index in invalid_digit_indexes:
        get_digit_from_code(code, invalid_digit_index)
        try_to_fix_digit()
    pass


def try_to_fix_code(code, processed_code):
    """
    :param code: String representation of digit code.
    :param processed_code: String representation of processed (numeric) code.
    Returns:
        A new code if it can be valid or the original code.
    """
    if not validation.is_code_numeric(processed_code):
        handle_invalid_digits(code, processed_code)
    pass


def process_string_code(code):
    """
    Processes the bank code. It handles the string code like a matrix. Each code is a 3x3 string. For example
    The inner for goes from 0:0 -> 0:3 then steps 1 line and concatenate 1:0 -> 1:3 then steps 1 line
    and concatenate 2:0 -> 2:3. Then the outer for "step a digit" and the inner for goes again.
    Then it searches the string digit in the dictionary of digits and concatenate the numbers. If digit not found in
    the dict it, it will ad a "?".
    :param code: String of a bank code that broken into lines and concatenated.
    Returns:
        String of the code in number format.
    """
    processed_code = ""
    digit = ""

    for index in range(NUMBER_OF_DIGITS):
        digit = ""
        starter_column_of_digit = index * DIGIT_CHARACTER_COLUMN
        for row in range(NUMBER_OF_DIGIT_PRINT_LINE):
            row_starter_index = starter_column_of_digit + (row * NUMBER_OF_CHARACTERS_IN_LINE)
            digit += code[row_starter_index: row_starter_index + DIGIT_CHARACTER_COLUMN]

        if digit in DICT_OF_STRING_DIGITS.keys():
            processed_code += str(DICT_OF_STRING_DIGITS[digit])
        else:
            processed_code += "?"

    if not is_code_valid(processed_code):
        processed_code = try_to_fix_code(code, processed_code)
    return processed_code


def handle_code_fix():
    """
    Handles the process of code fixer.
    Returns:
        The string list of processed bank codes.
    """
    read_codes = code_reader.read_from_dummy_file()
    for code in read_codes:
        process_string_code(code)
