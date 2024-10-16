from gendiff.constants import CHANGES_TYPES


def build_indent(depth):
    return " " * (depth * 2)


def format_data(lines):
    return '\n'.join(lines)


def put_into_braces(lines_string, depth):
    end_indent = build_indent(depth + 1)
    return f'{{\n{lines_string}\n{end_indent}}}'


def to_string(value, depth):

    if value is None:
        return 'null'

    if isinstance(value, bool):
        return str(value).lower()

    if isinstance(value, dict):
        lines = []
        for key, val in value.items():
            lines.append(f"{build_indent(depth + 2)}  "
                         f"{key}: {to_string(val, depth + 2)}")
            lines_string = format_data(lines)
        return put_into_braces(lines_string, depth)
    return value


def to_stylish(diff):
    def _iter_stylish(diff, depth=1):
        lines = []

        for key, item in diff.items():
            indent = build_indent(depth)

            match item['type']:
                case CHANGES_TYPES.UNCHANGED:
                    current_value = to_string(item['old_value'], depth)
                    lines.append(f"{indent}  {key}: {current_value}")
                case CHANGES_TYPES.ADDED:
                    current_value = to_string(item['value'], depth)
                    lines.append(f"{indent}+ {key}: {current_value}")
                case CHANGES_TYPES.REMOVED:
                    current_value = to_string(item['value'], depth)
                    lines.append(f"{indent}- {key}: {current_value}")
                case CHANGES_TYPES.UPDATED:
                    current_old_value = to_string(item['old_value'], depth)
                    current_new_value = to_string(item['new_value'], depth)
                    lines.append(f"{indent}- {key}: {current_old_value}")
                    lines.append(f"{indent}+ {key}: {current_new_value}")
                case CHANGES_TYPES.NESTED:
                    lines.append(
                        f"{indent}  {key}: "
                        f"{_iter_stylish(item['children'], depth + 2)}"
                        )
                case _:
                    raise ValueError(f'Unknown type: {item["type"]}')

        formatted_string = format_data(lines)
        result_string = put_into_braces(formatted_string, depth - 2)
        return result_string

    return _iter_stylish(diff)
