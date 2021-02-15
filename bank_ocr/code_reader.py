
DUMMY_FILE_NAME = "data/dummy_data.txt"


def start_process():

    return None


def read_from_dummy_file():

    """
    Reads from the /data/dummy_data.txt file.
    Returns:
         The string list of bank codes.
    """
    with open(DUMMY_FILE_NAME, "r") as file:
        lines = file.readlines()
    print(lines)