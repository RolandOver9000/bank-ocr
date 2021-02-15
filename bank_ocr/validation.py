from bank_ocr import code_reader


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
        calculated_checksum += int(number) * index
    return calculated_checksum


def validate(processed_codes):
    """
    Validates the code based on the gives rule.
    :param processed_codes: String list of bank codes.
    Returns:
        A dictionary with the string codes(key) and with a boolean value based on the validity(value).
    """
    validation_result = {}
    for code in processed_codes:
        reversed_code = code[::-1]
        if int(code) > 0 and calculate_checksum(reversed_code) % 11 == 0:
            validation_result[code] = True
        else:
            validation_result[code] = False

    return validation_result


def handle_process():
    """
    Handles the process of bank code validation.
    Returns:
        A dictionary with the string codes(key) and with a boolean value based on the validity(value).
    """
    processed_codes = code_reader.handle_process()
    return validate(processed_codes)

