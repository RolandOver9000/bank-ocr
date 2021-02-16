from bank_ocr import code_reader, code_writer


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


def validate(processed_code):
    """
    Validates the code based on the gives rule.
    :param processed_code: String of bank code.
    Returns:
        A boolean value based on the validity.
    """
    reversed_code = processed_code[::-1]
    if processed_code.isnumeric() and\
            int(processed_code) > 0 and\
            calculate_checksum(reversed_code) % 11 == 0:
        validation_result = True
    else:
        validation_result = False

    return validation_result


def handle_validation():
    """
    Handles the process of bank code validation.
    Returns:
        A dictionary with the string codes(key) and with a boolean value based on the validity(value).
    """
    processed_codes = code_reader.handle_code_reading()
    validated_processed_codes = {}
    for processed_code in processed_codes:
        validated_processed_codes[processed_code] = validate(processed_code)
    return validated_processed_codes


def handle_wrong_code():
    """
    Handles wrong code and the data saving into a file.
    Returns:
        Read data from the file that contains the processed bank codes represented as a string.
    """
    processed_codes = handle_validation()
    code_writer.write_validated_codes_to_file(processed_codes)
    return code_reader.read_validated_codes()
