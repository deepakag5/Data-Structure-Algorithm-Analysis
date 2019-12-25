def minWindow(s,t):

    # base case
    if not t or not s:
        return ""

    dict_t = {}

    # get freq of characters in target string
    for char in t:
        if char in dict_t:
            dict_t[char]+=1
        else:
            dict_t[char]=1

    windows_count = {}

    req_len_t = len(t)

    completed_t = 0

    left, right = 0, 0

    ans = (float('inf'), None, None)

    while right<len(s):
        char = s[right]

        windows_count[char] = windows_count.get(char, 0) + 1
        if char in dict_t and windows_count[char] == dict_t[char]:
            completed_t+=1

        while left<=right  and completed_t == req_len_t:
            char = s[left]

            if right-left+1 < ans[0]:
                ans = (right-left+1, left, right)

            windows_count[char] = windows_count.get(char) - 1
            if char in dict_t and windows_count[char]<dict_t[char]:
                completed_t-=1

            left+=1

        right+=1


    return "" if ans[0] == float('inf') else s[ans[1]:ans[2]+1]




print(minWindow("ADOBECODEBANC","ABC"))



