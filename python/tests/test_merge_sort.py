import pytest
# from code_challenges.merge_sort import merge_sort
from code_challenges.merge_sort.merge_sort import merge_sort

def test_merge_sort():
    sample_list = [8,4,23,42,16,15]
    expected = [4,8,15,16,23,42]
    merge_sort(sample_list)
    actual = (sample_list)
    assert actual == expected

def test_merge_sorted():
    sample_list = [20,18,12,8,5,-2]
    expected = [-2,5,8,12,18,20]
    actual = merge_sort(sample_list)
    assert actual == expected

def test_few_unique():
    sample_list = [5,12,7,5,5,7]
    expected = [5,5,5,7,7,12]
    actual = merge_sort(sample_list)
    assert actual == expected

def test_nearly_sorted():
    sample_list = [2,3,5,7,13,11]
    expected = [2,3,5,7,11,13]
    actual = merge_sort(sample_list)
    assert actual == expected
