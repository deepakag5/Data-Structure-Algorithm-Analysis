# Time: O(n)
# Space: O(n)

# Two Parse
def minRemoveToMakeValid(s):
    if len(s) == 0:
        return ""

    def delete_closing_brackets(s, open_b, close_b):
        sb = []
        balance = 0

        for char in s:
            # increment balance if opening bracket is encountered
            if char == open_b:
                balance += 1
            # if the balance is zero means no corresponding
            # open bracket - skip that ")" by doing continue
            # else decrease the balance
            if char == close_b:
                if balance == 0:
                    continue
                balance -= 1
            sb.append(char)

        return "".join(sb)

    s = delete_closing_brackets(s, "(", ")")
    s = delete_closing_brackets(s[::-1], ")", "(")

    return s[::-1]
