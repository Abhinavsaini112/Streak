def SumEven(num):
    total = 0
    for i in range(1,num+1):
        if i % 2 == 0:
            total += i

    return total


print(SumEven(5))