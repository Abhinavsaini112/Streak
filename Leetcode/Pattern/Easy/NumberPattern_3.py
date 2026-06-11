def NumberPattern(num):
    # print(1)
    # for i in range(1,num):
    #     print(1,end = '')
    #     j = 1
    #     while j < i:
    #         print(2,end = '')
    #         j += 1
    #     print(1)

    'or'
    for i in range(num):
        for j in range(i + 1):
            if j == 0 or j == i :
                print(1, end = '')
            else: 
                print(2, end = '')
        print()


value = int(input("Enter the integer value : "))
NumberPattern(value)