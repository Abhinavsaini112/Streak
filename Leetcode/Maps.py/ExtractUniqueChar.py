def UniqueChar(s):
    # unique = set()
    # new_s = ""
    # for i in s:
    #     if i not in unique:
    #         unique.add(i)
    #         new_s += i
    # return new_s

    '''creates a new string every time because strings are immutable in Python.
    If the string length is n, the overall complexity becomes:
    O(n²)'''

    seen = set()
    result = []

    for ch in s:
        if ch not in seen:
            seen.add(ch)
            result.append(ch)

    return "".join(result)

    # using dictionary
    # char_map = {}
    # new_s = []
    # for i in s :
    #     if i not in char_map:
    #         char_map[i] = True
    #         new_s.append(i)
    # return "".join(new_s)

s = UniqueChar('ababacd')
print(s)        