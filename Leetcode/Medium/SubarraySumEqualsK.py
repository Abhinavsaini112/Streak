# Solved using Prefix Sum and Sliding Window .
def SubarraySumEqualsK(li,k):
    n = len(li)
    count = 0
    prefixsum = 0
    hashmap = {0 : 1}
    for i in range(n):
        prefixsum += li[i]
        if prefixsum - k in hashmap:
            count += hashmap[prefixsum-k] 
        
        hashmap[prefixsum] = hashmap.get(prefixsum,0) + 1
    return count
    
print(SubarraySumEqualsK([1,1,1], 2))   # 2
print(SubarraySumEqualsK([2,1,1], 2))   # 2
print(SubarraySumEqualsK([1,-1,1], 1))  # 3
