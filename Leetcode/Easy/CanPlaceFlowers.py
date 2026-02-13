def PlaceFlower(flowers,n):
    if n == 0:
        True
    for i in range(len(flowers)):
        empty = (flowers[i] == 0)
        leftempty = (i == 0) or (flowers[i-1] == 0)
        rightempty = (i==len(flowers)-1 )or (flowers[i+1] == 0)
        
        if empty and leftempty and rightempty:
            flowers[i] = 1
            n -= 1
            if n == 0:
                return True
    return False

flowers = [0,1,0,0,0]
n = 2
result = PlaceFlower(flowers,n)
print(result)


# Time Complexity O(n)
# Space Complexity O(1)