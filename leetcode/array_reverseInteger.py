# Time: O(N)
# Space: O(1)

def reverseInt(x):
    if str(x).strip() == '':
        return ''

    if x == 0:
        return 0
    else:
        # convert to list of characters to reverse
        ch_x = list(str(x))

        # we can use ch_x = ch_x[::-1] as well to reverse

        left, right = 0, len(ch_x) - 1

        while left < right:
            ch_x[left], ch_x[right] = ch_x[right], ch_x[left]
            left, right = left + 1, right - 1

        # convert list to string
        ch_x = "".join(ch_x)
        # remove the leading zeros after reversal
        ch_x = ch_x.lstrip('0')
        # remove the trailing negative sign after reversal
        ch_x = ch_x.rstrip('-')

        if x < 0:
            # add leading negative sign for negative number
            ch_x = '-' + ch_x
            if int(ch_x) < (-2 ** 31):
                return 0
            else:
                return int(ch_x)
        else:
            if int(ch_x) > (2 ** 31):
                return 0
            else:
                return int(ch_x)
