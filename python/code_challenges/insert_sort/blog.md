
 InsertionSort(int[] arr)

    //definitions:
    i = the index number for what we are iterating through
    j = iteration number - 1
    temp = the element in the array that needs to be sorted

    //this is controlling the pointer for the array
    FOR i = 1 to arr.length

    //store one less than the iteration number for for loop once the while loop is broken
      int j <-- i - 1

      //assign the current element to be sorted to the temp variable (after the while has been broken)
      int temp <-- arr[i]  temp = 4

    //while is check if the temp is < or > the the current j index
      WHILE j >= 0 AND temp < arr[j]

      //begin the sort by setting the next index number to the previous index value
        arr[j + 1] <-- arr[j]
            j = 0 + 1

        //placing that value in front of that index
        j <-- j - 1

    //once the loop is broken, set that next non sorted number to temp
      arr[j + 1] <-- temp

1st (For):
temp = 4
j = 0
[4,8,23,42,16,15]

2nd (For):
temp = 8
j = 1
[4,8,23,42,16,15]

3rd(for):
temp = 23
j = 2
[4,8,23,42,16,15]

4th(for):
temp = 42
j = 3
[4,8,23,42,16,15]

5th(for):
temp = 16
j = 4
    (while)
    16 < 42
    42 , 42
    [4,8,23,42,42,15]
    (while)
    [4,8,23,23,42,15]
    (while)
    [4,8,16,23,42,15]
