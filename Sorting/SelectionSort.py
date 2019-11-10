
def selection_sort(arr):
    for i in range(len(arr)):
        least = i

        # if the current element is less the element at least index then reassign the least
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[least]:
                least = j
        # swap the least with the element at earlier index
        swap(arr, least, i)


def swap(arr, x, y):
    # swap the elements
    temp = arr[x]
    arr[x] = arr[y]
    arr[y] = temp


arr = [3, 2, 5, 6, 8, 1]

# sort the array
selection_sort(arr)

print(arr)
