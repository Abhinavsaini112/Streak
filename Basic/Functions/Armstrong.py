'''No, negative numbers cannot be Armstrong numbers.'''

def Armstrong(num):
    temp = num
    count = len(str(num))
    armstrong = 0
    while temp > 0:
        remainder = temp % 10
        armstrong += remainder ** count
        temp //= 10

    return armstrong == num

num = int(input("Enter the number: "))
print(Armstrong(num))
