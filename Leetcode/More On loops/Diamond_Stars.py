def Diamond_Start(num):
    n1 = (num + 1) // 2
    n2 = n1 - 1
    for i in range(1,n1 + 1,1):
        for j in range(n1 - i , 0, -1):
            print(' ', end = '')
        for j in range(i * 2 - 1):
            print('*', end = '')
        print()
    
    for i in range(n2):
        for j in range(i + 1):
            print(' ', end = '')
        for j in range(2 * (n2 - i) - 1,0, -1):
            print('*', end = '')
        print()



Diamond_Start(7)