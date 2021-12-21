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

#0b. No False Positives Here
def test_node_instance_fail():
    node = Node(1, None)
    assert node.next != node
    assert node.value != 2

#1. Successfully Instantiate an Empty Linked List
def test_linked_list_empty():
    ll = LinkedList()
    assert ll.head == None


#2. Can Insert into the Linked List
def test_linked_list_insert():
    ll = LinkedList()
    ll.insert('Link')
    assert ll.head.value == 'Link'

#3. Head property will properly point to the first node in the linked list
def test_head_points_to_first_node():
    ll = LinkedList()
    ll.insert('Ian')
    ll.insert ('Josh')
    assert ll.head.next.value == 'Ian'


#4. Insert multiple nodes into the linked list
def test_add_multiple_nodes():
    ll = LinkedList()
    ll.insert('Ian')
    ll.insert('Chris')
    assert ll.head.value == 'Chris'

# #5. return true when finding a value within the linked list that exists
def test_value_exist_in_list():
    ll = LinkedList()
    node1 = ll.insert('Pookie')
    ll.head == node1

    node2 = ll.insert('Ray-Ray')
    # node1.next = node2
    test_node = ll.includes('Ray-Ray')

    assert test_node == True

#6. return false when searching a value within the linked list that doesnt exist
def test_value_exist_not_in_list():
    ll = LinkedList()
    node1 = ll.insert('Pookie')
    ll.head == node1

    node2 = ll.insert('Ray-Ray')
    # node1.next = node2
    test_node = ll.includes('Bionca')

    assert test_node == False

#7. Return a collection of all the values that exist in the linked list
def test_return_all_values():
    ll=LinkedList()

    node1 = ll.insert('Pookie')
    ll.head == node1
    node2 = ll.insert('Ray-Ray')
    node3 = ll.insert('Josh')
    test = ll.to_string()
    assert test == 'Josh -> Ray-Ray -> Pookie -> NULL'


## Lab 06
    #0. Mic Check
def test_version():
    assert __version__ == '0.1.0'

# 1. add a node to the end of the linked list
def test_add_node_to_end():
    ll=LinkedList()
    ll.insert(3)
    ll.insert(1)
    ll.append(2)
    assert ll.to_string() == '1 -> 3 -> 2 -> NULL'

# 2. add multiple nodes to the end of a linked list
def test_add_multiple_nodes_to_end():
    ll=LinkedList()
    ll.insert(3)
    ll.insert(8)
    ll.append(5)
    ll.append(6)
    assert ll.to_string() == '8 -> 3 -> 5 -> 6 -> NULL'

# 3. insert a node before a node located in the middle of a linked list
def test_before_a_location():
    ll=LinkedList()
    ll.insert(3)
    ll.insert(8)
    ll.insert(5)
    ll.insert_before(8,1)
    assert ll.to_string() == '5 -> 1 -> 8 -> 3 -> NULL'


# 4.insert a node before the first node of a linked list
def test_before_first_node():
    ll=LinkedList()
    ll.insert(3)
    ll.insert(8)
    ll.insert(5)
    ll.insert_before(5,1)
    assert ll.to_string() == '1 -> 5 -> 8 -> 3 -> NULL'

# 5.insert after a node in the middle of the linked list
def test_after_a_location():
    ll=LinkedList()
    ll.insert(3)
    ll.insert(8)
    ll.insert(5)
    ll.insert_after(8,1)
    assert ll.to_string() == '5 -> 8 -> 1 -> 3 -> NULL'

# 6.insert a node after the last node of the linked list
def test_after_last_node():
    ll=LinkedList()
    ll.insert(3)
    ll.insert(8)
    ll.insert(5)
    ll.insert_after(3,1)
    assert ll.to_string() == '5 -> 8 -> 3 -> 1 -> NULL'





