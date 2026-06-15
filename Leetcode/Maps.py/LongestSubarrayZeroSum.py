def SumZero(li):
    m = {}
    sum = 0
    maxlength = 0
    for i in range(len(li)):
        sum += li[i]

        if sum == 0:
            maxlength = i + 1

        if sum in m:
            maxlength = max(maxlength, i - m[sum])
        else:
            m[sum] = i

    return maxlength


# li = [6,1,5,-8,-4,2]
li = [15,2,-2,-8,1,7,10,23]
print(SumZero(li))
