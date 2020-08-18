# Time: O(n)
# Space: O(n)


def distributeCandies(candies, num_people):
    if num_people == 1:
        return candies

    idx = 0
    counter = 1
    result = [0] * num_people

    while candies > 0:
        if candies > counter:
            result[idx] += counter
        else:
            result[idx] += candies

        candies -= counter
        idx += 1
        counter += 1

        if idx == len(result):
            idx = 0

    return result
