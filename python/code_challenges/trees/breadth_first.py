# from code_challenges.trees.binary_tree import Binary_Tree
from code_challenges.trees.node import Node
from code_challenges.stack_and_queue.queue import Queue


def breadth_first(bt):
    queue = Queue()
    queue.enqueue(bt.root)
    output_list = []

    while queue.IsEmpty() is False:
        front = queue.dequeue()
        output_list.append(front.value)

        if front.left is not None:
            queue.enqueue(front.left)

        if front.right is not None:
            queue.enqueue(front.right)
    return output_list







