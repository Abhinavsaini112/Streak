def MergeStringsAlternately(word1,word2):
    i=0
    result=""
    while i<len(word1) or i<len(word2):
        if i<len(word1):
            result+=word1[i]
        if i<len(word2):
            result+=word2[i]
        i+=1
    return result


word1='abc'
word2='def'
result=MergeStringsAlternately(word1,word2)
print(result)

 
'''Time Complexity is O(n+m) and Space Complexity is O(n+m) where n and m are the length of the string.'''

