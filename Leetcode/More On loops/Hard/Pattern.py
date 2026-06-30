def Pattern(num):
    k = num // 2
    if num % 2 != 0:
        k += 1
    for i in range(k):
        for j in range(1,num + 1):
            print(num * 2 * i + j, end = ' ')
        print()
    
    for i in range(k - 1,0,-1):
        for j in range(1,num + 1):
            print(num * (2 * i - 1) + j, end = ' ')
        print()

Pattern(6)


