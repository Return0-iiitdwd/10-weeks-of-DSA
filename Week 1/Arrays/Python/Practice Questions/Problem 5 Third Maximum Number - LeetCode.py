# https://leetcode.com/problems/third-maximum-number/

class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        s = set(nums)
        if len(s) > 2:
            return sorted(list(s))[-3]
        else:
            return max(s)

# Time Complexity O(n)
# Space Complexity O(n)
