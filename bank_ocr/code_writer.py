DUMMY_FILE_NAME = "data/validated_dummy_data.txt"


def write_validated_codes_to_file(processed_codes):
    """
    Empties the result dummy file then writes code to file with its validation.
    :param processed_codes: Dictionary of processed codes(key) with its validation(value).
    """
    with open(DUMMY_FILE_NAME, "w"):
        pass

    with open(DUMMY_FILE_NAME, "w") as file:
        for processed_code, evaluation in processed_codes.items():
            file.writelines(processed_code + " " + evaluation + "\n")
