from gendiff.constants import CHANGES_TYPES


def create_difference_tree(data1, data2):
    diff = {}

    keys = sorted(data1.keys() | data2.keys())

    for key in keys:

        if key not in data1:
            diff[key] = {
                'type': CHANGES_TYPES.ADDED,
                'value': data2[key]
            }

        elif key not in data2:
            diff[key] = {
                'type': CHANGES_TYPES.REMOVED,
                'value': data1[key]
            }

        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            diff[key] = {
                'type': CHANGES_TYPES.NESTED,
                'children': create_difference_tree(data1[key], data2[key])
            }

        elif data1[key] != data2[key]:
            diff[key] = {
                'type': CHANGES_TYPES.UPDATED,
                'old_value': data1[key],
                'new_value': data2[key]
            }

        else:
            diff[key] = {
                'type': CHANGES_TYPES.UNCHANGED,
                'old_value': data1[key]
            }

    return diff
