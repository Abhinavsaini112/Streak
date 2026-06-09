def NumberPattern(nums):
    for i in range(nums):
        for j in range(i+1):
            print(i,end = '')
        print()

value = int(input("Enter the integer value : "))
NumberPattern(value)