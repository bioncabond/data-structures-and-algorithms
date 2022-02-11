try:
    from stack_and_queue.queue import Queue
    from stack_and_queue.stack import Stack
    from stack_and_queue.node import Node

except:
    from queue import Queue
    from stack import Stack
    from node import Node

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
