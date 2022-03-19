from code_challenges.trees.node import Node

class Binary_Tree:
    def __init__(self,root=None):
        self.root = root

    def add(self,value):
        node = Node(value)
        if self.is_empty():
            self.root = node

    # root > left > right
    def pre_order(self):
        # empty list for values
        values = []

        def walk(root):
            if root is None:
                return

            values.append(root.value)
            walk(root.left)
            walk(root.right)

        walk(self.root)
        return values

    #left >> root >> right
    def in_order(self,root):
        values = []

        if root != None:
            values = self.in_order(root.left)
            values.append(root.value)
            values = values + self.in_order(root.right)
        return values


    #left >> right >> root
    def post_order(self,root):
        values = []

        if root!= None:
            values = self.post_order(root.left) #eggs
            values = values + self.post_order(root.right) #ham
            print(f"this is values: {values}")
            values.append(root.value) #green
        return values


    def max_value(self,current):
        if not self.root:
            return "There are no roots to this tree."

        else:
            max = current.value

            if current.right != None:
                right_max = self.max_value(current.right)
                if right_max > max:
                    max = right_max

            if current.left != None:
                left_max = self.max_value(current.left)
                if left_max > max:
                    max = left_max
        return max

    def is_empty(self):
            try:
                self.root.value
                return False
            except:
                return True

class Binary_Search(Binary_Tree):

    def add(self,value):
        #make our new NODE
        new_node = Node(value)

        #if self's node is not the root make it the root
        if not self.root:
            self.root = new_node
        #if it is the root
        else:
            current_node = self.root

            #while we have a current node
            while current_node:
                #if the new node value < current node:
                if new_node.value < current_node.value:
                    #check to the left
                    if current_node.left != None:
                        #if something is left set to the left node
                        current_node = current_node.left
                    else:
                        #if not set the current node to a new node; this means its a leaf.
                        current_node.left = new_node
                        break
                #if the new node value > current node:
                else:
                    #and if there is something to the right
                    if current_node.right != None:
                        #make that node the right node
                        current_node = current_node.right
                    else:
                        #if there is nothing; we are on a leaf
                        current_node.right = new_node
                        break

    def contains(self,node,value):
        if node:
            if node.value == value:
                return True
            if node.value > value:
                return self.contains(node.left,value)
            if node.value < value:
                return self.contains(node.right,value)
        else:
            return False






