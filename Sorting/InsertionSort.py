def insertion_sort(arr):
    for i in range(1,len(arr)):
        # create a temp variable to store current value
        temp = arr[i]
        position = i

        # keep swapping the elements until the previous element is greater than the element at position
        while position > 0 and temp < arr[position - 1]:
            arr[position] = arr[position - 1]
            position -= 1

        arr[position] = temp


arr = [3, 1, 8, 6, 2]

insertion_sort(arr)

print(arr)
