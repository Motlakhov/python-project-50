from gendiff.constants import FORMATS
from gendiff.styles.stylish import to_stylish
from gendiff.styles.plain import to_plain
from gendiff.styles.json import to_json


def format_diff(data, style):
    match style:
        case FORMATS.PLAIN:
            return to_plain(data)
        case FORMATS.STYLISH:
            return to_stylish(data)
        case FORMATS.JSON:
            return to_json(data)
        case _:
            raise ValueError(f'Unknown format: {style}, '
                             f' please choose from [{", ".join(FORMATS)}]')
