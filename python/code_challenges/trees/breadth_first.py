# try:
from trees.node import Node
from binary_tree import Binary_Tree
from code_challenges.stack_and_queue.queue import Queue

# except:
#     from trees.node import Node
#     from trees.binary_tree import Binary_Tree


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





