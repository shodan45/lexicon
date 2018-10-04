from __future__ import absolute_import

import sys
import importlib
import logging
import json
import lexicon.__main__

from types import ModuleType
from lexicon.providers.base import Provider as BaseProvider

logger = logging.getLogger(__name__)
data = [
    {'id': 'fake-id', 'type': 'TXT', 'name': 'fake.example.com', 'content': 'fake', 'ttl': 3600},
    {'id': 'fake2-id', 'type': 'TXT', 'name': 'fake2.example.com', 'content': 'fake2', 'ttl': 3600}
]

# Ensure that stdout corresponds to the given reference output
def assert_correct_output(capsys, expected_output_lines):
    out, _ = capsys.readouterr()
    assert out.splitlines() == expected_output_lines

def test_output_function_outputs_json_as_table(capsys):
    expected_output_lines = [
        'ID       TYPE NAME              CONTENT TTL ',
        '-------- ---- ----------------- ------- ----',
        'fake-id  TXT  fake.example.com  fake    3600',
        'fake2-id TXT  fake2.example.com fake2   3600',
    ]

    lexicon.__main__.handle_output(data, 'TABLE')
    assert_correct_output(capsys, expected_output_lines)

def test_output_function_outputs_json_as_table_with_no_header(capsys):
    expected_output_lines = [
        'fake-id  TXT fake.example.com  fake  3600',
        'fake2-id TXT fake2.example.com fake2 3600',
    ]

    lexicon.__main__.handle_output(data, 'TABLE-NO-HEADER')
    assert_correct_output(capsys, expected_output_lines)

def test_output_function_outputs_json_as_json_string(capsys):
    lexicon.__main__.handle_output(data, 'JSON')

    out, _ = capsys.readouterr()
    json_data = json.loads(out)

    assert json_data == data

def test_output_function_output_nothing_when_quiet(capsys):
    expected_output_lines = []

    lexicon.__main__.handle_output(data, 'QUIET')
    assert_correct_output(capsys, expected_output_lines)

def test_output_function_outputs_nothing_with_not_a_json_data(capsys):
    expected_output_lines = []

    lexicon.__main__.handle_output(True, 'TABLE')
    assert_correct_output(capsys, expected_output_lines)

    lexicon.__main__.handle_output(True, 'TABLE-NO-HEADER')
    assert_correct_output(capsys, expected_output_lines)

    lexicon.__main__.handle_output(True, 'JSON')
    assert_correct_output(capsys, expected_output_lines)