DUMMY_FILE_NAME = "data/validated_dummy_data.txt"


def write_validated_codes_to_file(processed_codes):
    """
    Writes code to file with its validation.
    :param processed_codes: Dictionary of processed codes(key) with its validation(value).
    """
    with open(DUMMY_FILE_NAME, "w") as file:
        for key, value in processed_codes.items():
            if key.isnumeric():
                evaluated_value = "ERR" if not value else ""
                file.writelines(key + " " + evaluated_value + "\n")
            else:
                file.writelines(key + " ILL\n")
    pass