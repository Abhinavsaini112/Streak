def IsSubsequence(li,s):
    i = 0
    j = 0
    while i < len(li) and j < len(s):
        if li[i] == s[j]:
            j += 1
        i += 1
        
    return j == len(s)

li = 'ahbgdc'
subseq = 'agc'
print(IsSubsequence(li,subseq))

'''Time Complexity is O(n)
Space Complexity is O(1)'''