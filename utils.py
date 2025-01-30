import json

def write_to_json_file(data, filename):
    """
    Write data to a JSON file.

    :param data: Dictionary to write to the JSON file.
    :param filename: Name of the file to save the JSON data.
    """
    with open(filename, 'w', encoding='utf8') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)


def read_from_json_file(filename):
    """
    Read data from a JSON file and return it as a dictionary.

    :param filename: Name of the JSON file to read.
    :return: Dictionary containing the JSON data.
    """
    with open(filename, 'r') as json_file:
        data = json.load(json_file)
    return data