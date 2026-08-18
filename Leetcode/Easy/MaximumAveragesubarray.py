# Sliding Window Approach

def MaximumAverageSum(li,k):
    current_sum = sum(li[:k])
    max_sum = current_sum
    n = len(li)
    for i in range(k,n):
        current_sum = current_sum - li[i - k] + li[i]
        if current_sum > max_sum:
            max_sum = current_sum

    return max_sum / k

li = [1,12,-5,-6,50,3]
print(MaximumAverageSum(li,4))
