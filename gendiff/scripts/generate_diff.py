#!/usr/bin/env python3
import json
import yaml
from gendiff.parser import parse_file
from gendiff.formatters.stylish import make_stylish_result
from gendiff.formatters.plain import make_plain_result
from gendiff.formatters.json import make_json_result
from gendiff.create_tree import build_diff

FORMATTERS = {
    'stylish': make_stylish_result,
    'plain': make_plain_result,
    'json': make_json_result
}

def generate_diff(file_path1, file_path2, formatter = 'stylish'):
    file1 = parse_file(file_path1)
    file2 = parse_file(file_path2)
    
    diff = build_diff(file1, file2)
    
    if isinstance(formatter, str):
        formatter_func = FORMATTERS[formatter] 
    else:
        formatter_func = formatter  

    return formatter_func(diff)

