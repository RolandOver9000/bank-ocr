from bank_ocr import code_reader


def validate(processed_codes):
    """
    Validates the code based on the gives rule.
    For example:
        account number:  3  4  5  8  8  2  8  6  5
        position names:  d9 d8 d7 d6 d5 d4 d3 d2 d1
        checksum calculation:(d1+2*d2+3*d3+...+9*d9) mod 11 = 0
    :param processed_codes: String list of bank codes.
    Returns:
        A dictionary with the string codes(key) and with a boolean value based on the validity(value).
    """
    validation_result = {}
    for code in processed_codes:
        code = code[::-1]
        print(code)
    return validation_result


def handle_process():
    """
    Handles the process of bank code validation.
    Returns:
        A dictionary with the string codes(key) and with a boolean value based on the validity(value).
    """
    processed_codes = code_reader.handle_process()
    return validate(processed_codes)

