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
