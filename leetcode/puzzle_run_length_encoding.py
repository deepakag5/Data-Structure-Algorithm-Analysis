# O(N) as we are traversing the string
# O(N) to store the result list

def runLenEnc(s):
    res_list = []
    char, num = None, 0

    for i in range(len(s)):
        if i == 0:
            char, num = s[i], 1
        elif char != s[i]:
            res_list.append((char, num))
            char, num = s[i], 1
        else:
            num += 1

        if i == len(s) - 1:
            res_list.append((char, num))

    return res_list
