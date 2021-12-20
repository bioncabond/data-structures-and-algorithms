
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

    @Error_Handler
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

if __name__=="__main__":
    ll = LinkedList()
    ll.insert(2)
    ll.insert(5)
    ll.insert(7)
    ll.insert(6)
    ll.insert(3)
    # print(ll.includes(35))
    # ll.__str__()
    ll.to_string()
    print(f'this is to_string:{ll.to_string()}')

    ll.insert()
