from typing import List

def findMedianSortedArrays(nums1: List[int], nums2: List[int]):

    if len(nums1)>len(nums2):
        nums1,nums2=nums2,nums1
        
    n,m=len(nums1),len(nums2)
    total=n+m
    half=(total+1)//2
    left=0
    right=n

    while left<=right:
        i=(left+right)//2
        j=half-i

        left1=nums1[i-1] if i>0 else float('-inf')
        right1=nums1[i] if i<n else float('inf')
        left2=nums2[j-1] if j>0 else float('-inf')
        right2=nums2[j] if j<m else float('inf')

        if left1<=right2 and left2<=right1:
            if total%2:
                return max(left1,left2)
            return (max(left1,left2)+min(right1,right2))/2
        elif left1>right2:
            right=i-1
        else:
           left=i+1

print(findMedianSortedArrays([1,2,3,5,9,11], [7,12,14,15]))


        # newList=[]
        # m=len(nums1)
        # n=len(nums2)
        # i,j=0,0        
        # while i<m and j<n:
        #     if nums1[i]<nums2[j]:
        #         newList.append(nums1[i])
        #         i+=1
        #     else:
        #         newList.append(nums2[j])
        #         j+=1
        # while i<m:
        #     newList.append(nums1[i])
        #     i+=1
        # while j<n:
        #     newList.append(nums2[j])
        #     j+=1
        # l=len(newList)
        # mid=0
        # if l%2==0:
        #     mid=(newList[(l//2)-1]+newList[(l//2)])/2
        # else:
        #     mid=(newList[l//2])
        # return mid