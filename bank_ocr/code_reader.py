
DUMMY_FILE_NAME = "data/dummy_data.txt"
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
    Then it searches the string digit in the dictionary of digits and concatenate the numbers.
    :param code: String of a bank code that broken into lines and concatenated.
    :return:
    """
    processed_code = ""

    for index in range(NUMBER_OF_DIGITS):
        digit = ""
        starter_column_of_digit = index * DIGIT_CHARACTER_COLUMN
        for row in range(NUMBER_OF_DIGIT_PRINT_LINE):
            row_starter_index = starter_column_of_digit + (row * NUMBER_OF_CHARACTERS_IN_LINE)
            digit += code[row_starter_index: row_starter_index + DIGIT_CHARACTER_COLUMN]
        processed_code += str(DICT_OF_STRING_DIGITS[digit])
    return processed_code


def process_read_lines(read_codes):
    """
    Processes the rows of the file.
    :param read_codes: List of strings
    Returns:
        List of the read codes.
    """
    code_list = []
    for code in read_codes:
        code_list.append(process_string_code(code))
    print(code_list)


def read_from_dummy_file():

    """
    Reads from the /data/dummy_data.txt file.
    Returns:
         The string list of codes that in the dummy file. 3 rows concatenated together to get a code in 1 list item.
    """
    with open(DUMMY_FILE_NAME, "r") as file:
        line = ""
        lines = []
        bank_code_line_length = 4

        for row_index, row in enumerate(file):
            line += row.strip("\n")
            read_line_length = len(row) - 1
            read_character_number = NUMBER_OF_CHARACTERS_IN_LINE - read_line_length
            line += " " * read_character_number
            # +1 because 0 % x = 0
            if (row_index + 1) % bank_code_line_length == 0:
                lines.append(line)
                line = ""
        lines.append(line)
    return lines


def handle_process():
    """
    Handles the process of code reader.
    """
    read_lines = read_from_dummy_file()
    process_read_lines(read_lines)