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


def PivotIndex(li):
    n = len(li)
    total_sum = sum(li)
    left_sum = [0] * n
    if 0 == total_sum - 0 - li[0]:
        return 0
    for i in range(1,n):
        left_sum[i] = left_sum[i - 1] + li[i - 1]

        if left_sum[i] == total_sum - left_sum[i] - li[i]:
            return i
        # If we know the total sum
        # At any index i
        # Right sum = Total sum - Left sum - current element
    return -1

print(PivotIndex([1,7,3,6,5,6]))


def PivotIndex(li):
    n = len(li)
    total_sum = sum(li)
    left_sum = 0
    for i in range(n):
        x = li[i]
        right_sum = total_sum - left_sum - x
        if left_sum == right_sum:
            return i
        left_sum += x
    return -1

print(PivotIndex([1,7,3,6,5,6]))
    