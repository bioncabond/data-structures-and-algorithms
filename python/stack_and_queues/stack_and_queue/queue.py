from __future__ import annotations
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



# class Animal():
#     def __init__(self,animal):
#         self.animal = animal
#         self.animal_type = self.only_dogs_and_cats()

#     def only_dogs_and_cats(self):
#         small_animal = self.animal
#         if small_animal in ['dog','cat']:
#             return small_animal
#         else:
#             print("We don't have that here.")


class Animal_shelter():

    # class _Node():
    #     def __init__(self,value,next=None)
    #     self.value = value


    def __init__(self):
        self.stack = Stack()
        self.size = 0
        self.front = None
        self.rear = None
        self.queue = Queue()
        self.animal_type= ""


    def isEmpty(self):
        return self.size == 0

    def enqueue(self,animal_type):
        # print(f'inside enqueue {animal_type}')
        node = Node(animal_type)

        if self.isEmpty() == True:
            self.queue.front = node
            self.queue.rear = node
        else:
            self.queue.rear.next = node
            self.queue.rear = node
        self.size += 1


    def dequeue(self,pref_animal):
        status = True
        while status == True:
            if pref_animal == self.queue.front.value:
                self.animal_type = self.queue.front.value
                status = False
            else:
                temp = self.queue.front
                self.stack.push(self.queue.front)
                self.queue.front = self.queue.front.next

        while self.stack.top != None:
            temp = self.queue.front
            self.queue.font = self.stack.pop()
            self.queue.front.next = temp

        self.size -= 1
        print(f'dequeue: {self.animal_type} {self.size}')
        return self.animal_type
    # 1 while:
    ##check each time if the pref = dog or cat (animal_type)
        ##if it matches
        # return and exit
    # 2 while:
    ## push everything in the stack
    ##back to the queue and set the front of the queue to the next node
    ##use pop to get the last one off the stack and return it

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

