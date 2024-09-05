from gendiff.constants import ADDED, DELETED, NESTED, MODIFIED, UNCHANGED

def build_diff(data1, data2):
    diff = {}

    keys = sorted(data1.keys() | data2.keys())

    for key in keys:

        if key not in data1:
            diff[key] = {
                'type': ADDED,
                'value': data2[key]
            }

        elif key not in data2:
            diff[key] = {
                'type': DELETED,
                'value': data1[key]
            }

        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            diff[key] = {
                'type': NESTED,
                'children': build_diff(data1[key], data2[key])
            }

        elif value1 != value2:
            diff[key] = {
                'type': MODIFIED,
                'old_value': data1[key],
                'new_value': data2[key]
            }

        else:
            diff[key] = {
                'type': UNCHANGED,
                'old_value': data1[key]
            }

    return diff
