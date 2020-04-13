def reverseStr(s):
    if len(s) == 0:
        return None

    if len(s) == 1:
        return s

    # as strings are immutable we need to convert it to list

    list_str = list(s)

    left, right = 0, len(list_str) - 1

    while left < right:
        # if not character then just move forward
        if not list_str[left].isalpha():
            left += 1
        elif not list_str[right].isalpha():
            right -= 1
        else:
            # if character then swap
            list_str[left], list_str[right] = list_str[right], list_str[left]
            left += 1
            right -= 1

    # return back as a string
    return ''.join(list_str)
