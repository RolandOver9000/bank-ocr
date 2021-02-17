from bank_ocr import validation, code_reader, code_writer

DUMMY_FILE_NAME = "data/dummy_data.txt"
VALIDATED_DUMMY_FILE_NAME = "data/validated_dummy_data.txt"
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
    "|_|": '0',
    "   "
    "  |"
    "  |": '1',
    " _ "
    " _|"
    "|_ ": '2',
    " _ "
    " _|"
    " _|": '3',
    "   "
    "|_|"
    "  |": '4',
    " _ "
    "|_ "
    " _|": '5',
    " _ "
    "|_ "
    "|_|": '6',
    " _ "
    "  |"
    "  |": '7',
    " _ "
    "|_|"
    "|_|": '8',
    " _ "
    "|_|"
    " _|": '9',
    " _ "
    "|_|"
    "| |": 'A',
    " _  "
    "|_\""
    "|_/": 'B',
    " _ "
    "|  "
    "|_ ": 'C',
    " _ "
    "| \""
    "|_/": 'D',
    " _ "
    "|_ "
    "|_ ": 'E',
    " _ "
    "|_ "
    "|  ": 'F'

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
    segments_representation = ['|', '_', '\\', '/']
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


def get_digits_from_code_by_index(code, digit_indexes):
    """
    Collects all digits in a code based on index(es).
    :param code: String representation of digit code.
    :param digit_indexes: Indexes of the invalid digits.
    Returns:
        A dictionary of invalid digits(value) based on its index(key) in the code.
    """
    digit_on_index = {}
    for index in range(NUMBER_OF_DIGITS):
        digit = ""
        starter_column_of_digit = index * DIGIT_CHARACTER_COLUMN
        for row in range(NUMBER_OF_DIGIT_PRINT_LINE):
            row_starter_index = starter_column_of_digit + (row * NUMBER_OF_CHARACTERS_IN_LINE)
            digit += code[row_starter_index: row_starter_index + DIGIT_CHARACTER_COLUMN]
        if index in digit_indexes:
            digit_on_index[index] = digit

    return digit_on_index


def get_single_digit_from_code_by_index(code, digit_index):
    """
    Gets a single digit string from a code by the given index.
    :param code: String representation of digit code.
    :param digit_index: The number of the searched digit's index.
    Returns:
        The string representation of the digit.
    """
    digit = ""
    starter_column_of_digit = digit_index * DIGIT_CHARACTER_COLUMN
    for row in range(NUMBER_OF_DIGIT_PRINT_LINE):
        row_starter_index = starter_column_of_digit + (row * NUMBER_OF_CHARACTERS_IN_LINE)
        digit += code[row_starter_index: row_starter_index + DIGIT_CHARACTER_COLUMN]

    return digit


def get_possible_valid_code(processed_code, valid_digit_options, index_of_invalid_digit):
    """
    Checks the variations of a possible code if there is only 1 wrong digit.
    :param processed_code: String representation of processed (numeric) code.
    :param valid_digit_options: The possible options about what a digit can be.
    :param index_of_invalid_digit: The index of the wrong digit in the code.
    Returns:
        The possible code that are valid or empty list.
    """
    print(processed_code, " processed code\n ", valid_digit_options, " options")
    for digit_option in valid_digit_options:
        fixed_process_code = processed_code[:index_of_invalid_digit] \
                             + str(digit_option) \
                             + processed_code[index_of_invalid_digit + 1:]
        if validation.get_validation_status(fixed_process_code) == VALID_CODE_STATUS:
            return [fixed_process_code]
    return []


def handle_invalid_digit(code, processed_code):
    """
    Manages the process of invalid digit repair.
    :param code: String representation of digit code.
    :param processed_code: String representation of processed (numeric) code.
    Returns:
        The possible solution if the code has any.
    """
    invalid_digit_index = list(processed_code).index("?")
    invalid_digit = get_single_digit_from_code_by_index(code, invalid_digit_index)
    valid_digit_options = try_to_fix_digit(invalid_digit)
    if valid_digit_options:
        return get_possible_valid_code(processed_code, valid_digit_options, invalid_digit_index)
    return []


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
    invalid_digits = get_digits_from_code_by_index(code, range(len(processed_code)))
    possible_solutions = []

    for index_of_digit, digit in invalid_digits.items():
        possible_digit_variations = try_to_fix_digit(digit)
        valid_number_variations = get_valid_number_variation(index_of_digit, processed_code, possible_digit_variations)
        if valid_number_variations:
            possible_solutions += valid_number_variations
    return possible_solutions


def handle_code_fix():
    """
    Handles the process of code fixer.
    - Evaluates code then if it is wrong, it starts the fixing process, then evaluates the result again and saves it.
    - After that it starts the "write result into the file" process.
    Returns:
        The string of processed bank codes that read from the file.
    """
    final_evaluation = {}
    code_index = 0
    evaluation_result_index = 1

    read_codes = code_reader.read_from_dummy_file(DUMMY_FILE_NAME)
    for code in read_codes:
        possible_solutions = []
        processed_code = code_reader.process_string_code(code)
        evaluation = validation.get_validation_status(processed_code)
        if evaluation != DIGIT_ERROR_STATUS and evaluation != CHECKSUM_ERROR_STATUS:
            final_evaluation[processed_code] = VALID_CODE_STATUS
        else:
            if evaluation == DIGIT_ERROR_STATUS and not validation.is_code_contain_multiple_bad_digits(processed_code):
                possible_solutions = handle_invalid_digit(code, processed_code)
            elif evaluation == CHECKSUM_ERROR_STATUS:
                possible_solutions = handle_checksum_error(code, processed_code)
            evaluated_process_code = validation.evaluate_fixed_code(processed_code, possible_solutions, evaluation)
            final_evaluation[evaluated_process_code[code_index]] = evaluated_process_code[evaluation_result_index]

    code_writer.write_validated_codes_to_file(final_evaluation)
    return code_reader.read_validated_codes(VALIDATED_DUMMY_FILE_NAME)
