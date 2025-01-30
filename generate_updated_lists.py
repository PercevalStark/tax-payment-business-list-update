from current_lists import utilities
from utils import read_from_json_file, write_to_json_file

utilities_to_remove = read_from_json_file("results/utilities_to_remove.json")
utilities_to_add = read_from_json_file("results/utilities_to_add.json")


utilities_to_remove_code_segment = {(u['code'], u['segment']) for u in utilities_to_remove}

updated_utilities_list = [u for u in utilities if (u['code'], u['segment']) not in utilities_to_remove_code_segment]
updated_utilities_list.extend(utilities_to_add)

write_to_json_file(updated_utilities_list, "results/updated_utilities.json")

