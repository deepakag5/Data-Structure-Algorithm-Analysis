# Time : O(4^n/ sqrt(n))
# Space : O(4^n/ sqrt(n))


def generate_parenthesis(n):
    if n == 0:
        return []

    result = []

    def backtrack(s='', left=0, right=0):
        # we need to have a closing bracket for each opening bracket
        # so a pair hence 2*n
        if len(s) == 2 * n:
            result.append(s)
            return
        # we need open brackets at most the length of n
        if left < n:
            backtrack(s + '(', left + 1, right)
        # we will place a closing bracket only after we have an open bracket
        if right < left:
            backtrack(s + ')', left, right + 1)

    backtrack()
    return result
