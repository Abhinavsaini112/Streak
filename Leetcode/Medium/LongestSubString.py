def lengthOfLongestSubstring( s: str) :
    left=0
    max_len=0
    start_index=0
    l=len(s)
    substring=set()
    for i in range(l):
        while s[i] in substring:
            substring.remove(s[left])
            left+=1
        substring.add(s[i])
        
        if (i - left + 1) > max_len:
            max_len = i - left + 1
            start_index = left  # update where longest substring starts

    longest_substring = s[start_index:start_index + max_len]
    return max_len, longest_substring




s='abcabcbb'
value,string=lengthOfLongestSubstring(s)
print(value,string)


