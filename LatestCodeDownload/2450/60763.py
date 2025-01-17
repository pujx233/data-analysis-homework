def extreme_insertion_index(nums, target, left):
    lo = 0
    hi = len(nums)

    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] > target or (left and target == nums[mid]):
            hi = mid
        else:
            lo = mid + 1

    return lo


def searchRange(nums, target):
    left_idx = extreme_insertion_index(nums, target, True)

    # assert that `left_idx` is within the array bounds and that `target`
    # is actually in `nums`.
    if left_idx == len(nums) or nums[left_idx] != target:
        return [-1, -1]

    return [left_idx, extreme_insertion_index(nums, target, False) - 1]


nums = eval('['+input()+']')
nums = list(nums)
target = int(input())
print(searchRange(nums,target))