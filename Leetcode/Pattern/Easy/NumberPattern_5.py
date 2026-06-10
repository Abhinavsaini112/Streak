def NumberPattern(num):
    for i in range(num):
        char = chr(ord('A') + i)
        for j in range(i+1):
            print(char, end = '')
        print()

value = int(input("Enter the integer value : "))
NumberPattern(value)
