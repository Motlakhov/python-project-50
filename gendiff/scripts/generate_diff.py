#!/usr/bin/env python3
import json
import yaml
from gendiff.parser import parse_file
from gendiff.formatters.stylish import make_stylish_result
from gendiff.formatters.plain import make_plain_result
from gendiff.create_tree import build_diff

FORMATTERS = {
    'stylish': make_stylish_result,
    'plain': make_plain_result
}

def generate_diff(file_path1, file_path2, formatter = 'stylish'):
    file1 = parse_file(file_path1)
    file2 = parse_file(file_path2)
    
    diff = build_diff(file1, file2)
    
    if isinstance(formatter, str):
        formatter_func = FORMATTERS[formatter] 
    else:
        formatter_func = formatter  # Это может быть функция, если формат был получен иначе

    return formatter_func(diff)

  # diff = build_diff(file1, file2)

  # return diff

  # diff_output = []

  # all_keys = sorted(set(file1.keys()).union(set(file2.keys())))

  # for key in all_keys:
  #     if key in file1 and key in file2:
  #         if file1[key] == file2[key]:
  #             diff_output.append(f'  {key}: {file1[key]}'.lower())
  #         else:
  #             diff_output.append(f'- {key}: {file1[key]}'.lower())
  #             diff_output.append(f'+ {key}: {file2[key]}'.lower())
  #     elif key in file1:
  #         diff_output.append(f'- {key}: {file1[key]}'.lower())
  #     else:
  #         diff_output.append(f'+ {key}: {file2[key]}'.lower())

  # diff = '\n'.join(diff_output)
  # return diff
