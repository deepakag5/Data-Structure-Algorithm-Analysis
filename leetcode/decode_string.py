def decodeString(s):
    """
    :type s: str
    :rtype: str
    """

    if not s:
        return ""

    # create two stacks
    # one for num and another for char
    nums, char = [], []
    i = 0
    length = len(s)

    # loop over the length of string
    while i < length:
        # if the char in string is a number
        if s[i].isdigit():
            # unit placeholder
            num = 0
            while i < length and s[i].isdigit():
                # if the number is two digit then
                # number at tenth place should be multiplied by 10
                num = 10 * num + int(s[i])
                i += 1
            # add the num to stack
            nums.append(num)
        # if the char is an open bracket or alpha
        # keep adding it to stack
        elif s[i] == "[" or s[i].isalpha():
            char.append(s[i])
            i += 1
        # if there are not more digits or char
        # which means a closing bracket has been hit
        else:
            # pop out character and append to tmp
            char1 = char.pop()
            tmp = []
            while char1 != "[":
                tmp.append(char1)
                char1 = char.pop()
            # pop out num as well and repeat char that many times
            num = nums.pop()
            # remember as we are adding items to stack (LIFO)
            # we need to reverse string which are in tmp
            new_char = num * "".join(tmp[::-1])
            char.append(new_char)
            i += 1
    return "".join(char)


print(decodeString("3[a]2[bc]"))
