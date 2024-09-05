import pytest
from gendiff.generate_diff import generate_diff


@pytest.mark.parametrize("file1, file2, formatter, expected_output", [
    (
        "tests/fixtures/file1.json",  # Путь к первому файлу
        "tests/fixtures/file2.json",  # Путь ко второму файлу
        "stylish",
        "tests/fixtures/expected_output_stylish.txt"
    ),
    (
        "tests/fixtures/file1.yml",
        "tests/fixtures/file2.yml",
        "stylish",
        "tests/fixtures/expected_output_stylish.txt"
    ),
    (
        "tests/fixtures/file1.json",
        "tests/fixtures/file2.json",
        "plain",
        "tests/fixtures/expected_output_plain.txt"
    ),
    (
        "tests/fixtures/file1.yml",
        "tests/fixtures/file2.yml",
        "plain",
        "tests/fixtures/expected_output_plain.txt"
    ),
    (
        "tests/fixtures/file1.json",
        "tests/fixtures/file2.json",
        "json",
        "tests/fixtures/expected_output_json.txt"
    ),
    (
        "tests/fixtures/file1.yml",
        "tests/fixtures/file2.yml",
        "json",
        "tests/fixtures/expected_output_json.txt"
    )
])
def test_generate_diff(file1, file2, formatter, expected_output):
    diff = generate_diff(file1, file2, formatter)
    expected_result = read_file(expected_output)
    assert diff == expected_result


def read_file(file_name):
    with open(file_name, 'r') as file:
        return file.read().strip()
