def MaxVowels(str,k):
    vowels = {'a','e','i','o','u'}
    current_vowels = 0
    n = len(str)
    for i in range(k):
        if str[i] in vowels:
            current_vowels += 1

    max_vowels = current_vowels

    for i in range(k,n):
        if str[i] in vowels:
            current_vowels += 1
        if str[i - k] in vowels:
            current_vowels -= 1
        if current_vowels > max_vowels:
            max_vowels = current_vowels

    return max_vowels

string = 'leetcode'
print(MaxVowels(string,3))