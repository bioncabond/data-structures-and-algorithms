
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


    def insert(self, value):
        node = Node(value)
        if self.head != None:
            node.next = self.head
        self.head = node

    def includes(self,value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def to_string(self):
        current=self.head
        string = ''

        while current:
            string += 'NULL'
        else:
            string += f'{ {current.value} } -> '
            current = current.next
        print(string)

if __name__=="__main__":
    ll = LinkedList()
    ll.insert(2)
    ll.insert(5)
    ll.insert(7)
    ll.insert(6)
    ll.insert(3)
    # ll.__str__()
    ll.to_string()


