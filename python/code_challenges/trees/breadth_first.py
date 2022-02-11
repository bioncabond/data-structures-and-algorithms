from trees.binary_tree import *
from code_challenges.stack_and_queue.queue import Queue

class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None


def breadth_first(bt):
    queue = Queue()
    queue.enqueue(bt.root)
    output_list = []

    while queue.IsEmpty() == None:
        return "There is no tree to see."

    else:
        if bt.root:
            output_list.append(bt.root)

        while queue:
            current = queue.dequeue()
            output_list.append(current.value)
            if current.left:
                queue.enqueue(current.left)
            if current.right:
                queue.enqueue(current.right)
        return output_list





