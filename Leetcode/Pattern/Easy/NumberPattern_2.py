def NumberPattern(num):
    print(1)
    for i in range(1,num):
        print(i,end = '')
        zero = 1
        while zero < i:
            print(0,end = '')
            zero += 1
        print(i)
        
            
        

value = int(input("Enter the integer value : "))
NumberPattern(value)