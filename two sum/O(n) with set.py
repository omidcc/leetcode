def twoSum(nums, target):
    indices = set()
    for i in range(0, len(nums)):
        dif = target - nums[i]
        if dif in nums:
            index = list.index(nums, dif)
            if i != index:
                indices.add(i)
                indices.add(index)
    return list(indices)


print(twoSum([2, 7, 11, 5], 9))
