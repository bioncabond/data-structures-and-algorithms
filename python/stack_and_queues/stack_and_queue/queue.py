from stack_and_queue.node import Node
from stack_and_queue.stack import Stack
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


class Pseudo_queue():

    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()
        self.len = 0

    def enqueue(self,value):
        if self.s2.top == None:
            self.s2.push(value)
        else:
            status = True
            while status == True:
                if self.s2.top == None:
                    status = False
                else:
                    temp = self.s2.pop()
                    self.s1.push(temp)
            self.s1.push(value)
            # print(f"{self.s1.top.value}")

            status = True
            while status == True:
                if self.s1.top == None:
                    status = False
                else:
                    temp = self.s1.pop()
                    self.s2.push(temp)
        self.len +=1

    def dequeue(self):
        self.len -=1
        return self.s2.pop()


class Animal_shelter(object):

    def __init__(self):
        self.queue_1 = Queue()
        self.queue_2 = Queue()
        # self.current_queue = self.queue_1
        # self.next_queue = self.queue_2
        self.size = 0
        self.head = None

    def __str__(self):
        current = self.head
        while current:
            current = current.next

    def enqueue(self,animal_type):
        if self.queue_2 == None:
            self.queue_2.push(animal_type)
        else:
            if animal_type == 'dog' or animal_type == 'cat':
                to_add = animal_type
                self.size +=1
                if not self.head:
                    self.head = to_add
                else:
                    temp_animal = self.head
                    print (f'{animal_type} {self.size} toadd: {to_add} {self.head}')

                    while temp_animal.next != None:
                        temp_animal.next = self.head

            else:
                print(f'We dont keep {animal_type}s here')

    # def dequeue(self,animal_type):

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
    a.enqueue("dog")
    a.enqueue("cat")
    # a.enqueue("bear")

    # print(a.enqueue())
