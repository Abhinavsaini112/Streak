def PrintPairDiffK(li,k):
    
    m = {}
    count = 0
    for i in li:
        if i + k in m:
            count += m[i+k]
        if  k != 0 and i - k in m:
            count += m[i-k]
        m[i] = m.get(i,0) + 1

    return count


li,k = [4,4,4,4],0
# li,k = [2,-1,3,5,6,0,-1,2,6],3
answer = PrintPairDiffK(li,k)
print(answer)


def PrintPairDiffK2(li,k):
    
    m = {}
    count = 0

    for i in li:
        m[i] = m.get(i,0) + 1

    if k == 0:
        for i in m:
            f = m[i]
            count += (f*(f-1))//2
    else:
        for i in m:
            if (i - k) in m:
                count += m[i-k] * m[i]
            if (i + k) in m:
                count += m[i+k] * m[i]
            m[i] = 0

    return count

li,k = [2,-1,3,5,6,0,-1,2,6],3
# li,k = [6,6,6,6],0

answer = PrintPairDiffK2(li,k)
print(answer)

