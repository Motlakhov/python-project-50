#!/usr/bin/env python3
import json

def generate_diff(file_path1, file_path2):
  file1 = json.load(open(file_path1))
  file2 = json.load(open(file_path2))

  diff_output = []

  all_keys = sorted(set(file1.keys()).union(set(file2.keys())))

  for key in all_keys:
      if key in file1 and key in file2:
          if file1[key] == file2[key]:
              diff_output.append(f'  {key}: {file1[key]}')
          else:
              diff_output.append(f'- {key}: {file1[key]}')
              diff_output.append(f'+ {key}: {file2[key]}')
      elif key in file1:
          diff_output.append(f'- {key}: {file1[key]}')
      else:
          diff_output.append(f'+ {key}: {file2[key]}')

  return '\n'.join(diff_output)

