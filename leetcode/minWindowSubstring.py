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

    # keep track of character and their freq
    windows_count = {}

    # for length of req str
    req_len_t = len(t)

    # for keeping track if length meets req length in t
    completed_t = 0

    # keep track of window
    left, right = 0, 0

    # hold the results
    ans = (float('inf'), None, None)

    while right<len(s):
        char = s[right]

        # we used get function so that if key is not present it
        # should not raise keyerror -- dict.get("key", default_value) instead of dict["key"]
        windows_count[char] = windows_count.get(char, 0) + 1

        # if the frequency of character in window is same as in dict then increment completed t
        if char in dict_t and windows_count[char] == dict_t[char]:
            completed_t+=1

        # contract the window
        while left<=right  and completed_t == req_len_t:
            char = s[left]

            if right-left+1 < ans[0]:
                ans = (right-left+1, left, right)

            # decrease the count in window and decrease completed t as character
            # at the position pointed by the `left` pointer is no longer a part of the window.
            windows_count[char] = windows_count.get(char) - 1
            if char in dict_t and windows_count[char]<dict_t[char]:
                completed_t-=1

            # keep moving forward with left pointer
            left+=1

        # keep moving forward with right pointer
        right+=1


    return "" if ans[0] == float('inf') else s[ans[1]:ans[2]+1]



def minWindowOptimized(s, t):

    if not t or not s:
        return ""

    dict_t = {}

    for char in t:
        if char in dict_t:
            dict_t[char]+=1
        else:
            dict_t[char]=1

    windows_count = {}

    left, right = 0, 0

    filtered_s = []

    for i, char in enumerate(s):
        if char in dict_t:
            filtered_s.append((i, char))

    req_len_t = len(t)

    completed_t = 0

    ans = float('inf'), None, None

    while right<len(filtered_s):
        char = filtered_s[right][1]

        windows_count[char] = windows_count.get(char, 0) + 1
        if windows_count[char] == dict_t[char]:
            completed_t+=1

        while left<=right and completed_t==req_len_t:
            char = filtered_s[left][1]

            end = filtered_s[right][0]
            start = filtered_s[left][0]

            if end-start+1<ans[0]:
                ans = (end-start+1, start, end)

            windows_count[char] -=1
            if windows_count[char]<dict_t[char]:
                completed_t-=1

            left+=1

        right+=1

    return "" if ans[0]==float('inf') else s[ans[1]:ans[2]+1]

