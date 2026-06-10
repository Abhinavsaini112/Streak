def NumberPattern(num):

    for i in range(num):
        j = 0 
        while j <= i:
            print(j+1,end = '')
            j += 1

        k = (num - i - 1) * 2
        while k  > 0:
            print(' ',end = '')
            k -= 1
        
        m = j 
        while m >= 1:
            print(m , end = '')
            m -= 1

        print()

value = int(input("Enter the integer value : "))
NumberPattern(value)
