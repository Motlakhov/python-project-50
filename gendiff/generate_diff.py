from gendiff.parser import parse
from gendiff.create_tree import build_diff
from gendiff.styles.stylish import to_stylish
from gendiff.styles.plain import to_plain
from gendiff.styles.json import to_json
import os.path


def get_extension(file_path):
    _, extension = os.path.splitext(file_path)
    return extension


def get_file_data(file_path):
    with open(file_path) as file:
        return parse(file, get_extension(file_path))


def generate_diff(file_path1, file_path2, style='stylish'):

    file1 = get_file_data(file_path1)
    file2 = get_file_data(file_path2)

    diff = build_diff(file1, file2)

    if style == 'stylish':
        return to_stylish(diff)
    elif style == 'plain':
        return to_plain(diff)
    elif style == 'json':
        return to_json(diff)
    else:
        raise ValueError(f'Unknown format: {style}')
