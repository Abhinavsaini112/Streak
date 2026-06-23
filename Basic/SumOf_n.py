def Sum_n(n):
    # sum = 0
    # a = 1    
    # sum = n * (2 * a + (n - 1)) / 2
    # return sum

    # or
    total = 0
    for i in range(1, n+1):
        total += i
    return total
        
print(Sum_n(2))