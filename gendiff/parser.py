import yaml
import json


def parse_file(filepath):
    ending = filepath.endswith

    match ending:
        case 'json':
            file = json.load(open(filepath))
        case 'yml' | 'yaml':
            file = yaml.safe_load(open(filepath))
    return file
