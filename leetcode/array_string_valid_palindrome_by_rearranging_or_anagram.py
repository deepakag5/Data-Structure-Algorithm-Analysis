# Time: O(N)
# Space: O(k)

def canmakePalindrome_from_rearrangement_or_anagram(s):
    # there are 256 chars in ASCII (0-255)
    count1 = [0] * 256

    # get the frequency of characters at their respective
    # ascii value index - for example ascii value of
    # 'a' is 97 which means at that index the frequency 'n' will be
    # updated if char a is present 'n' number of times in given str
    for char in s:
        count1[ord(char)] += 1

    num_odd = 0

    # if there are more than one character where the frequency is odd
    # we cannot make a palindrome from it !
    for i in range(256):
        if count1[i] % 2 != 0:
            num_odd += 1

        if num_odd > 1:
            return False

    return True
