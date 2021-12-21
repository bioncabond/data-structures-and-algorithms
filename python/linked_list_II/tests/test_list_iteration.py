import pytest
from linked_list.linked_list_iterations import LinkedList,Node
# from linked_list.linked_list import LinkedList,Node
from linked_list import __version__


#0. Mic Check
def test_version():
    assert __version__ == '0.1.0'

# 1. add a node to the end of the linked list
def test_add_node_to_end():
    ll=LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(4)
    current = 4
    assert ll.current.next == None





# 2. add multiple nodes to the end of a linked list
# 3. insert a node before a node located i the middle of a linked list
# 4.insert a node before the first node of a linked list
# 5.insert after a node in the middle of the linked list
# 6.insert a node after the last node of the linked list
