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

    formed = len(t)

    ans = float('inf'), None, None


    while r<=len(s):
