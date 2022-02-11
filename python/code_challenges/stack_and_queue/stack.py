from stack_and_queue.node import Node

class Stack():
    def __init__(self, node=None):
        self.top = node
        self.size = 0

    def push(self,value):
        #make the node
        node = Node(value)
        #point to the top of the stack
        node.next = self.top
        #make the node the top
        self.top = node
        self.size += 1

    def pop(self):
        if self.size == 0:
            raise Exception("Nothing in Stack")
        if self.top != None:
            temp = self.top
            self.top = self.top.next
            temp.next = None
            return temp.value
        self.size -= 1

    def peek(self):
        if self.top == None:
            raise Exception("Nothing in Stack")
        node = self.top
        return self.top.value

    def IsEmpty(self):
        if self.top == None:
            return True


