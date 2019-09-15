def append_n_times(arr, num, count):
    for i in range(count):
        arr.append(num)

def sortNums(nums):
    counts = {}

    for num in nums:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    keys = counts.keys()
    min_key = min(keys)
    max_key = max(keys)
    med_key = None
    for k in keys:
        if k > min_key and k < max_key:
            med_key = k
            break

    arr_output = []
    append_n_times(arr_output, min_key, counts[min_key])
    append_n_times(arr_output, med_key, counts[med_key])
    append_n_times(arr_output, max_key, counts[max_key])
    return arr_output

# Fill this in.

print(sortNums([3, 3, 2, 1, 3, 2, 1]))
# [1, 1, 2, 2, 3, 3, 3]