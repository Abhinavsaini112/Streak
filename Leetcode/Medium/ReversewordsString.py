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
