import pytest
from linked_list.linked_list import LinkedList,Node
from linked_list import __version__

#0. Mic Check#
def test_version():
    assert __version__ == '0.1.0'

#0a. Test of the Node instance
def test_node_instance():
    node = Node(1, None)
    assert node.next == None
    assert node.value == 1

#0a. No False Positives Here
def test_node_instance_fail():
    node = Node(1, None)
    assert node.next != node
    assert node.value != 2

#1. Successfully Instantiate an Empty Linked List
def test_linked_list_empty():
    ll = LinkedList()
    assert ll.head == None


#2. Can Instert into the Linked List
def test_linked_list_insert():
    ll = LinkedList()
    ll.insert('Link')
    assert ll.head.value == 'Link'

#3. Head property will properly point to the first node in the linked list
def test_head_points_to_first_node():
    ll = LinkedList()
    ll.insert('Ian')
    assert ll.head.value == 'Ian'


#4. Insert multiple nodes into the linked list
def test_add_multiple_nodes():
    ll = LinkedList()
    ll.insert('Ian')
    ll.insert('Chris')
    assert 'Ian' , 'Chris' in LinkedList

# #5. return true when finding a value within the linked list that exists
def test_value_exist_in_list():
    ll = LinkedList()
    node1 = ll.insert('Pookie')
    ll.head = node1

    node2 = ll.insert('Ray-Ray')
    # node1.next = node2

    ll.includes('Pookie')
    assert True

#6. return false when searching a value within the linked list that doesnt exist
def test_value_exist_in_list():
    ll = LinkedList()
    node1 = ll.insert('Pookie')
    ll.head = node1

    node2 = ll.insert('Ray-Ray')
    # node1.next = node2

    test=ll.includes('Josh')
    assert test == False

#7. Return a collection of all the values that exist in the linked list
def test_return_all_values():
    ll=LinkedList()

    node1 = ll.insert('Pookie')
    ll.head = node1
    node2 = ll.insert('Ray-Ray')
    node3 = ll.insert('Josh')
    test = ll.to_string()
    assert test == ('Josh -> Ray-Ray -> Pookie -> NULL')




