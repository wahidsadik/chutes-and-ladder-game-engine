import json


def load_config(config_file: str) -> dict:
    '''
    loads json
    '''
    with open(config_file) as json_data_file:
        return json.load(json_data_file)
