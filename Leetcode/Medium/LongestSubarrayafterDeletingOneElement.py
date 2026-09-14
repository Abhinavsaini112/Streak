def LongSubarray(li):
    left = 0
    counterzeroes = 0
    n = len(li)
    max_length = 0
    for right in range(n):
        if li[right] == 0:
            counterzeroes += 1
        while counterzeroes > 1:
            if li[left] == 0:
                counterzeroes -= 1
            left += 1
        current_length = right - left
        max_length = max(current_length,max_length)

    return max_length

li = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
print(LongSubarray(li))
            
