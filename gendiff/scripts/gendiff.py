#!/usr/bin/env python3
import argparse
from gendiff.scripts.generate_diff import generate_diff


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
        )
    parser.add_argument('first_file', type=str, help='')
    parser.add_argument('second_file', type=str, help='')
    parser.add_argument('-f', '--format',
                        help='set format of output',
                        default='stylish',
                        choices=['stylish', 'plain', 'json'])
    args = parser.parse_args()
    file_path1 = args.first_file
    file_path2 = args.second_file
    formatter = args.format

    diff = generate_diff(file_path1, file_path2, formatter)

    print(diff)


if __name__ == '__main__':
    main()
