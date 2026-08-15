def KPair_Sum(li,k):
    dic = {}
    pair = 0
    for num in li:
        compliment = k - num
        if compliment in dic and dic[compliment] > 0:
            pair += 1
            dic[compliment] -= 1
        else:
            dic[num] = dic.get(num,0) + 1

    return pair

li = [4,1,3,2,1,2,3]
print(KPair_Sum(li,5))
'''Time Complexity is O(n) and Space Complexity is O(1)'''

def Pair_sum(li,k):
    li.sort()
    left = 0 
    right = len(li) - 1
    pair = 0
    while left < right:
        if li[left] + li[right] == k:
            pair += 1
            left += 1
            right -= 1
        elif li[left] + li[right] > k :
            right -= 1
        else:
            left += 1

    return pair

li = [4,1,3,2,1,2,3]
print(Pair_sum(li,5))