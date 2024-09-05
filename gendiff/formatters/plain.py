def to_str(value):
    if isinstance(value, (bool, int)):
        return str(value).lower()
    if value is None:
        return 'null'
    if isinstance(value, dict):
        return '[complex value]'
    
    return f"'{value}'"
    


def make_plain_result(diff):
    def _iter(diff, path=""):
        lines = []

        for key, item in diff.items():
            current_path = f'{path}.{key}' if path else key

            if isinstance(key, dict):
                current_value = '[complex value]'

            match item['type']:
                case 'nested':
                    lines.extend(_iter(item["children"], current_path))
                case 'added':
                    current_value = to_str(item['value'])
                    if isinstance(item['value'], dict):
                        lines.append(f"Property '{current_path}' was added "
                                     f"with value: [complex value]")
                    else:
                        current_value = to_str(item['value'])
                        lines.append(f"Property '{current_path}' was added "
                                     f"with value: {current_value}")
                case 'deleted':
                    lines.append(f"Property '{current_path}' was removed")
                case 'modified':
                    old_value = to_str(item['old_value'])
                    new_value = to_str(item['new_value'])

                    if isinstance(item['old_value'], dict):
                        old_value = '[complex value]'
                    if isinstance(item['new_value'], dict):
                        new_value = '[complex value]'
                    lines.append(f"Property '{current_path}' was updated. "
                                 f"From {old_value} to {new_value}")
        return lines
    return '\n'.join(_iter(diff))
