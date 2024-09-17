import yaml
import json


def parse(data, extension):
    match extension:
        case 'json':
            return json.load(data)
        case 'yml' | 'yaml':
            return yaml.safe_load(data)
        case _:
            raise ValueError(f'Unsupported extension: {extension}')
