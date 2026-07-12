# Top Down Approach (DP)
def Lcs_recursive_Top(str1, str2):
    m, n = len(str1), len(str2)
    memo = [[-2] * n for _ in range(m)]
    
    def dp(i,j):
        # Base case : if we reach the end of either string
        if i == m or j == n:
            return 0
        if memo[i][j] != -2:
            return memo[i][j]
        
        # If characters match
        if str1[i] == str2[j]:
            memo[i][j] = 1 + dp(i + 1, j + 1)
        else:
            memo[i][j] = max(dp(i + 1, j), dp(i, j + 1))
        return memo[i][j]
    
    return dp(0,0)
        
str1 = 'AGGTAB'
str2 = "GXTXAYB"
print(Lcs_recursive_Top(str1, str2))

'''Time Complexity O(m * n)
At each state (i,j):
we do a constant amount of work:
Compare characters str1[i] and str2[j]
Possibly call dp(i + 1, j + 1) or dp(i , j + 1)/dp(i + 1, j).
But thanks to memoization , each (i,j) is solved only once.
After the first time, we just do a table lookup O(1).'''

'''Space Complexity O(m *   n)'''

# Bottom Up Approach (DP)
def Lcs_recursive_Bottom(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # fill the table row by row , top left to bottom right
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp [i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]
    
str1 = 'AGGTAB'
str2 = "GXTXAYB"
print(Lcs_recursive_Bottom(str1, str2))