class Solution:
	def moveZero(self, nums):
		k = 0
		i = 0
		while i + k < len(nums):
			while i + k < len(nums) and nums[i + k] == 0:
				k += 1
			if i + k >= len(nums):
				break
			temp = nums[i + k]
			nums[i] += temp
			nums[i + k] -= temp
			i += 1
			
		return nums

if __name__ == '__main__':
	n = int(input())
	x = Solution()
	while n > 0:
		n -= 1
		input()
		nums = input().split()
		nums = x.moveZero([int(i) for i in nums])
		for i in range(len(nums)):
			print(nums[i], end=" ")
		print()