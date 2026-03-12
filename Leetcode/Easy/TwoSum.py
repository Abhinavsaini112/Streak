from typing import List

def TwoSum(nums:List[int],target:int)->List[int]:
    pair={}
    for index,value in enumerate(nums):
        difference = target-value
        if difference in pair:
            return [pair[difference],index]
        pair[value]=index
    return ["Sum Not Found"]

nums = [2,7,11,15]
target = 9

print(TwoSum(nums,target))



