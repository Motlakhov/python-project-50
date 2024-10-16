import pytest
import pathlib
from gendiff.generate_diff import generate_diff
from gendiff.constants import FORMATS


file1_json = pathlib.Path('tests/fixtures/file1.json')
file2_json = pathlib.Path('tests/fixtures/file2.json')
file1_yml = pathlib.Path('tests/fixtures/file1.yml')
file2_yml = pathlib.Path('tests/fixtures/file2.yml')
expected_stylish = pathlib.Path('tests/fixtures/expected_output_stylish.txt')
expected_plain = pathlib.Path('tests/fixtures/expected_output_plain.txt')


@pytest.mark.parametrize("file1, file2, formatter, expected_output", [
    (
        file1_json,  # Путь к первому файлу
        file2_json,  # Путь ко второму файлу
        FORMATS.STYLISH,
        expected_stylish
    ),
    (
        file1_yml,
        file2_yml,
        FORMATS.STYLISH,
        expected_stylish
    ),
    (
        file1_json,
        file2_json,
        FORMATS.PLAIN,
        expected_plain
    ),
    (
        file1_yml,
        file2_yml,
        FORMATS.PLAIN,
        expected_plain
    )
])
def test_generate_diff(file1, file2, formatter, expected_output):
    diff = generate_diff(file1, file2, formatter)
    expected_result = read_file(expected_output)
    assert diff == expected_result


def read_file(file_name):
    with open(file_name, 'r') as file:
        return file.read().strip()
