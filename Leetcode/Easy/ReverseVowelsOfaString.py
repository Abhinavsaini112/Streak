# Traverse the string
# Collect all the vowels in a list
# Reverse the vowel list
# Traverse the string again
# Replace vowels from the reversed list

# How can you determine if a character is a vowel?
# How can you reverse characters in a string?
# How can you replace characters in a string?

# Brute Force Method

def ReverseVowels(s):
    i = 0
    vowels_list = []
    result = []
    vowels = set('aeiouAEIOU')
    for ch in s:
        if ch in vowels:
            vowels_list.append(ch)
    vowels_list.reverse()
    for ch in s:
        if ch in vowels:
            result.append(vowels_list[i])
            i += 1
        else:
            result.append(ch)
    return ''.join(result)
# Time Complexity is O(n)
# Space Complexity is O(n)

print(ReverseVowels("hello"))        
print(ReverseVowels("leetcode"))     
print(ReverseVowels("Abhinav")) 

# Optimized Approach

def ReverseVowels(s):
    vowels = set('aeiouAEIOU')
    arr = list(s)
    left = 0
    right = len(arr) - 1

    while left < right :
        while arr[left] not in vowels:
            left += 1
            if left > right:
                break
        while arr[right] not in vowels:
            right -= 1
            if left > right:
                break
        if left < right:
            arr[left],arr[right] = arr[right],arr[left]
        left += 1
        right -= 1
    
    return "".join(arr)

# Time Complexity O(n)
# Space Complexity O(n)

print(ReverseVowels("hello"))        
print(ReverseVowels("leetcode"))     
print(ReverseVowels("Abhinav"))


