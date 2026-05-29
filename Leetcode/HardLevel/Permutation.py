def Permutation(nums):
    result = []
    used = [False]*len(nums)

    def backtrack(path):
        if len(path) == len(nums):
            result.append(path[:])
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            used[i] = True
            path.append(nums[i])
            backtrack(path)
            path.pop()
            used[i] = False
        
    backtrack([])
    return result

print(Permutation([1,2,3]))


def Permutation_K(nums,k):
    result = []
    used = [False]*len(nums)

    def backtracking(path):

        if len(path) == k:
            result.append(path[:])
            return
        
        for i in range(len(nums)):
            if used[i]:
                continue
            path.append(nums[i])
            used[i] = True
            backtracking(path)
            path.pop()
            used[i] = False
            
    
    backtracking([])
    return result

print(Permutation_K([1,2,3,4],3))

'''⏱ Time Complexity
Total permutations generated are:
P(n,k)= n!/(n-k)!
​	
 
For each permutation:
copying path[:] takes:
O(k)
So total time complexity:
O((n!/(n-k)!)⋅k)

Space Complexity is O(n). '''