def FindDifference(list_1   ,list_2):
    set1 = set(list_1)
    set2 = set(list_2)

    diff_1 = list(set1 - set2)
    diff_2 = list(set2 - set1)

    return [diff_1,diff_2]

list1 = [1,2,3,4]
list2 = [5,2,8,9]
print(FindDifference(list1,list2))

def Finddifference(list_1,list_2):
    set1 = set(list_1)
    set2 = set(list_2)

    only_in_nums1 = []
    only_in_nums2 = []

    for i in set1:
        if i not in set2:
            only_in_nums1.append(i)

    for j in set2:
        if j not in set1:
            only_in_nums2.append(j)

    return [only_in_nums1,only_in_nums2]

list1 = [1,2,3,4]
list2 = [5,2,8,9]
print(FindDifference(list1,list2))