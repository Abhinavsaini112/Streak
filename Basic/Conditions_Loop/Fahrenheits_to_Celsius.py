def Fahrenheits_to_Celsius(start,end,k):
    for i in range(start,end + 1,k):
        Celsius = (i - 32) * 5 // 9
        print(i, Celsius)


Fahrenheits_to_Celsius(0,100,20)