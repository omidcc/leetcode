def twoSum(nums, target):
    indices = []
    for i in range(0, len(nums)):
        dif = target - nums[i]
        # print(dif)
        if dif in nums:
            index = list.index(nums, dif)
            if i != index:
                if i not in indices:
                    indices.append(i)
                if index not in indices:
                    indices.append(index)

    return indices


print(twoSum([2, 7, 11, 5], 9))
