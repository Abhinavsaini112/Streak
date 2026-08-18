def MaxConsOnes(li,k):
    left = 0
    n = len(li)
    max_length = 0
    countzeroes = 0 
    for right in range(n):
        if li[right] == 0:
            countzeroes += 1
        while countzeroes > k:
            if li[left] == 0:
                countzeroes -= 1
            left += 1

        currentwindowsize = right - left + 1
        max_length = max(max_length, currentwindowsize)

    return max_length

li = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
print(MaxConsOnes(li,3))
