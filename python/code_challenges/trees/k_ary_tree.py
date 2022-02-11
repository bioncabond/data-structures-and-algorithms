from stack_and_queue.queue import Queue

class Node:
    def __init__(self,value,children=[]):
        self.value = value
        self.children = children

class Kary_Tree:
    def __init__(self,node=None):
        self.root = node

    def breadth_first(self):
        queue = Queue()
        queue.enqueue(bt.root)
        output_list = []

        while queue:
            current = queue.dequeue()
            for node in current.children:
                queue.enqueue(node)
            output_list.append(current.value)
        return output_list

def fizz_buzz(value):
    if value % 3 and value % 5:
        return "FizzBuzz"
    if value % 3:
        return "Fizz"
    if value % 5:
        return "Buzz"
    else:
        return str(value)

def fizz_buzz_tree(tree):
    if tree.root == None:
        return ("This tree has not root.")
    else:
        queue = Queue()
        queue.enqueue(tree.root)

    while not queue.IsEmpty():
        current = queue.dequeue()
        current.value = fizz_buzz(current.value)
        for node in current.children:
            queue.enqueue(node)


if __name__ == "__main__":
    node14 = Kary_Tree(14)
    node13 = Kary_Tree(13)
    node12 = Kary_Tree(12)
    node11 = Kary_Tree(11)
    node10 = Kary_Tree(10)
    node9 = Kary_Tree(9)
    node8 = Kary_Tree(8)
    node7 = Kary_Tree(7)
    node5 = Kary_Tree(5)
    node6 = Kary_Tree(6, [node12,node13,node14])
    node4 = Kary_Tree(4, [node8,node9])
    node3 = Kary_Tree(3, [node6,node7,node10])
    node2 = Kary_Tree(2, [node4,node5,node11])
    node1 = Kary_Tree(1, [node2,node3])
    new_tree=Kary_Tree(node1)
    print(new_tree)




