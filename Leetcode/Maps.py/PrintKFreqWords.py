def Freq_k(arr,k):
    li = []
    result = {}
    words = arr.split()
    for i in words:
        result[i] = result.get(i,0) + 1
        
    for key in result:
        if result[key] == k :
            li.append(key)
    '''or
    return [word for word,count in result.items() if count == k ]
    '''
    return li

array = "this is a word string having many many word"
answer = Freq_k(array,2)
print(answer)