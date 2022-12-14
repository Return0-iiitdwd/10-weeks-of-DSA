# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/

import math


class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        lp = [math.inf for _ in range(k + 1)]
        mpro = [0 for _ in range(k + 1)]
        for p in prices:
            for i in range(1, k + 1):
                lp[i] = min(lp[i], p - mpro[i - 1])
                mpro[i] = max(mpro[i], p - lp[i])
        return mpro[-1]

# Time Complexity O(n * k)
# Space Complexity O(k ^ 2)
