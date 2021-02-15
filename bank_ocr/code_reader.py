
DUMMY_FILE_NAME = "data/dummy_data.txt"
NUMBER_OF_CHARACTERS_IN_LINE = 27


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
