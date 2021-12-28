
def Error_Handler(func):
    def Inner_Function(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except TypeError:
            print(f"{func.__name__} is broken! ")
    return Inner_Function

##Make the Node Class
class Node:
    def __init__(self,value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self, head=None, value=None):
        self.head=head
        self.value = value
        current = self.head

    # @Error_Handler
    def insert(self, value):
        node = Node(value)
        if self.head != None:
            node.next = self.head
        self.head = node

    def includes(self,item):
        current = self.head
        while current:
            if current.value == item:
                return True
            current = current.next
        return False

    def to_string(self):
        current=self.head
        output_string = ''

        while current is not None:
            output_string += f'{current.value} -> '
            current = current.next
        else:
            output_string += 'NULL'
        return output_string

    def append(self, end_value):
            new_end_node = Node(end_value)
            current = self.head
            while current:
                if current.next == None:
                    current.next = new_end_node
                    break
                current = current.next


    def insert_before(self, search_value, new_value):
        #if the old value is == the head value
        if self.head.value == search_value:
        #make a new node using this new value
            node = Node(new_value)
        #set that new value next to be the current as the head
            node.next = self.head
        #set the current node as the new head
            self.head = node
        else:
            current = self.head
            #while the next node is not empty
            while current.next != None:
                #if the next node's value is the old value
                if current.next.value == search_value:
                    #hold that next node in temp
                    temp = current.next
                    #droppin in the new node followed by the temp which is the previous current.next
                    current.next = Node(new_value, temp)
                    break
                current = current.next

    def insert_after (self, value, new_value):
        #if the current node is the head
        current = self.head
        #while the current is not the last one
        while current != None:
            if current.value == value:
                temp = current.next
                current.next = Node(new_value, temp)
                break
            current = current.next

    def kth_from_end (self,k=12):
        node_count = 0
        current = self.head
        print (f'this is node_count: {node_count}')

        # count the number of nodes in list
        # while current:
        #     current = current.next
        #     node_count += 1

        # if node_count > k:
        #     print (f'k is out of bounds')
        # # elif:
        # #     current = self.head
        # #     for i in range(node_count - k):
        # #         current = current.next
        # return print (f'this is the return')
        # current.value


        # return follow.value
if __name__=="__main__":
    ll = LinkedList()
    ll.insert()
    ll.insert(2)
    ll.insert(5)
    ll.insert(7)
    ll.insert(6)
    ll.insert(3)
    # print(ll.includes(35))
    # ll.__str__()
    ll.to_string()
    ll.kth_from_end()
    # print(f'this is to_string:{ll.to_string()}')
    print (f'this is LL: {LinkedList()}')
