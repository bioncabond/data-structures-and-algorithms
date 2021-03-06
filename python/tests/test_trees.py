
from code_challenges.trees.node import Node
from code_challenges.trees.binary_tree import Binary_Search, Binary_Tree
from code_challenges.trees.breadth_first import breadth_first
import pytest

# #0 Mic Check
# def test_version():
#     assert __version__ == '0.1.0'

#Binary_Tree Class Testing

def test_add_empty_tree():
    bt = Binary_Tree()
    assert bt.root == None

def test_bt_in_order():
    green = Node('green')
    eggs = Node('eggs')
    ham = Node('ham')

    #set the root to 'green'
    bt = Binary_Tree(green)
    green.left = eggs
    green.right = ham
    print(f"green left {green.left} ")
    in_order_list = bt.in_order(green)
    assert in_order_list == ['eggs','green','ham']

def test_bt_pre_order():
    green = Node('green')
    eggs = Node('eggs')
    ham = Node('ham')

    #set the root to 'green'
    bt = Binary_Tree(green)
    green.left = eggs
    green.right = ham

    post_order_list = bt.post_order(green)
    assert post_order_list == ['eggs','ham','green']

#Binary_Search Class Testing

def test_add_root():
    binary_search = Binary_Search()
    binary_search.add(8)
    assert binary_search.root.value == 8

def test_add_left():
    binary_search = Binary_Search()
    binary_search.add(8)
    binary_search.add(4)
    assert binary_search.root.left.value == 4

def test_add_right():
    binary_search = Binary_Search()
    binary_search.add(8)
    binary_search.add(12)
    assert binary_search.root.right.value == 12

def test_contains():
    # bst = prepare_bst
    binary_search = Binary_Search()
    binary_search.add(8)
    binary_search.add(12)
    binary_search.add(27)
    # binary_search.contains(binary_search.root, 8) == True
    assert binary_search.contains(binary_search.root,8) == True
    assert binary_search.contains(binary_search.root,27) == True
    assert binary_search.contains(binary_search.root,500) == False

#Max Value Test
def test_max_value():
    binary_search = Binary_Search()
    binary_search.add(8)
    binary_search.add(12)
    binary_search.add(27)
    binary_search.add(45)
    assert binary_search.max_value(binary_search.root) == 45

def test_max_value_for_empty():
    binary_search = Binary_Search()
    assert binary_search.max_value(binary_search.root) == "There are no roots to this tree."

#Breadthfirst Test
# def test_for_output_list():
#    a = Node("a")
#    b = Node("b")
#    c = Node("c")
#    bt = Binary_Tree(a)

#    a.left = b
#    a.right = c
#    expected = breadth_first(bt)
#    assert expected == ['a','b','c']

# def test_breadth_multiple_val():
#     apple = Node("apple")
#     pear = Node("pear")
#     orange = Node("orange")

#     bt = Binary_Tree(apple)
#     apple.left = pear
#     apple.right = orange
#     expected = breadth_first(bt)
#     assert expected == ["apple", "pear", "orange"]

def test_breadth_single_val():
    bt = Binary_Tree()
    bt.add("apple")
    expected = breadth_first(bt)
    assert expected == ["apple"]
