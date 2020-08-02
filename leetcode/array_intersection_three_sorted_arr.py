# Time: O(m) where m is the length of smallest arr
# Space: O(k) where k is the number of common elements


def arraysIntersection(arr1, arr2, arr3):
    if len(arr1) == 0 or len(arr2) == 0 or len(arr3) == 0:
        return []

    out_list = []

    i, j, k = 0, 0, 0

    while i < len(arr1) and j < len(arr2) and k < len(arr3):
        if arr1[i] == arr2[j] and arr2[j] == arr3[k]:
            out_list.append(arr1[i])
            i += 1
            j += 1
            k += 1
        elif arr1[i] < arr2[j] or arr1[i] < arr3[k]:
            i += 1
        elif arr2[j] < arr3[k] or arr2[j] < arr1[i]:
            j += 1
        elif arr3[k] < arr1[i] or arr3[k] < arr2[j]:
            k += 1
        else:
            i += 1
            j += 1
            k += 1

    return out_list


def arraysIntersection(arr1, arr2, arr3):
    return sorted(set(arr1) & set(arr2) & set(arr3))
