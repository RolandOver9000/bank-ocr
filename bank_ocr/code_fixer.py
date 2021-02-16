from bank_ocr import validation, code_reader

NUMBER_OF_CHARACTERS_IN_LINE = 27
NUMBER_OF_DIGIT_PRINT_LINE = 3
NUMBER_OF_DIGITS = 9
DIGIT_CHARACTER_COLUMN = 3
CHARACTERS_IN_DIGIT = NUMBER_OF_DIGIT_PRINT_LINE * DIGIT_CHARACTER_COLUMN
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
    return True if validation.is_valid(processed_code) == "" else False


def is_digit_valid(assembled_digit):
    """
    Checks if digit is valid.
    :param assembled_digit: String representation of a possible digit.
    Returns:
        Boolean value based on digit evaluation.
    """
    return True if assembled_digit in DICT_OF_STRING_DIGITS.keys() else False


def try_to_fix_digit(digit):
    """
    Tries out if a wrong digit can be fixed by add or remove segment.
    :param digit: String representation of a digit.
    Returns:
        A lis of possible numbers or an empty number if the digit cannot be fixed.
    """
    segments_representation = ['|', '_']
    possible_solutions = []

    for index, character in enumerate(digit):
        if character == " ":
            for segment in segments_representation:
                assembled_digit = digit[0:index] + segment + digit[index + 1:]
                if is_digit_valid(assembled_digit):
                    possible_solutions.append(DICT_OF_STRING_DIGITS[assembled_digit])
        else:
            assembled_digit = digit[0:index] + " " + digit[index + 1:]
            if is_digit_valid(assembled_digit):
                possible_solutions.append(DICT_OF_STRING_DIGITS[assembled_digit])

    return possible_solutions


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


def get_invalid_digits_from_code(code, invalid_digit_indexes):
    """
    Collects all invalid digits in a code.
    :param code: String representation of digit code.
    :param invalid_digit_indexes: Indexes of the invalid digits.
    Returns:
        A dictionary of invalid digits(value) based on its index(key) in the code.
    """
    invalid_digits = {}
    for index in range(NUMBER_OF_DIGITS):
        digit = ""
        starter_column_of_digit = index * DIGIT_CHARACTER_COLUMN
        for row in range(NUMBER_OF_DIGIT_PRINT_LINE):
            row_starter_index = starter_column_of_digit + (row * NUMBER_OF_CHARACTERS_IN_LINE)
            digit += code[row_starter_index: row_starter_index + DIGIT_CHARACTER_COLUMN]
        if index in invalid_digit_indexes:
            invalid_digits[index] = digit

    return invalid_digits


def get_possible_valid_code_with_options(processed_code, valid_digit_options, index_of_invalid_digit):
    """
    Checks the variations of a possible code if there is only 1 wrong digit.
    :param processed_code: String representation of processed (numeric) code.
    :param valid_digit_options: The possible options about what a digit can be.
    :param index_of_invalid_digit: The index of the wrong digit in the code.
    Returns:
        The possible codes that are valid.
    """
    validity_counter = 0
    possible_codes = []
    for digit_option in valid_digit_options:
        fixed_process_code = processed_code[:index_of_invalid_digit] \
                             + str(digit_option) \
                             + processed_code[index_of_invalid_digit + 1:]
        if validation.is_valid(fixed_process_code):
            validity_counter += 1
            possible_codes.append(fixed_process_code)
    return possible_codes


def handle_invalid_digits(code, processed_code):
    """
    Manages the process of invalid digit repair.
    :param code: String representation of digit code.
    :param processed_code: String representation of processed (numeric) code.
    Returns:
        The number of possible solution(s) if the code has any.
    """
    invalid_digit_indexes = get_invalid_number_indexes_from_code(processed_code)
    invalid_digits = get_invalid_digits_from_code(code, invalid_digit_indexes)
    possible_solutions = []

    for index_of_invalid_digit, invalid_digit in invalid_digits.items():
        valid_digit_options = try_to_fix_digit(invalid_digit)
        possible_solutions += \
            get_possible_valid_code_with_options(processed_code, valid_digit_options, index_of_invalid_digit)

    return possible_solutions


def try_to_fix_code(code, processed_code):
    """
    :param code: String representation of digit code.
    :param processed_code: String representation of processed (numeric) code.
    Returns:
        The possible solutions of the code.
    """
    if not validation.is_code_numeric(processed_code):
       return handle_invalid_digits(code, processed_code)
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
    return processed_code


def handle_code_fix():
    """
    Handles the process of code fixer.
    Returns:
        The string list of processed bank codes.
    """
    possible_solutions = []

    read_codes = code_reader.read_from_dummy_file()
    for code in read_codes:
        processed_code = process_string_code(code)
        evaluation = is_code_valid(processed_code)

            possible_solutions = try_to_fix_code(code, processed_code)
        else:
            possible_solutions.append(processed_code)
        validation.evaluate_code_status(processed_code, possible_solutions)
