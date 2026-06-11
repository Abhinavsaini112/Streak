def NumberPattern(num):
    for i in range(num):
        for j in range(1,num - i + 1):
            print(j,end = '')

        'or'
        # j = 1
        # while j <= i:
        #     print(j, end = '')
        #     j += 1
        
        print()

value = int(input("Enter the integer value : "))
NumberPattern(value)
