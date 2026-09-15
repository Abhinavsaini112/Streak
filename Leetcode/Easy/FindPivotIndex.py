def PivotIndex(li):
    n = len(li)
    left_sum = [0] * n
    right_sum = [0] * n
    for i in range(1,n):
        left_sum[i] = left_sum[i - 1] + li[i - 1] 
    for i in range(n - 2,-1,-1):
        right_sum[i] = right_sum[i + 1] + li[i + 1]
    for i in range(n):
        if left_sum[i] == right_sum[i]:
            return i
    return -1

print(PivotIndex([1,7,3,6,5,6]))