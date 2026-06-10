def NumberPattern(num):
    for i in range(num):
        j = 1
        while j <= i:
            print(0, end = '')
            j += 1
        print('*', end = '')

        k = num - i - 1
        while k > 0:
            print(0, end = '')
            k -= 1
        print('*', end = '')

        k = num - i - 1
        while k > 0:
            print(0, end = '')
            k -= 1
        print('*', end = '')

        l = 0 
        while l < i:
            print(0, end = '')
            l += 1
    
        print()


value = int(input("Enter the integer value : "))
NumberPattern(value)
