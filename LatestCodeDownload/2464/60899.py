def minSubArrayLen(s, nums):
    """
    :type s: int
    :type nums: List[int]
    :rtype: int
    """
    l = 0
    r = 0
    sum_all = 0
    nums_len = len(nums)
    minLength = nums_len + 1
    while l < nums_len:
        if r < nums_len and sum_all < s:
            sum_all += nums[r]
            r += 1
        else:
            sum_all -= nums[l]
            l += 1

        if sum_all >= s:
            minLength = min(minLength, r - l)

    if minLength == nums_len + 1:
        return 0

    return minLength

if __name__ == '__main__':
    target = int(input())
    list0 = list(map(int, input().split(",")))
    print(minSubArrayLen(target,list0))