def KidsCandies(candies,extracandies):
    value=max(candies)
    result=[]
    for candy in candies:
        result.append(candy+extracandies>=value)
    return result

candies=[2,3,5,1,3]
extracandies=3
answer=KidsCandies(candies,extracandies)
print(answer)

'''Time Complexity is O(n) and Space Complexity is O(n)'''
