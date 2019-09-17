def singleNumber(nums):
    mapping = {}
    for num in nums:
        if num not in mapping:
            mapping[num] = 1
        else:
            mapping[num] += 1

    for key in mapping:
        if mapping[key] == 1:
            return key
    return None


print(singleNumber([4, 3, 2, 4, 1, 3, 2, 5, 5]))
# 1
