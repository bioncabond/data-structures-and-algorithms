try:
    from stack_and_queue.queue import Queue
    from stack_and_queue.stack import Stack
    from stack_and_queue.node import Node

except:
    from queue import Queue
    from stack import Stack
    from node import Node


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
