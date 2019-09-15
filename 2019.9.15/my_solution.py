def two_sum(list, k):
    def helper(index, target, num):
        if target == 0 and num == 0:
            return True
        if index >= len(list):
            return False
        return helper(index + 1, target, num) or helper(index + 1, target - list[index], num - 1)

    return helper(0, k, 2)

# Best solution is to make a hashmap of complements.

# True
print(two_sum([4, 7, 1, -3, 2], 5))

# False
print(two_sum([4], 5))
