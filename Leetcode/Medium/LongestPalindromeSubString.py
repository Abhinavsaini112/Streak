def longestPalindrome(s: str) -> str:
    long_sub=''
    len_sub=0
       
    for i in range(len(s)):
       # for odd center
        l,r=i,i
        while l>=0 and r<len(s) and s[l]==s[r]:
            if (r-l+1)>len_sub:
                len_sub=(r-l+1)
                long_sub=s[l:r+1]
            l-=1
            r+=1
        
        # for even center
        l,r=i,i+1
        while l>=0 and r<len(s) and s[l]==s[r]:
            if (r-l+1)>len_sub:
                len_sub=r-l+1
                long_sub=s[l:r+1]
            l-=1
            r+=1
    return long_sub

string='cbbd'
print(longestPalindrome(string))
        