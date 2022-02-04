import pytest
from stack_and_queue.validate_brackets import *


def test_string_one():
    string = "{[]{()}}"
    actual = validate_brackets(string)
    expected = True
    assert actual == expected

def test_string_two():
    string = "[[()]]"
    actual = validate_brackets(string)
    expected = True
    assert actual == expected

def test_string_three_spaces():
    string = "{ [ ) )"
    actual = validate_brackets(string)
    expected = False
    assert actual == expected

def test_empty_string():
    string = ""
    actual = validate_brackets(string)
    expected = True
    assert actual == expected
