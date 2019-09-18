def check(nums):
    # Fill this in.
    just_switched = False
    num_need_to_change = 0
    first = True
    for i in range(len(nums)):
        if first:
            first = False
        else:
            if nums[i-1] > nums[i]:
                num_need_to_change += 1
                nums[i] = nums[i-1]

    if num_need_to_change > 1:
        return False
    return True


print(check([13, 4, 7]))
# True
print(check([5, 1, 3, 2, 5]))
# False

print(check([1, 1, 45, 1]))

print(check([3,4,2,3]))
