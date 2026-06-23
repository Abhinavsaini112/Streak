def Fibonacci(n):
    a , b = 0 , 1
    if n <= 0:
        return 0
    
    for i in range(n):
        a , b = b , a + b
        
    return a
    
print(Fibonacci(6))

