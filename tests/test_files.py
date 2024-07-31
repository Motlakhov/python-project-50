import pytest
from gendiff.scripts.generate_diff import generate_diff

@pytest.mark.parametrize("file1, file2, expected_output", [
    (
        "tests/fixtures/file1.json",  # Путь к первому файлу
        "tests/fixtures/file2.json",  # Путь ко второму файлу
        '- follow: false\n  host: hexlet.io\n- proxy: 123.234.53.22\n- timeout: 50\n+ timeout: 20\n+ verbose: true'
    )
])

def test_generate_diff(file1, file2, expected_output):
    assert generate_diff(file1, file2) == expected_output

