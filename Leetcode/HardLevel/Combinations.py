def combinations(nums,k):
    result = []

    def backtracking(start,path):
        if len(path) == k:
            result.append(path[:])
            return 
        
        for i in range(start , len(nums)):
            path.append(nums[i])
            backtracking(i+1,path)
            path.pop()

    backtracking(0 , [])
    return result

print(combinations([1,2,3,4],2))
