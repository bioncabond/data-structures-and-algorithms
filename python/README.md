# MultiBracket Validation 

- Write a function called validate_brackets that takes in a string and returns a true or false whether or not the brackets in the string are balanced.
 
 
![Whiteboard]! (https://user-images.githubusercontent.com/88898665/150918596-21cf21af-9286-4e20-9433-c0e23f413321.png)


Approach & Efficiency

Write a function that takes in one string as imput
    Create 3 list:
    Open Tags =  [,{,(
    Closing Tags = ],},)
    Validate = empty list
Iterate through the string and compare indexes:
    If in open tags, push the index into the the empty list
    If in the closed tags, check to see if the index of the bracket to the last element in the empty list
    if true then pop from the empty list
    if false, return false
Once the loop if finished, check to see if there is anything in the empty list we made.
    If empty return True
    If not empty; return Fals

Solution
 
Run test in test_validate.py    


# Animal Shelter
- Create a class called AnimalShelter which holds only dogs and cats.
The shelter operates using a first-in, first-out approach.
    Implement the following methods:
    enqueue
        Arguments: animal
        animal can be either a dog or a cat object.
    dequeue
        Arguments: pref
        pref can be either "dog" or "cat"
Return: either a dog or a cat, based on preference.
If pref is not "dog" or "cat" then return null.

## Whiteboard Process

![Whiteboard]!(https://user-images.githubusercontent.com/88898665/151455117-24470c69-2684-4175-a1d0-c12ee734fdbe.png)


## Approach & Efficiency
-Create an Animal_shelter Class 
-Create a Stack and Queue to manage animals entering the shelter 
-Create an Is_empty funtion 
-Enqueue: 
    -Take in animal type 
    -Create node to hold the animal type 
    -If empty:
        -Set the front ad rear to the Node
     Else: 
        -set the queue's rear's next to node 
        -set the queue's rear to the node 
     Increment size +1 
-Dequeue: 
    -Take in the prefered animal 
    -See if the preferred animal is the value of what is in the front of the queue. 
        - If they are eual set that animal type as the front value 
    -If its not store that front value in a variable
    -Push that value into the stack 
    -Point set the next node to the front. 
    -If there is noting at thte top of the stack: 
        -store the front of the queue 
        -pop that last value off the stack and store it as the front 
        -point the next node after the front to the temp. 
    Decrease size -1 
    return the animal_type


# pseudo queue
Partner(s) for this code challenge josh H. 

Create a new class called pseudo queue
Use the enqueue and dequeue methods to push values from one stack to a second stack. Use stacks to manage the queue.  

![Whiteboard]! (https://user-images.githubusercontent.com/88898665/151452135-acb00093-62f3-438f-b20d-17ed0301880f.png)

#Approach & Efficiency
-Create a class named Psuedo_queue 
-Initialize: 
    Stack1 & Stack2
    Len counter = 0
-Create enqueue function
    If Stack 2 is empty push in arugument
    Pop off all vallues in Stack 1
    Push Stack1 values into Stack 2
    Pop off values in Stack 2 to form queue with new value
    Increment length +1
-Create dequeue function
    decrement length -1
    return last popped value from stack 2



# array_binary_search

My Partner for this code challenge was Ian Cargill. (A new class partner list was sent out after Ian and I started working. Taylor was to work with Victor.)

# Use Binary Search To Find A Value In An Array

Take in an 2 parameters: an assorted array and a search key using binary search. Find the midpoint of that array and compare the parameters to the edges of that array (low and high), if in between the edges return the midpoint. Repeat this until the search key is found. Return the index of this search key or a -1 if not found.

## Whiteboard Process

![Whiteboard](binarywhiteboard.png)

## Approach & Efficiency

-Define the Low
-Define the High
-Define the midpoint
-Check the search key value at the midpoint
-If not the search key, find the new low and high
-Recheck the search key value at the new midpoint
-Repeat until midpoint = search key

# Code Challenge 2 - array_insert_shift

# Insert to Middle of an Array

-Insert a value at the midpoint of the array.
-Return the modified array with the value added.

## Whiteboard Process

![Whiteboard](arraywhiteboard.png)

## Approach & Efficiency

- Create an array that holds and acccepts values
- Find the midpoint of the array/list
- Insert the new value in at the mid point
- Append the first half of the array elements + the value + the end/second half of the array elements
  -Return the modified string.

#Solution:
list = [2,4,6,-8]
value = n
def insert_shift_array:
mid_point = len(list)//2
list = list[0:mid_point] + n + [mid_point:]
print(list)

---------------------------------------------------------------------------------------------------------

# Code Challenge 01 - Reverse Array
Challenge:
Reverse an Array
Write a function called reverseArray which takes an array as an argument and will turns an array with elements in the reverse order.

Whiteboard Process
Whiteboard

Approach & Efficiency
Algorithm: -Write a function that takes in an array -Return an array of the elements reversed

Solution
def reverseArray(): i = len(numList) - 1 while i >= 0 : print(numList[i]) i -= 1



# Data Structures and Algorithms

## Language: `Python`

### Folder and Challenge Setup

Each type of code challenge has slightly different instructions. Please refer to the notes and examples below for instructions for each DS&A assignment type.

### Data Structure: New Implementation

- Create a new folder under the `python` level, with the name of the data structure and complete your implementation there
  - i.e. `linked_list`
- Implementation (the data structure "class")
  - The implementation of the data structure should match package name
    - i.e. `linked_list/linked_list.py`
  - Follow Python [naming conventions](https://www.python.org/dev/peps/pep-0008/#naming-conventions)

    ```python
    class LinkedList:
      def __init__(self):
        # ... initialization code

      def method_name(self):
        # method body
    ```

- Tests
  - Within folder `tests` create a test file called `test_[data_structure].py`
    - i.e. `tests/test_linked_list.py`
    - Your tests will then need to require the data structure you're testing
      - i.e. `from linked_list.linked_list import LinkedList`

### Data Structure: Extending an implementation

- Work within the existing data structure implementation
- Create a new method within the class that solves the code challenge
  - Remember, you'll have access to `self` within your class methods
- Tests
  - You will have folder named `tests` and within it, a test file called `test_[data_structure].py`
    - i.e. `tests/test_linked_list.py`
    - Add to the tests written for this data structure to cover your new method(s)

### Code Challenge / Algorithm

Code challenges should be completed within a folder named `code_challenges` under the `python` level

- Daily Setup:
  - Create a new folder under the `python` level, with the name of the code challenge
    - Each code challenge assignment identifies the branch name to use, for example 'find-maximum-value'
    - For clarity, create your folder with the same name, ensuring that it's `snake_cased`
    - i.e. For a challenge named 'find_maximum_value', create the folder:`code_challenges/find_maximum_value`
  - Code Challenge Implementation
    - Each code challenge requires a function be written, for example "find maximum value"
    - Name the actual challenge file with the name of the challenge, in `snake_case`
      - i.e. `find_maximum_value.py`
    - Reminder: Your challenge file will then need to require the data structure you're using to implement
      - i.e. `from linked_list.linked_list import LinkedList`
    - Your challenge function name is up to you, but name something sensible that communicates the function's purpose. Obvious is better than clever
      - i.e. `find_maximum_value(linked_list)`
  - Tests
    - Ensure there is a `tests` folder at the root of project.
      - i.e. a sibling of this document.
    - within it, a test file called `test_[challenge].py`
      - i.e. `tests/find_maximum_value.py`
      - Your test file would require the challenge file found in the directory above, which has your exported function
        - i.e. `from code_challenges.find_maximum_value import find_maximum_value`

## Running Tests

If you setup your folders according to the above guidelines, running tests becomes a matter of deciding which tests you want to execute.  Jest does a good job at finding the test files that match what you specify in the test command

From the root of the `data-structures-and-algorithms/python` folder, execute the following commands:

- **Run every possible test** - `pytest`
- **Run filtered tests** - `pytest -k some_filter_text`
- **Run in watch mode** - `ptw` or `pytest-watch`
