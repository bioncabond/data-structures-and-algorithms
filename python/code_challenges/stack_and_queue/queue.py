from __future__ import annotations
from stack_and_queue.node import Node
from stack_and_queue.animal_shelter import Animal_shelter
import sys


class Queue:
    def __init__(self,front=None,rear=None):
        self.front = front
        self.rear = rear
        self.size = 0

    def IsEmpty(self):
        if self.front == None:
            return True

    def enqueue(self,value):
        node = Node(value)
        if self.IsEmpty() == True:
            self.front = self.rear = node
        else:
            self.rear.next = node
        self.size +=1
        print(f"Enqueue: {node.value}")
        print(f"Size: {self.size}")

    def dequeue(self,value):
        node =Node(value)
        if self.IsEmpty() == True:
            self.front = self.rear = node
        else:
            self.front = self.front.next
            node.next = None
            self.size -=1
        print(f"Dequeue: {node.value}")
        print(f"Size: {self.size}")

    def peek(self):
         return self.front.value



if __name__ == "__main__":

    # q = Queue()
    # q.enqueue("apple")
    # q.enqueue("car")
    # q.enqueue("zelda")
    # p = Pseudo_queue()
    # p.enqueue("pizza")
    # p.enqueue("wings")
    # p.enqueue("burgers")
    # p.dequeue()
    a = Animal_shelter()
    a.enqueue("dog")
    a.enqueue("cat")
    a.enqueue("cat")
    a.dequeue("dog")

