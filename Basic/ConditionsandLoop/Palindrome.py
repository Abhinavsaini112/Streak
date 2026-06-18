def Palindrome(num):
    rev = 0
    temp = num 
    while num > 0 :
        remainder = num % 10
        rev = rev * 10 + remainder
        num = num // 10
    
    return (rev == temp)

num = int(input("Enter the number : "))
print(Palindrome(num))