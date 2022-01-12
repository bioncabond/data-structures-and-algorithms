# Stacks and Queues

Implement and test both stacks and queues.

## Challenge

Create a Stack Class and the following methods to maneuver the stack:
-push: add to
-pop: take away from
-peek: see what is on top
-Is_Empty: is the stack empty? Return True

Create a Queue Class and the following methods to maneuver the stack:
-enqueue: add to
-dequeue: take away
-peek: see what is at the front
-Is_Empty: is the queue empty? Return True

Besure to raise execptions for peek and pop for stacks if the stack is empty.

Besure to raise execptions for peek and dequeue for queue if the queue is empty.

## Approach & Efficiency

Write the methods to handle the above mentioned methods.

## API

No APIs needed.

# Zip List

Worked with game of greed partner (Josh H.) on code and whiteboard.

# Challenge Summary

Zip 2 linked list into one so that the nodes alternate between the two list.

## Whiteboard Process

![Whiteboard](/python/linked_list_II/linked_list/Code_Challenge_8.jpg)

## Approach & Efficiency

--Write a function called zip list
--Take in a 2 list as arguments (a,b)
--Set the head of both list
--Create a loop to iterate through each list
--If the a.next node is truthy grab b.next node to new list
--If the b.next node is truthy grab a.next to new list
return the merged list with alternating nodes

## Solution

def zip_list(list_1,list_2):
list_1_current = list_1_head
list_2_current = list_2_head

while list_1 current != None and list_2 current != None:
list_1.next = list_1 current.next
list_2.next = list_2 current.next

     list_1_current.next = list_2_next
     list_2_current.next= list_1_next

     list_1_current = list1_next
     list_2_current = list2_next

test = LinkedList()
zipped_list = test.zip_list(list_1, list_2)
print(zipped_list)

# Singly Linked List

# Challenge Summary

k-th value from the end of a linked list

## Whiteboard Process

![Whiteboard](/python/linked_list_II/linked_list/Code_Challenge_7.jpg)

## Approach & Efficiency

--Write method for linked list
--take in a number as an argument
--count the number of k from the tail of the list
--return the node's value that is k places from the tail of the linked list

## Solution

def kth_from_end(self, k):
leader = self.head
follower = None
tail_count = 0

     while leader:
          leader = leader.next

          if follower:
             follower = follower.next
          elif tail_count = k
             follower = self.head
           else:
               tail_count += 1
       if not follower:
             raise TargetError("k is out of bounds")

return follower.value

## Challenge

Insert the following methods to traverse and move the positions of nodes:
Lab 05:
-Insert
-Inclueds
-To String

## Lab 06:

-Append
-Insert Before
-Insert After

![Whiteboard](/python/linked_list_II/linked_list/Code_Challenge_06.jpg)

## Approach & Efficiency

-Create the LinkedList Class
-Create the Node Class

## Create append method

-Find the tail of the Linked List (current.next = Null)
-Add node after the tail position in the Linked List

## Create insert before method

-Within the Linked List class:
-Identify the specified value
-Insert the new value before the specified value

## Create insert after method

-Within the Linked List class:
-Identify the specified value
-Insert the new value after the specified value

## API

No APIs were used.
