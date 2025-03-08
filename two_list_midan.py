
'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

This code calculates the median of two sorted arrays by merging them into one array, sorting it, and identifying the middle element(s). It's useful for statistical analysis when combining datasets to find their central tendency.
'''
def median(arr1,arr2,m,n):
    arr3=[]
    arr3.extend(arr1)
    arr3.extend(arr2)
    arr3.sort()
    print(arr3)
    if len(arr3)%2!=0:
        index=(len(arr3)//2)
        mid=arr3[index]
        if (-10**6) <=mid and mid<= (10**6):
            print("Sorted combine list is",arr3,"Median is",mid)
    else:
        mid_1=(len(arr3)//2)
        mid_2=(len(arr3)//2)+1 
        if (-10**6) <=mid_1 and mid_2<= (10**6): 
            mid=(mid_1+mid_2)/2 
            print("Sorted combine list is",arr3,"Midian is",mid)

arr1=[10,2]
arr2=[3,4]
n=len(arr1)
m=len(arr2)

if 0<=n<=1000:
    if 0<=m<=1000:
       if 0<=m+n<=2000:
           median(arr1,arr2,m,n)
