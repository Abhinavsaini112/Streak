def RectangularNumber(num):
    for i in range(num * 2 - 1):
        for j in range(num * 2 - 1):
            print(num, end = '')
        print()

RectangularNumber(3)