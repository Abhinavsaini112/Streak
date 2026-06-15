def LongConsSeq(arr): 
    '''Method 1
    sort the array than find the longest consecutive sequence .'''

    '''Method 2 
    using the dictionary . '''

    result_map = {}
    max_length = 0
    start,end = 0,0

    for i in arr:
        result_map[i] = True

    for i in result_map:
        if i - 1 not in result_map:
            count = 0
            j = i
            while j in result_map:
                count += 1
                j += 1
            if count > max_length:
                max_length = count
                start = i
                end = start + max_length -1  

    return [start,end]
'''At first glance, the nested while loop looks like O(n²):
while j in result_map:
    count += 1
    j += 1
But notice:
A number is visited in the while loop only when it belongs to a sequence starting point.
Across the entire algorithm, each number is processed at most once inside the while.
Example:
1 2 3 4 5 6 7
Only 1 starts a sequence.
The while loop visits:
1 → 2 → 3 → 4 → 5 → 6 → 7
once.
Therefore total work is:
O(n)'''

arr = [2,12,9,16,10,5,3,20,25,11,1,8,9]
answer = LongConsSeq(arr)
print(answer)
    