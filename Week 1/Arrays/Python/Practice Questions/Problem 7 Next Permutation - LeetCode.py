# https://leetcode.com/problems/next-permutation/

class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(n - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                nums[i:] = sorted(nums[i:])
                j = i - 1
                for k in range(i, n):
                    if nums[j] < nums[k]:
                        nums[j], nums[k] = nums[k], nums[j]
                        return nums
        return nums.reverse()

# Time Complexity O(n ^ 2)
# Space Complexity O(n)
