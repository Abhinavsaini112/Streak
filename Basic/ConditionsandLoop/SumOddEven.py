def SumOddEven(num):
    sumodd,sumeven = 0,0
    while num > 0 :
        remainder = num % 10
        if (remainder % 2) == 0:
            sumeven += remainder
        else:
            sumodd += remainder
        num = num // 10
    return (sumeven, sumodd)

num = int(input("Enter the number : "))
even , odd = SumOddEven(num)
print(even , odd)
