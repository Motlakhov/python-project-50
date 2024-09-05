#!/usr/bin/env python3
from gendiff.parser import parse_file
from gendiff.create_tree import build_diff
from gendiff.constants import FORMATTERS


def generate_diff(file_path1, file_path2, formatter='stylish'):
    file1 = parse_file(file_path1)
    file2 = parse_file(file_path2)

    diff = build_diff(file1, file2)

    if isinstance(formatter, str):
        formatter_func = FORMATTERS[formatter]
    else:
        formatter_func = formatter

    return formatter_func(diff)
