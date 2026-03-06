def MaximumSubarray(li):
    currentsum = li[0]
    maxsum = li[0]
    for i in range(1,len(li)):
        currentsum = max(currentsum + li[i], li[i])
        maxsum = max(currentsum,maxsum)
    return maxsum

li = [-2,1,-3,4,-1,2,1,-5,4]
result = MaximumSubarray(li)
print(result)

'''Time Complexity is O(n) and Space Complexity is O(1)'''

def MaximumSubarray(li):
    currentsum = li[0]
    maxsum = li[0]
    start = 0 
    end = 0
    for i in range(1,len(li)):
        if li[i] > currentsum + li[i]:
            start = i
            currentsum = li[i]
        else: 
            currentsum = currentsum + li[i]
        if maxsum < currentsum:
            maxsum = currentsum 
            end = i
        maxsum = max(currentsum,maxsum)
    return maxsum , li[start:end+1]

li = [-2,1,-3,4,-1,2,1,-5,4]
result,subarray = MaximumSubarray(li)
print(result,subarray)

