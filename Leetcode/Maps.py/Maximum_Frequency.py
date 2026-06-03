def Maximum_Frequency(arr):
    ele = None
    count = 0
    result = {}
    for i in arr:
        result[i] = result.get(i,0) + 1

        if result[i] > count :
            count = result[i]
            ele = i

    return ele

array = [2,12,2,11,12,2,1,2,2,11,12,12,12,12]
element = Maximum_Frequency(array)
print(element)
             
