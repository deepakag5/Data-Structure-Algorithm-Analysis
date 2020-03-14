def fizzBuzz(n):
    ans = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            ans.append("FizzBuzz")
        elif i % 3 == 0:
            ans.append("Fizz")
        elif i % 5 == 0:
            ans.append("Buzz")
        else:
            ans.append(str(i))
    return ans


def fizzBuzz_Conditions(n):
    ans = []

    for i in range(1, n + 1):
        div_by_3 = (i % 3 == 0)
        div_by_5 = (i % 5 == 0)

        num_str = ""

        if div_by_3:
            num_str += "Fizz"
        if div_by_5:
            num_str += "Buzz"
        if not num_str:
            num_str += str(i)

        ans.append(num_str)

    return ans


def fizzBuzz_HashTable(n):
    hash_table = {3: "Fizz", 5: "Buzz"}
    ans = []

    for i in range(1, n + 1):
        num_str = ""

        for key in hash_table.keys():
            if i % key == 0:
                num_str += hash_table[key]

        if not num_str:
            num_str += str(i)

        ans.append(num_str)

    return ans
