def ReverseWordsString(s):
    words = s.split()
    words.reverse()
    return " ".join(words)


s = "The sky is blue"
result = ReverseWordsString(s)
print(result)