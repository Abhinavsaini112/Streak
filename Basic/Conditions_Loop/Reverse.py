def ReverseNumber(num):
    rev = 0
    while num > 0:
        remainder = num % 10
        rev = rev * 10 + remainder
        num = num // 10
    return rev

num = int(input("Enter the number : "))
print(ReverseNumber(num))