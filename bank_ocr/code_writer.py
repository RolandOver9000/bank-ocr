DUMMY_FILE_NAME = "data/validated_dummy_data.txt"


def write_validated_codes_to_file(processed_codes):
    """
    Empties the result dummy file then writes code to file with its validation.
    :param processed_codes: A list of lists where the inner lists are the processed codes (at index 0)
    and the evaluation result (at index 1).
    """
    index_of_code = 0
    index_of_evaluation = 1

    with open(DUMMY_FILE_NAME, "w"):
        pass

    with open(DUMMY_FILE_NAME, "w") as file:
        for processed_code in processed_codes:
            file.writelines(processed_code[index_of_code] + " " + processed_code[index_of_evaluation] + "\n")
