nums, target = [int(i) for i in input().split(',')], int(input())
left, right = 0, len(nums) - 1
while right >= left:
    mid = int((left + right) / 2)
    if nums[mid] == target:
        print(mid)
        break

    elif nums[left] < nums[mid]:
        if nums[left] <= target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1
    else:
        if nums[mid] < target <= nums[right]:
            left = mid + 1
        else:
            right = mid - 1
else:
    print(-1)