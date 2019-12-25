def minWindow(s,t):
    # placeholders
    # dict to hold count
    # windows count
    # left and right pointers
    # formed (freq of characters)
    # ans

    # base case
    if not t or not s:
        return None

    dict_t = {}

    for char in t:
        if char in dict_t:
            dict_t[char]+=1
        else:
            dict_t[char]=1

    windows_count = {}

    l, r = 0, 0

    req_length_t = len(t)

    freq_char_t = 0

    ans = float('inf'), None, None

    while r<len(s):
        char = s[r]

        windows_count[char] = windows_count.get(char, 0)+1

        if char in dict_t and windows_count[char] == dict_t[char]:
            freq_char_t+=1

        while l<=r and freq_char_t == req_length_t:
            char = s[l]

            if r-l+1 < ans[0]:
                ans = (r-l+1, l, r)

            windows_count[char] -= 1

            if char in dict_t and windows_count[char] < dict_t[char]:
                freq_char_t-=1

            l+=1

        r+=1

    return "" if ans[0] == float('inf') else s[ans[1]:ans[2]+1]


