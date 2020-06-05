def factorCombIterative(num):
    if num==0 or num==1:
        return []

    stack, combinations = [(num, 2, [])], []

    while stack:
        n, i, comb =  stack.pop()

        while i*i<=n:
            if n%i == 0:
                combinations.append(comb + [i, n / i])
                stack.append((n/i, i, comb+[i]))

            i+=1

    return combinations



def factorCombRecursive(num):
    def factor_rec(n, i, comb, combinations):
        while i*i<=n:
            if n%i == 0:
                combinations.append(comb + [i, n / i])
                factor_rec(n/i, i, comb+[i], combinations)

            i+=1

        return combinations

    return factor_rec(num, 2, [], [])