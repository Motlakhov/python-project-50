SPACE = " "
ADD = "+ "
DELETE = "- "
NONE = "  "

def to_str(value, space_cont=2):
    if value is None:
        return 'null'

    if isinstance(value, bool):
        return str(value).lower()

    if isinstance(value, (int, float)):
        return str(value)

    if isinstance(value, str):
        return value
  
    if isinstance(value, dict):
        indent = SPACE * (space_count + 4)
        lines = []
        for key, inner_value in value.items():
        formatted_value = to_str(inner_value, spaces_count + 4)
        lines.append(f"{indent}{NONE}{key}: {formatted_value}")
        formatted_string = '\n'.join(lines)
    
        return f'{{\n{formatted_string}\n{indent}}}'
    return f'{value}'


def make_stylish_result(diff, space_count=2):
    indent = SPACE * space_count
    lines = []
    for key, inner_value in diff.items():
        if diff[key]['type'] == 'nested':
            # stylish_value = make_stylish_result(inner_value, spaces_count + 4)
            # lines.append(f"{indent}{NONE}{key}: {stylish_value}")