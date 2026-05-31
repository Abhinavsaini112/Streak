def PairSumto_0(array):
    result = {}

    for i in array:
        result[i] = result.get(i,0) + 1

    count = 0
    visited = set()

    for nums in result:

        if nums in visited : 
            continue
        
        if nums == 0:
            count += result[0]*(result[-0]-1)//2

        elif -nums in result :
            count += result[nums]*result[-nums]
        
        visited.add(nums)
        visited.add(-nums)

    return count
    
# array = [2,-2,2,1,-6,-2,6,3]
array = [0,0,0,0]
freq = PairSumto_0(array)
print(freq)


def PairSum0(nums):

    count = 0
    result = {}
    for i in nums:
        count += result.get(-i,0)
        result[i] = result.get(i,0) + 1

    return count

array = [2,-2,2,1,-6,-2,6,3]
array1 = [0,0,0]
freq = PairSum0(array)
freq1 = PairSum0(array1)
print(freq)
print(freq1)
