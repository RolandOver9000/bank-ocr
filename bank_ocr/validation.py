from bank_ocr import code_reader, code_writer

CHECKSUM_ERROR_STATUS = "ERR"
DIGIT_ERROR_STATUS = "ILL"
VALID_CODE_STATUS = ""
MULTIPLE_VALID_CODE_STATUS = "AMB"
HEXADECIMAL_TO_DECIMAL = {
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15
}


def calculate_checksum(reversed_code):
    """
    Calculates the checksum based on a formula.
    For example:
        account number:  3  4  5  8  8  2  8  6  5
        position names:  d9 d8 d7 d6 d5 d4 d3 d2 d1
        checksum calculation:(d1+2*d2+3*d3+...+9*d9) mod 11 = 0
    :param reversed_code: Reversed string version of the bank code.
    Returns:
        A calculated checksum based on the formula.
    """
    calculated_checksum = 0
    for index, number in enumerate(reversed_code):
        # +1 because index starts from 0
        calculated_checksum += int(number) * (index + 1)
    return calculated_checksum


def is_code_hexadecimal(processed_code):
    """
    Checks if the code is a valid hexadecimal number.
    :param processed_code: String version of bank code.
    Returns:
        A boolean value based on the evaluation.
    """
    return True if list(processed_code).count("?") == 0 else False


def convert_code_to_decimal(reversed_code):

    pass


def is_code_valid_checksum(processed_code):
    """
    Checks if checksum is valid.
    :param processed_code: String of bank code.
    Returns:
        A boolean value if checksum is correct.
    """
    list_of_digits = list(processed_code)
    list_of_digits.reverse()

    if not processed_code.isnumeric():
        list_of_digits = convert_code_to_decimal(processed_code)

    return sum(list_of_digits) > 0 and calculate_checksum(list_of_digits) % 11 == 0


def get_validation_status(processed_code):
    """
    Validates the code based on the gives rule.
    :param processed_code: String of bank code.
    Returns:
        A boolean value based on the validity.
    """
    if is_code_hexadecimal(processed_code):
        if is_code_valid_checksum(processed_code):
            return VALID_CODE_STATUS
        else:
            return CHECKSUM_ERROR_STATUS
    else:
        return DIGIT_ERROR_STATUS


def handle_validation():
    """
    Handles the process of bank code validation.
    Returns:
        A dictionary with the string codes(key) and with a boolean value based on the validity(value).
    """
    processed_codes = code_reader.handle_code_reading()
    validated_processed_codes = {}
    for processed_code in processed_codes:
        validated_processed_codes[processed_code] = get_validation_status(processed_code)
    return validated_processed_codes


def evaluate_fixed_code(processed_code, possible_solutions, previous_evaluation):
    """
    Evaluates the fixed code based on the fix result.
    :param processed_code: String representation of processed (numeric) code.
    :param possible_solutions: List of the possible codes that are valid.
    :param previous_evaluation: Previous evaluation of the code.
    Returns:
        A list that's first element is a result code, the second element is the re-evaluated value based
        on the fix result(s).
    """
    if not possible_solutions:
        return [processed_code, previous_evaluation]
    if len(possible_solutions) == 1:
        return [possible_solutions[0], VALID_CODE_STATUS]
    else:
        return [processed_code, MULTIPLE_VALID_CODE_STATUS]


def handle_wrong_code():
    """
    Handles wrong code and the data saving into a file.
    Returns:
        Read data from the file that contains the processed bank codes represented as a string.
    """
    processed_codes = handle_validation()
    code_writer.write_validated_codes_to_file(processed_codes)
    return code_reader.read_validated_codes()
