def placeflowers(flowerbed, n):
    if n>=len(flowerbed):
        return False

    i, count = 0, 0

    initial_pos = 0
    final_pos = len(flowerbed) - 1


    while i<len(flowerbed):
        if flowerbed[i]==0 and (i==initial_pos or flowerbed[i-1]==0) and (i==final_pos or flowerbed[i+1]==0):
            flowerbed[i]=1
            count+=1
        i+=1

    return count>=n


