from stack_and_queue.node import Node
from stack_and_queue.stack import Stack


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

    def IsEmpty(self):
        if self.len == 0:
            return True

    def enqueue(self,value):
        self.len +=1
        self.s1.push(value)
        print(f"Prepop:S1-Enqueue: {value} S1-Size: {self.len}")
        result = self.s1.pop()
        print(f"POSTPOP: S1-Enqueue: {value} S1-Size: {self.len}")

    def dequeue(self):
        if self.s2.IsEmpty():
            print(f"We in this?")
            while self.len > 0:
                self.s2.push(self.s1.pop())
                print(f"s2: {self.s2}")
                self.len-=1
                print(f"this is len: {self.len}")
            result = self.s2.pop()
            print(f"result: {result}")

            while True:
                self.s1.push(self.s2.pop())
                print(f"SSS2: {self.s2}")

                self.len += 1
                if self.s2.IsEmpty():
                    return result
        else:
            return "Empty stack over here!"








if __name__ == "__main__":

    # q = Queue()
    # q.enqueue("apple")
    # q.enqueue("car")
    # q.enqueue("zelda")
    p = Pseudo_queue()
    p.enqueue("pizza")
    p.enqueue("wings")
    p.enqueue("burgers")
    print(p.dequeue())




