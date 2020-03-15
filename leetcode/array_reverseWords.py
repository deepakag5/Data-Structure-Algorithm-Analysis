# Time: O(N)
# Space: O(1)

def reverseWords(s):
    def reverseString(string):
        left, right = 0, len(string) - 1
        while left < right:
            string[left], string[right] = string[right], string[left]
            left, right = left + 1, right - 1

        return "".join(string)

    return " ".join([reverseString(list(st)) for st in s.split()])

    ## we can even do below
#   return " ".join([st[::-1] for st in s.split()])
