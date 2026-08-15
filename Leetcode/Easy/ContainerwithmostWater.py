def WaterContainer(li):
    left = 0
    right = len(li) - 1
    max_area = 0

    while left < right:
        width = right - left
        height = min(li[left], li[right])

        area = height * width
        max_area = max(max_area, area)

        if li[left] < li[right]:
            left += 1
        else:
            right -= 1

    return max_area


li = [3, 4, 1, 2, 2, 4, 1, 3, 2]
print(WaterContainer(li))


def WaterContainer(li):
    left = 0 
    right = len(li) - 1
    max_area = 0

    for i in range(len(li) - 1, -1, -1):
        area = min(li[left],li[right]) * i
        max_area = max(max_area, area)

        if li[left] < li[right]:
            left += 1
        else:
            right -= 1
            
    return max_area

li = [2, 1, 8, 6, 4, 6, 5, 5]
print(WaterContainer(li))

'''Time Complexity is O(n)
Space Complexity is O(n)'''

