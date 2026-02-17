def ReverseWordsString(s):
    words = s.split()
    words.reverse()
    return " ".join(words)


s = "The sky is blue"
result = ReverseWordsString(s)
print(result)


def ReverseWordsString(s):
    words = []
    n = len(s)
    i = 0 
    while i < n:
        while i < n and s[i] == ' ':
            i += 1
        if i < n:
            word_start = i
            while i < n and s[i] != " ":
                i += 1
            words.append(s[word_start: i])
    words.reverse()
    return ' '.join(words)

s = "The sky is blue"
result = ReverseWordsString(s)
print(result)

def RevereseWordsString(s):
    chars = list(s)
    n = len(s)
    
    def reverse(l,r):
        while l < r:
            chars[l], chars[r] =  chars[r], chars[l]
            l += 1 
            r -= 1
    # reverse the string
    reverse(0,n-1)
    write = 0 
    read = 0
    first_word = False
    while read < n:
        # skip spaces
        while read < n and chars[read] == ' ':
            read += 1
        if read == n:
            break
        # add space after every word apart from the first word
        if first_word:
            chars[write] = ' '
            write += 1
        first_word = True

        word_start = write

        while read < n and chars[read] != '':
            chars[write] = chars[read]
            write += 1
            read += 1
        reverse(word_start , write-1)
    return ''.join(chars[:write])

s = " The    sky   is blue   "
result = ReverseWordsString(s)
print(result)
