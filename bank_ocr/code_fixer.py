from bank_ocr import validation, code_reader, code_writer

NUMBER_OF_CHARACTERS_IN_LINE = 27
NUMBER_OF_DIGIT_PRINT_LINE = 3
NUMBER_OF_DIGITS = 9
DIGIT_CHARACTER_COLUMN = 3
CHARACTERS_IN_DIGIT = NUMBER_OF_DIGIT_PRINT_LINE * DIGIT_CHARACTER_COLUMN
CHECKSUM_ERROR_STATUS = "ERR"
DIGIT_ERROR_STATUS = "ILL"
VALID_CODE_STATUS = ""
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


def get_digits_from_code(code, digit_indexes):
    """
    Collects all digits in a code based on index(es).
    :param code: String representation of digit code.
    :param digit_indexes: Indexes of the invalid digits.
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
        if index in digit_indexes:
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
        if validation.get_validation_status(fixed_process_code) == VALID_CODE_STATUS:
            validity_counter += 1
            possible_codes.append(fixed_process_code)
    return possible_codes


def handle_invalid_digits(code, processed_code):
    """
    Manages the process of invalid digit repair.
    :param code: String representation of digit code.
    :param processed_code: String representation of processed (numeric) code.
    Returns:
        The possible solution(s) if the code has any.
    """
    invalid_digit_indexes = get_invalid_number_indexes_from_code(processed_code)
    invalid_digits = get_digits_from_code(code, invalid_digit_indexes)
    possible_solutions = []

    for index_of_invalid_digit, invalid_digit in invalid_digits.items():
        valid_digit_options = try_to_fix_digit(invalid_digit)
        possible_solutions += \
            get_possible_valid_code_with_options(processed_code, valid_digit_options, index_of_invalid_digit)

    return possible_solutions


def get_valid_number_variation(index_of_digit, processed_code, possible_digit_variations):
    """
    Checks if a code can be valid based on the possible digits on a specific index.
    :param index_of_digit: Index of the digit that can be interchangeable with the given possible digit variations.
    :param processed_code: String representation of processed (numeric) code.
    :param possible_digit_variations: The list of the numbers that can be interchangeable with the number that is on
    the given index.
    Returns:
        A list of valid codes.
    """
    valid_codes = []

    for digit in possible_digit_variations:
        code_variation = processed_code[:index_of_digit] + str(digit) + processed_code[index_of_digit + 1:]
        if validation.is_code_valid_checksum(code_variation):
            valid_codes.append(code_variation)
    return valid_codes


# In the case of checksum errors maybe would be better to save out what number can be converted into another number
# because it will be always fix.
def handle_checksum_error(code, processed_code):
    """
    Handles the process of the checksum error fix. It iterates over the digits of the code and collects all the possible
    variations of the digit based on digit manipulation that happens in try_to_fix_digit.
    :param code: String representation of digit code.
    :param processed_code: String representation of processed (numeric) code.
    Returns:
        The possible solution(s) if the code has any.
    """
    invalid_digits = get_digits_from_code(code, range(len(processed_code)))
    possible_solutions = []

    for index_of_digit, digit in invalid_digits.items():
        possible_digit_variations = try_to_fix_digit(digit)
        possible_solutions = get_valid_number_variation(index_of_digit, processed_code, possible_digit_variations)
    return possible_solutions


def handle_code_fix():
    """
    Handles the process of code fixer.
    - Evaluates code then if it is wrong, it starts the fixing process, then evaluates the result again and saves it.
    - After that it starts the "write result into the file" process.
    Returns:
        The string list of processed bank codes.
    """
    final_evaluation = {}
    code_index = 0
    evaluation_result_index = 1

    read_codes = code_reader.read_from_dummy_file()
    for code in read_codes:
        processed_code = code_reader.process_string_code(code)
        evaluation = validation.get_validation_status(processed_code)
        if evaluation == DIGIT_ERROR_STATUS:
            possible_solutions = handle_invalid_digits(code, processed_code)
            evaluated_process_code = validation.evaluate_fixed_code(processed_code, possible_solutions, evaluation)
            final_evaluation[evaluated_process_code[code_index]] = evaluated_process_code[evaluation_result_index]
        elif evaluation == CHECKSUM_ERROR_STATUS:
            possible_solutions = handle_checksum_error(code, processed_code)
            evaluated_process_code = validation.evaluate_fixed_code(processed_code, possible_solutions, evaluation)
            final_evaluation[evaluated_process_code[code_index]] = evaluated_process_code[evaluation_result_index]
        else:
            final_evaluation[processed_code] = VALID_CODE_STATUS
    code_writer.write_validated_codes_to_file(final_evaluation)
