def ValidParantheses(str):
    dict = {")":"(","]":"[","}":"{"}
    li = []
    for i in str:
        if i in '({[':
            li.append(i)
        elif i in ')}]':
            if not li or li[-1] != dict[i]:
                return False
            li.pop()
    return not li

str = '({[]})'

'''str = ')()' and '(((' -> edge cases'''

result = ValidParantheses(str)
print(result)

'''Time Complexity is O(n) and Space Complexity is O(n)'''