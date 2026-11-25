import json


def load_records(source_path):
    with open(source_path, encoding="utf-8") as input_file:
        return [json.loads(line) for line in input_file]
