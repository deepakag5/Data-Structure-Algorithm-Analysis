def factorCombIterative(num):
    stack, combinations = [(num, 2, [])], []
    while stack:
        n, i, comb = stack.pop()
        while i * i <= n:
            if n % i == 0:
                combinations.append((comb + [i, n/i]))
                stack.append((n/i, i, comb+[i]))
            i += 1
    return combinations