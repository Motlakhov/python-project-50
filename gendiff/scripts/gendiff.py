#!/usr/bin/env python3
import argparse
from gendiff.scripts.generate_diff import generate_diff
from gendiff.formatters import stylish

def main():
	parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
	parser.add_argument('first_file', type=str, help='')
	parser.add_argument('second_file', type=str, help='')
	parser.add_argument('-f', '--format', help='set format of output', default='stylish')
	args = parser.parse_args()

	diff = generate_diff(args.first_file, args.second_file)
      
	if args.format == 'stylish':
         print(stylish.make_stylish_result(diff))

	# print(diff)

if __name__ == '__main__':
    main()
