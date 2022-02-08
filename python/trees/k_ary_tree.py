from stack_and_queues.queue import Queue


class Node:
    def __init__(self,value,children):
        self.value = value
        self.children = children


    def tree_helper(self,tree):
        tree_queue = Queue()

        if self.value == None:
            return "There is nothing in the tree."
        else:
           while Queue:
                new_front = self.value
                if self.children:
                    tree_queue.enqueue(self.children)
                    tree_queue.dequeue(new_front)
                else:
                    str(self.value)
                return new_front,self.value

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
        print("Tree?")



if __name__ == "__main__":
    tree = Binary_Tree()
    tree.root = Node(1)
    tree.children = Node(5)
    tree.children = Node(30)
    tree.children.children = Node(3)
    tree.children.children = Node(15)
