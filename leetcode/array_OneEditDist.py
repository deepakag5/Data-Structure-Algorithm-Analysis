# Time : O(N)
# Space : O(N)  --  because strings are immutable in Python and Java and to create substring costs O(N)space.

def OneEditDist(s, t):
    if (len(s) == 0 and len(t) > 1) or (len(s) == 1 and len(t) > 0):
        return False

    len_s, len_t = len(s), len(t)

    if len_s > len_t:
        return OneEditDist(t, s)

    if len_t > len_s + 1:
        return False

    for i in range(len_s):
        if s[i] != t[i]:
            if len_s == len_t:
                return s[i + 1:] == t[i + 1:]
            else:
                return s[i:] == t[i + 1:]

    return len_s + 1 == len_t
