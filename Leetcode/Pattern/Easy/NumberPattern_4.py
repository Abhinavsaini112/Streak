def NumberPattern(num):
    for i in range(num,0,-1):
        j = 1
        while j <= i:
            print(j, end = '')
            j += 1
        print()

value = int(input("Enter the integer value : "))
NumberPattern(value)
