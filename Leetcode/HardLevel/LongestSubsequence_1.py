def Lcs_recursive(str1, str2, i = 0, j = 0):
    # Base case : if we reach the end of either string
    if i == len(str1) or j == len(str2):
        return 0
    
    # If characters match
    if str1[i] == str2[j]:
        return 1 + Lcs_recursive(str1, str2, i + 1, j + 1)
    
    # If they don't match, take the maximum of two possibilities
    return max( Lcs_recursive(str1, str2, i + 1, j),
               Lcs_recursive(str1, str2, i, j + 1))
   
str1 = 'AGGTAB'
str2 = "GXTXAYB"
print(Lcs_recursive(str1, str2))


'''Time Complexity : O(2^m+n)

1. How recursion works here
At every step (i,j):
If str1[i] == str2[j] we got one recursive call : dp(i+1,j+1).
If str1[i] != str2[j] we branch into two recursive calls:
dp(i + 1, j)
dp(i, j + 1)
so , mismatches cause a branching factor of 2 .

2. Worst case
In the worst case (when almost no characters match), every recursive call branches 
into two new calls, until one of the strings runs out.
The maximun recursion depth is about m + n (since each step increases either i or j).
The total number of nodes is this recursion tree is exponential in m + n. '''