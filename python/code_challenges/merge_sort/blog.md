# Merge Sort

## Pseudo Code
    ALGORITHM Mergesort(arr)
        DECLARE n <-- arr.length

        if n > 1
        DECLARE mid <-- n/2
        DECLARE left <-- arr[0...mid]
        DECLARE right <-- arr[mid...n]
        // sort the left side
        Mergesort(left)
        // sort the right side
        Mergesort(right)
        // merge the sorted left and right sides together
        Merge(left, right, arr)

    ALGORITHM Merge(left, right, arr)
        DECLARE i <-- 0
        DECLARE j <-- 0
        DECLARE k <-- 0

        while i < left.length && j < right.length
            if left[i] <= right[j]
                arr[k] <-- left[i]
                i <-- i + 1
            else
                arr[k] <-- right[j]
                j <-- j + 1

            k <-- k + 1

        if i = left.length
        set remaining entries in arr to remaining values in right
        else
        set remaining entries in arr to remaining values in left

## How it works:

Merge sort uses the technique to breakdown a list into several smaller list by dividing the input into a left and right half. Once the list has been split down as far as it can, it the compares the elements in the halves to sort them into order.

## Example:

Given this list:
[8,4,23,42,16,15]

* We split this list into a left and right half:
Left [8,4,23]   ||    Right [42,16,15]

* Lets look at the Right side and split again
    Note: this will also happen for the left side as well

    Split_left [42,16]   ||   Split_right [15]
        Note: since split_right [15]only has 1 element it is done splitting

    We will split_left again:
        split_again_left [42]   ||  split_right [15]  split_again_right [16]

*Now that we have both sides down to 1 element (aka no more splits able to be made) we can start comparing the values of each item in the list for sorting.

    At the top most level of the right side of the list we have left -> [42] [16]  right-> [15]

    *Compare right and left
        15<42
        [15,42]

        15<16
        Final Right side sort: [15,16,42]

*Repeat the same process for the left side:
 Left [8,4,23]
    Split_left [8,4]   ||   Split_right [23]
        Note: [23] is done splitting

 We will split_left again:
        split_again_left [8]   ||  split_right [23]  split_again_right [4]
    top most level of the right side of the list we have left -> [8] [4]  right-> [23]
    *Compare right and left
        23>8
        [8,23]
        23>4
        Final Right side sort: [4,8,23]

*Each ise has been sorted both right and left:
    right -> [4,8,23]
    left ->  [15,16,42]

*Next the left and right sides are compared by each element:
4 < 15
[4]
8 < 16
[4,8]
8 < 15
[4,8,15]
15 < 16
[4,8,15,16]
16 < 23
[4,8,15,16,23]
23 < 42
[4,8,15,16,23,42]

Final Result:
[4,8,15,16,23,42]
