def romanToInt(s):
    values_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    total = 0
    i = 0

    while i < len(s):
        if i + 1 < len(s) and values_dict[s[i]] < values_dict[s[i + 1]]:
            # If the symbols are out of numeric order.
            # We subtract the value of i+1 and i to get their total value
            total += values_dict[s[i + 1]] - values_dict[s[i]]
            # jump two places as we are considering
            # both i and i+1 here
            i += 2
        else:
            total += values_dict[s[i]]
            i += 1

    return total
