def PyramidPattern(num):
    for i in range(num):
        j = num - i - 1
        while j > 0 :
            print(' ', end = '')
            j -= 1
        
        k = i + 1
        while k > 0 :
            print(k, end = '')
            k -= 1
        
        l = k + 1
        while l <= i :
            print(l + 1, end = '')
            l += 1
        
        print()

value = int(input("Enter the value of n : "))
PyramidPattern(value)