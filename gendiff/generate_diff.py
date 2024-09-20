from gendiff.parser import parse
from gendiff.create_tree import create_difference_tree
from gendiff.styles import format_diff
import os.path


def get_extension(file_path):
    extension = os.path.splitext(file_path)[1]
    return extension[1:]


def get_file_data(file_path):
    with open(file_path) as file:
        return parse(file, get_extension(file_path))


def generate_diff(file_path1, file_path2, style='stylish'):

    data1 = get_file_data(file_path1)
    data2 = get_file_data(file_path2)

    diff_tree = create_difference_tree(data1, data2)
    formatted_diff = format_diff(diff_tree, style)

    return formatted_diff
