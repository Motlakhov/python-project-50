from gendiff.formatters.stylish import make_stylish_result
from gendiff.formatters.plain import make_plain_result
from gendiff.formatters.json import make_json_result


FORMATTERS = {
    'stylish': make_stylish_result,
    'plain': make_plain_result,
    'json': make_json_result
}

# DIFF_TYPES
ADDED = 'added',
DELETED = 'deleted',
NESTED = 'nested',
MODIFIED = 'modified',
UNCHANGED = 'unchanged'

# Make indent with:
SPACE = " "
ADD = "+ "
DELETE = "- "
