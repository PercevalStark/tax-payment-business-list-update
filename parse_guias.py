import csv
import json

from current_lists import taxes, utilities


def write_to_json_file(data, filename):
    """
    Write data to a JSON file.

    :param data: Dictionary to write to the JSON file.
    :param filename: Name of the file to save the JSON data.
    """
    with open(filename, 'w', encoding='utf8') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)


taxes_indexed = {f"{tax['code']}_{tax['segment']}": tax for tax in taxes}
utilities_indexed = {f"{utility['code']}_{utility['segment']}": utility for utility in utilities}

grid_map = {
    "Estendida, até 23:59": "24H",
    "Restrita, até 20:45": "20H",
}

convenios_tax = ["TRIBUTOS ESTADUAIS", "TRIBUTOS MUNICIPAIS",]

taxes_to_add = []
utilities_to_add = []


with open("Validador de Guias - ListaBoletos.csv") as lista_boletos_file:
    file_reader = csv.reader(lista_boletos_file, delimiter=",")
    next(file_reader)
    for row in file_reader:
        row_info = {
            "code": str(int(row[0])),
            "segment": str(int(row[1])),
            "name": row[2],
            "time": grid_map[row[4]],
            "type": row[5],
        }

        if taxes_indexed.pop(f"{row_info['code']}_{row_info['segment']}", None):
            continue

        if utilities_indexed.pop(f"{row_info['code']}_{row_info['segment']}", None):
            continue
            
        if row_info['type'] in convenios_tax:
            taxes_to_add.append(row_info)
        else:
            utilities_to_add.append(row_info)


write_to_json_file(taxes_to_add, "results/taxes_to_add.json")
write_to_json_file(utilities_to_add, "results/utilities_to_add.json")

write_to_json_file(
    [{"code": v["code"], "segment": v["segment"], "name": v["name"]} for v in taxes_indexed.values()],
    "results/taxes_to_remove.json"
)
write_to_json_file(
    [{"code": v["code"], "segment": v["segment"], "name": v["name"]} for v in utilities_indexed.values()],
    "results/utilities_to_remove.json"
)
