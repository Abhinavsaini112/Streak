def BinaryPattern(num):
    for i in range(num):
        if i % 2 == 0:
            for j in range(num - i,0,-1):
                print(1, end = '')
        else:
            for j in range(num - i,0,-1):
                print(0, end = '')
        print()

BinaryPattern(5)