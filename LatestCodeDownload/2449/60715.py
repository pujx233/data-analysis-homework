def search(nums, target):
    left = 0
    right = len(nums) - 1
    if len(nums) == 0:
        return -1
    if target >= nums[0]:
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[0]:
                right = mid - 1
            else:
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid
    else:
        while left < right:
            mid = (left + right) // 2
            if nums[mid] >= nums[0]:
                left = mid + 1
            else:
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid
    if nums[left] == target:
        return left
    return -1
nums=list(map(int,input().split(',')))
target=int(input())
print(search(nums,target))