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

print(combinations([1,2,3,4],3))

'''Time Complexity

Let
n = len(nums)
k = size of each combination

The number of combinations is (nCk) = a

For every combination, copying path takes O(k) = b time. 

Time Complexity =O(a * b)'''

'''Space Complexity

Auxiliary space : is the extra or temporary memory space used by an algorithm during 
its execution to solve a problem. It excludes the memory required to store the 
original input data.

Input Space: The memory required to hold the initial data provided to the algorithm.

Space Complexity = Input Space + Auxiliary Space

Auxiliary Space
O(k)

Total Space (including output)
O(a * b)
	​

'''