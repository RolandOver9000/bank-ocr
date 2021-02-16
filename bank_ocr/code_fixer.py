NUMBER_OF_CHARACTERS_IN_LINE = 27
NUMBER_OF_DIGIT_PRINT_LINE = 3
NUMBER_OF_DIGITS = 9
DIGIT_CHARACTER_COLUMN = 3
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
