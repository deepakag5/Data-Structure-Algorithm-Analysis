def isIsomorphic(s, t):
    """
    :param s: str
    :param t: str
    :return: boolean
    """
    d1, d2 = {}, {}

    for char in s:
        if char in d1:
            d1[char]+=1
        else:
            d1[char]=1

    for char in t:
        if char in d2:
            d2[char]+=1
        else:
            d2[char]=1

    return sorted(d1.values())==sorted(d2.values())


def isIsomorphic1(s, t):
    """
    :param s: str
    :param t: str
    :return: boolean
    """
    return len(set(zip(s,t))) == len(set(s)) == len(set(t))