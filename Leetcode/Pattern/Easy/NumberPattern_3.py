def NumberPattern(num):
    print(1)
    for i in range(1,num):
        print(1,end = '')
        j = 1
        while j < i:
            print(2,end = '')
            j += 1
        print(1)

value = int(input("Enter the integer value : "))
NumberPattern(value)