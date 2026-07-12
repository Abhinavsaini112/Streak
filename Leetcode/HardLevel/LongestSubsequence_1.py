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