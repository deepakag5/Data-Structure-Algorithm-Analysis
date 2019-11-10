# brute force

def bubble_sort(arr):
    # traverse the array for all elements
    for i in range(len(arr)):
        # check if the last element is smaller than the previous one
        # if yes swap
        for j in range(len(arr) - 1, i, -1):
            if arr[j] < arr[j - 1]:
                swap(arr, j, j - 1)


def swap(arr, x, y):
    temp = arr[x]
    arr[x] = arr[y]
    arr[y] = temp


arr = [2, 1, 5, 8, 7]

bubble_sort(arr)

print(arr)


# improved version

def improved_bubble_sort(arr):
    for i in range(len(arr)):
        # create a flag to keep track if inner loop swaps any element
        swapped = 0

        for j in range(len(arr) - 1, i, -1):
            if arr[j] < arr[j - 1]:
                swap(arr, j, j - 1)
                swapped = 1
        # if no element is swapped by inner loop array is already sorted - no need to run outer loop break
        if swapped == 0:
            break


arr = [2, 1, 5, 8, 7]

improved_bubble_sort(arr)

print(arr)
