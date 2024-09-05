# Make indent with:
# SPACE = " "
# ADD = "+ "
# DELETE = "- "

def to_str(value, space_count=2):

    if value is None:
        return 'null'

    elif isinstance(value, bool):
        return str(value).lower()

    elif isinstance(value, dict):
        indent = " " * (space_count + 4)
        lines = []
        for key, inner_value in value.items():
            formatted_value = to_str(inner_value, space_count + 4)
            lines.append(f"{indent}  {key}: {formatted_value}")
        formatted_string = '\n'.join(lines)
        end_indent = " " * (space_count + 2)
        return f'{{\n{formatted_string}\n{end_indent}}}'
    else:
        return f'{value}'


def make_stylish_result(diff):
    def _iter(diff, space_count=2):
        lines = []

        for key, item in diff.items():
            indent = " " * space_count

            match item['type']:
                case 'unchanged':
                    current_value = to_str(item['old_value'], space_count)
                    lines.append(f"{indent}  {key}: {current_value}")
                case 'added':
                    current_value = to_str(item['value'], space_count)
                    lines.append(f"{indent}'+ '{key}: {current_value}")
                case 'deleted':
                    current_value = to_str(item['value'], space_count)
                    lines.append(f"{indent}'- '{key}: {current_value}")
                case 'modified':
                    current_old_value = to_str(item['old_value'], space_count)
                    current_new_value = to_str(item['new_value'], space_count)
                    lines.append(f"{indent}'- '{key}: {current_old_value}")
                    lines.append(f"{indent}'+ '{key}: {current_new_value}")
                case 'nested':
                    lines.append(f"{indent}  {key}: "
                                 f"{_iter(item['children'], space_count + 4)}")
                case _:
                    pass

        formatted_string = '\n'.join(lines)
        end_indent = " " * (space_count - 2)

        return f'{{\n{formatted_string}\n{end_indent}}}'

    return _iter(diff)
