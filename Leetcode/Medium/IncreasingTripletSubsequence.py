# Brute force method
# Time Complexity is O(n*n*n)
def IncreasingTripletSubsequence(nums):
    n = len(nums)
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if nums[i] < nums[j] < nums[k]:
                    return True
    return False

# Approach to solve in O(n) time complexity
def IncreasingTripletSubsequence(nums):
    # first bar -> lowest jump height seen so far
    # second bar -> lowest jump height seen that is higher than a previous jump

    # If I can lower a bar , I will always do it.

    first = float('inf')
    second = float('inf')
    for jump in nums:
        if jump <= first:
            first = jump
        elif jump <= second:
            second = jump
        else:
            return True
    return False


print(IncreasingTripletSubsequence([1,2,3,4,5]))   # True
print(IncreasingTripletSubsequence([5,4,3,2,1]))   # False
print(IncreasingTripletSubsequence([2,1,5,0,4,6])) # True
print(IncreasingTripletSubsequence([1,1,1,1,1,1])) # False

