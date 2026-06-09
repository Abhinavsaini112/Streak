def NumberPattern(num):
    for i in range(num):
        for j in range(i + 1):
            print(1,end = '')
        print()

num = int(input("Enter the number : "))
NumberPattern(num)
