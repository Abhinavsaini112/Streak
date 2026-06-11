def ArrowPattern(num):
    n , m = (num + 1) // 2 , (num - 1) // 2

    for i in range(n):
        for j in range(i): 
            print(" ", end = '')

        for k in range(i+1):
            print('*', end = '')

        print()
    
    for i in range(m):
        for j in range(m-i-1,0,-1):
            print(' ', end = '')
        
        for k in range(m-i,0,-1):
            print('*', end = '')
        
        print()
    
    

        
value = int(input("Enter the value of n : "))
ArrowPattern(value)
