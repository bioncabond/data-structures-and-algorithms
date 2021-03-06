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
        if self.head is None:
            self.head = new_end_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_end_node


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

    def kth_from_end (self,k):
        node_count = 0
        current = self.head
        # print (f'this is node_count: {node_count}')

        # count the number of nodes in list
        while current:
            current = current.next
            node_count += 1
        print (f'this is loops node_count: {node_count}')
        if k > node_count:
            return ("k is out of bounds")
        #moving the pointer back to the front of the list; no list modification
        elif k < 0:
            return("k is negative")
        elif self.head.next is None:
            return current.value

        current = self.head
        for i in range(1,node_count - k):
            current = current.next
        return current.value

    def zip_list(self,list_1,list_2):
        ll = LinkedList()
        list_1_curr = list_1.head
        list_2_curr = list_2.head
        print(f"list_1_current: {list_1_curr.value}")

        while list_1_curr != None or list_2_curr != None:
            if list_1_curr != None and list_2_curr != None:
                ll.append(list_1_curr.value)
                ll.append(list_2_curr.value)
                # print(f"while equal: {list_1_curr.value} {list_2_curr.value}")
                list_1_curr = list_1_curr.next
                list_2_curr = list_2_curr.next
                # print(f"ll2chains: {ll.to_string()}")
            elif list_1_curr == None:
                ll.append(list_2_curr.value)
                list_2_curr == list_2_curr.next
            elif list_2_curr == None:
                ll.append(list_1_curr.value)
                list_1_curr == list_1_curr.next
        print(ll.to_string())
        return ll

if __name__=="__main__":
    ll = LinkedList()
    ll1=LinkedList()
    ll2=LinkedList()
    ll1.insert(3)
    ll1.insert(8)
    ll1.insert(5)
    ll2.insert('a')
    ll2.insert('b')
    ll2.insert('c')
    expected = ll.zip_list(ll1,ll2)
    print (f'this is LL: {expected.to_string()}')


    # print(f'this is to_string:{ll.to_string()}')
