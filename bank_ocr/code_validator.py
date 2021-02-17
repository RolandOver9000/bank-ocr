
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


def get_calculated_checksum(code):
    """
    Calculates the checksum based on a formula.
    For example:
        account number:  3  4  5  8  8  2  8  6  5
        position names:  d9 d8 d7 d6 d5 d4 d3 d2 d1
        checksum calculation:(d1+2*d2+3*d3+...+9*d9) mod 11 = 0
    :param code: Reversed string version of the bank code.
    Returns:
        A calculated checksum based on the formula.
    """
    code.reverse()
    calculated_checksum = 0
    for index, number in enumerate(code):
        # +1 because index starts from 0
        calculated_checksum += int(number) * (index + 1)
    return calculated_checksum


def is_code_has_unknown_digit(processed_code):
    """
    Checks if the code is a valid hexadecimal number.
    :param processed_code: String version of bank code.
    Returns:
        A boolean value based on the evaluation.
    """
    return True if list(processed_code).count("?") == 0 else False


def convert_code_to_decimal(digit_list):
    """
    Converts list of hexadecimal numbers to decimal.
    :param digit_list: Hexadecimal list of numbers.
    Returns:
        A list that contains the decimal version of the given hexadecimal numbers.
    """
    converted_digits = []

    for index, digit in enumerate(digit_list):
        if not digit.isnumeric():
            digit = HEXADECIMAL_TO_DECIMAL[digit]
        converted_digits.append(digit)

    return converted_digits


def is_code_valid_checksum(processed_code):
    """
    Checks if checksum is valid.
    :param processed_code: String of bank code.
    Returns:
        A boolean value if checksum is correct.
    """

    if processed_code.isnumeric():
        list_of_digits = [int(digit) for digit in processed_code]
    else:
        converted_digits = convert_code_to_decimal(processed_code)
        list_of_digits = [int(digit) for digit in converted_digits]

    return sum(list_of_digits) > 0 and get_calculated_checksum(list_of_digits) % 11 == 0


def get_validation_status(processed_code):
    """
    Validates the code based on the gives rule.
    :param processed_code: String of bank code.
    Returns:
        A boolean value based on the validity.
    """
    if is_code_has_unknown_digit(processed_code):
        if is_code_valid_checksum(processed_code):
            return VALID_CODE_STATUS
        else:
            return CHECKSUM_ERROR_STATUS
    else:
        return DIGIT_ERROR_STATUS


def is_code_contain_multiple_bad_digits(processed_code):
    """
    Checks if the processed code has multiple wrong digit.
    :param processed_code: String representation of processed (numeric) code.
    Returns:
        A boolean based on the number of the wrong digits that the processed code contains.
    """
    return True if list(processed_code).count("?") > 1 else False


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
