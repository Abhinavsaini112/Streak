def MergeStringsAlternately(word1,word2):
    i = 0
    result = []
    while i < len(word1) or i < len(word2):
        if i < len(word1):
            result.append(word1[i])
        if i < len(word2):
            result.append(word2[i])
        i += 1

    return "".join(result)


word1 = 'abc'
word2 = 'def'
result = MergeStringsAlternately(word1,word2)
print(result)

 
'''Time Complexity is O(n+m) 
 Space Complexity is O(n+m) 
 where n and m are the length of the string.'''

"Pattern you're learning: this is an example of two-pointer/index traversal + output construction."
