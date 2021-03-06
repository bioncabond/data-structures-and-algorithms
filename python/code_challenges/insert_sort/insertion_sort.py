    # InsertionSort(int[] arr)

    #     FOR i = 1 to arr.length

    #     int j <-- i - 1
    #     int temp <-- arr[i]

    #     WHILE j >= 0 AND temp < arr[j]
    #         arr[j + 1] <-- arr[j]
    #         j <-- j - 1

    #     arr[j + 1] <-- temp

def insertion_sort(lst):
    for i in range(len(lst)):
        j = i - 1
        temp = lst[i]

        while j>=0 and temp < lst[j]:
            lst[j + 1] = lst[j]
            j = j - 1
        lst[j +1 ] = temp
    return lst

if __name__ == "__main__":
    test = [8,4,23,42,16,15]
    print(insertion_sort(test))
