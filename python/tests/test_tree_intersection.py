from code_challenges.tree_intersection.tree_intersection import tree_intersection
from code_challenges.trees.binary_tree import Binary_Tree,Node
import pytest

def test_pol():
    assert tree_intersection

def test_nodes():
    tree = Binary_Tree()
    node = Node(0)
    assert tree
    assert node

def test_first_tree(binary_tree_1,binary_tree_2):
    actual = tree_intersection(binary_tree_1,binary_tree_2)
    expected = [6,11]
    assert actual == expected

def test_no_dups(binary_tree_1,binary_tree_2):
    actual = tree_intersection(binary_tree_1,binary_tree_2)
    expected = [6,11]
    assert actual == expected


@pytest.fixture
def binary_tree_1():
    tree1 = Binary_Tree()
    tree1.root = Node(2)
    tree1.root.left = Node(6)
    tree1.root.right = Node(11)
    tree1.root.left.right = Node(25)
    return tree1

@pytest.fixture
def binary_tree_2():
    tree2 = Binary_Tree()
    tree2.root = Node(3)
    tree2.root.left = Node(6)
    tree2.root.right = Node(11)
    tree2.root.left.right = Node(22)
    return tree2
