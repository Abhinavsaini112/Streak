def UniqueOccurrences(li):
    unique = {}
    for i in li:
        unique[i] = unique.get(i,0) + 1

    freq_values = unique.values()

    return len(set(freq_values)) == len(unique)

li = [1,2,2,1,3,1]
print(UniqueOccurrences(li))

from collections import Counter
def UniqueOccurrences(li):
    unique = Counter(li)

    freq_values = unique.values()

    return len(set(freq_values)) == len(unique)

li = [1,2,2,1,3,1,3]
print(UniqueOccurrences(li))

'''Time Complexity is O(n) and Space Complexity is O(n)'''