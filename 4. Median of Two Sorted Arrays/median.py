def findMedianSortedArrays(nums1, nums2):
    mergedArray = nums1 + nums2
    i = 0
    mergedArray.sort()
    n = len(mergedArray)
    median = 0.0
    if n % 2:
        median = mergedArray[int(n/2)]
    else:
        median = (mergedArray[(int(n/2))-1] + mergedArray[int(n/2)])/2.0
    return median


print(findMedianSortedArrays([1, 2], [3, 4]))
