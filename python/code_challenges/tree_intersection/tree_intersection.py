from code_challenges.hash_tables.hashtable import Hashtable
from code_challenges.trees.binary_tree import Binary_Tree

def tree_intersection(tree_1,tree_2):
    new_num = []
    tree_1 = tree_1.pre_order()
    tree_2 = tree_2.pre_order()
    hashtable = Hashtable()
    for value in tree_1:
        hashtable.set(key=str(value), value=value)
    for value in tree_2:
        if hashtable.contains(str(value)):
            new_num.append(value)
    return new_num


