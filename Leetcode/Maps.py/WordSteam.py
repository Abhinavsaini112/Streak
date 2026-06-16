'''Rabin Karp Algorithm
1. Ascii code
2. Rolling hash function
3. Spurious hits. '''

def wordStem(words):
    
    shortest = min(words, key=len)
    m = len(shortest)

    BASE = 257
    MOD = 10 ** 9 + 7

    def get_common_hashes(length):
        common = None

        for word in words:
            hashes = set()

            if length == 0:
                hashes.add(0)
            elif len(word) >= length:
                h = 0
                power = 1

                for i in range(length):
                    h = (h * BASE + ord(word[i])) % MOD
                    if i < length - 1:
                        power = (power * BASE) % MOD

                hashes.add(h)

                for i in range(length, len(word)):
                    h = (
                        (h - ord(word[i - length]) * power) * BASE
                        + ord(word[i])
                    ) % MOD

                    h %= MOD
                    hashes.add(h)

            if common is None:
                common = hashes
            else:
                common &= hashes

            if not common:
                return set()

        return common

    left, right = 0, m
    best_len = 0

    while left <= right:
        mid = (left + right) // 2

        if get_common_hashes(mid):
            best_len = mid
            left = mid + 1
        else:
            right = mid - 1

    if best_len == 0:
        return ""

    common_hashes = get_common_hashes(best_len)

    result = []

    for i in range(m - best_len + 1):
        sub = shortest[i:i + best_len]

        h = 0
        for ch in sub:
            h = (h * BASE + ord(ch)) % MOD

        if h in common_hashes:
            if all(sub in word for word in words):
                result.append(sub)

    return min(result)

words = [
    "grace",
    "graceful",
    "disgraceful",
    "gracefully"
]

print(wordStem(words))