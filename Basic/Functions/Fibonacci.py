def Fibonacci(num):
    a = 0
    b = 1
    while a <= num:
        if a == num:
            return True
        else: 
            a,b = b,a + b
    else:
        return False

num = int(input("Enter the value : "))
value = Fibonacci(num)
print(value)
