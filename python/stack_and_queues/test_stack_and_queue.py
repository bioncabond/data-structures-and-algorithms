import pytest
from stack_and_queue import __version__
# from stack_and_queue.node import Node
from stack_and_queue.queue import Queue,Pseudo_queue
from stack_and_queue.stack import Stack


#0. Mic Check#
def test_version():
    assert __version__ == '0.1.0'

#Push Test
#1.0- Successfully push onto a stack:
def test_push_on_stack():
    sl = Stack()
    sl.push("apple")
    assert sl.top.value == "apple"

#1.1- Successfully push multiple onto a stack:
def test_push_multi_on_stack():
    sl = Stack()
    sl.push("apple")
    sl.push("car")
    assert sl.top.value == "car"

#Pop Test
#2.0- Successfully pop off the stack:
def test_push_on_stack():
    sl = Stack()
    sl.push("apple")
    sl.push("car")
    sl.push("zelda")
    sl.pop()
    sl.pop()
    assert sl.top.value == "apple"

#2.1- Successfully pop off the stack until empty:
def test_pop_to_death():
    sl = Stack()
    sl.push("apple")
    sl.push("car")
    sl.push("zelda")
    while sl.top:
        sl.pop()
    assert sl.top == None

#Peek Test
#3.0- Successfully peek the next item on the stack:
def test_peek_next_stack():
    sl = Stack()
    sl.push("apple")
    sl.push("car")
    sl.push("zelda")
    sl.peek()
    assert sl.top.value == "zelda"

#IsEmpty Test
#4.0- Instantiate an empty stack
def test_peek_next_stack():
    sl = Stack()
    expected = sl.IsEmpty()
    assert expected == True

# Raise Stack Exception
# 5.0- pop or peek on empty stack raises exception
def test_peek_stack_exception():
    with pytest.raises(Exception):
        sl = Stack()
        expected = sl.pop()
        assert expected == ("Nothing in the Stack")

#Queue
#1.0- Enqueue into a queue
def test_enqueue_into_queue():
    q = Queue()
    q.enqueue("apple")
    q.enqueue("car")
    q.enqueue("zelda")
    expected = q.peek()
    assert expected == "apple"

def test_enqueue_multi_into_queue():
    q = Queue()
    q.enqueue("apple")
    q.enqueue("car")
    q.enqueue("zelda")
    actual = q.size
    expected = 3
    assert expected == actual

def test_dequeue_from_queue():
    q = Queue()
    q.enqueue("apple")
    q.enqueue("car")
    q.enqueue("zelda")
    q.enqueue("mario")
    q.dequeue("mario")
    actual = q.size
    expected = 3
    assert expected == actual

def test_peek_into_queue():
    q = Queue()
    q.enqueue("boat")
    actual = q.peek()
    expected = "boat"
    assert expected == actual

def test_peek_into_queue_exception():
    with pytest.raises(Exception):
        q = Queue()
        q.enqueue("boat")
        q.dequeue("boat")
        actual = q.peek()
        expected = "boat"
        assert expected == actual

def test_dequeue_mulit_from_queue():
    q = Queue()
    q.enqueue("apple")
    q.enqueue("car")
    q.dequeue("car")
    q.dequeue("apple")
    actual = q.size
    expected = 0
    assert expected == actual

def test_instantiate_empty_queue():
    q=Queue()
    actual = q.IsEmpty()
    expected = True
    assert expected == actual

#Pseudo Queue Test
def test_enqueue_stack():
    p = Pseudo_queue()
    p.enqueue("green")
    p.enqueue("red")
    p.enqueue("blue")
    actual = p.len
    expected = 3
    assert expected == actual

def test_push_s1_into_s2():
    p = Pseudo_queue()
    p.enqueue("green")
    p.enqueue("red")
    p.enqueue("blue")
    expected = p.s2.top.value
    assert expected == "green"

def test_s1_empty():
    p = Pseudo_queue()
    expected = p.s1.top
    assert expected == None

def test_s2_empty():
    p = Pseudo_queue()
    expected = p.s2.top
    assert expected == None

def test_dequeue_stack():
    p = Pseudo_queue()
    p.enqueue("green")
    p.enqueue("red")
    p.enqueue("blue")
    p.dequeue()
    p.dequeue()
    actual = p.len
    expected = 1
    assert expected == actual



