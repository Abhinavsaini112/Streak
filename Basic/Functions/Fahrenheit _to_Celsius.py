def F_C(start,end,step):
    # li = []
    for i in range(start,end + 1, step):
        Celsius = (i - 32) * 5 // 9
        # li.append([i, Celsius])
        print(i,Celsius)
    # return li

start = int(input("Enter the start Fahrenheit value: "))
end = int(input("Enter the end Fahrenheit value: "))
step = int(input("Enter the value of step: "))
F_C(start,end,step)
# li = F_C(start,end,step)
# for i in li:
    # print(i)

