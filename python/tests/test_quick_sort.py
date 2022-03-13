import pytest
from code_challenges.quick_sort.quick_sort import quick_sort

def test_sort_sample():
    arr = [8,4,23,42,16,15]
    n = len(arr)
    quick_sort(arr,0,n-1)
    actual = arr
    expected=[4, 8, 15, 16, 23, 42]
    assert actual == expected

def test_reverse_sorted():
    arr = [20,18,12,8,5,-2]
    n = len(arr)
    quick_sort(arr,0,n-1)
    actual = arr
    expected =[-2, 5, 8, 12, 18, 20]
    assert actual == expected

def test_few_uniques():
    arr = [5,12,7,5,5,7]
    n = len(arr)
    quick_sort(arr,0,n-1)
    actual = arr
    expected =[5,5,5,7,7,12]
    assert actual == expected

def test_nearly_sorted():
    arr = [2,3,5,7,13,11]
    n = len(arr)
    quick_sort(arr,0,n-1)
    actual = arr
    expected =[2,3,5,7,11,13]
    assert actual == expected

def test_expected_failure():
    arr = [-5,5,8,2,3,4]
    n = len(arr)
    quick_sort(arr,0,n-1)
    actual = arr
    expected =[-5,5,2,8,3,4]
    assert actual != expected
