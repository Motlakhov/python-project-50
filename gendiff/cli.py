import argparse
from gendiff.constants import FORMATS


def get_args():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file', type=str, help='')
    parser.add_argument('second_file', type=str, help='')
    parser.add_argument('-f', '--format',
                        default='stylish',
                        help=f'select format of output from '
                             f'[{", ".join(FORMATS)}]')

    return parser.parse_args()
