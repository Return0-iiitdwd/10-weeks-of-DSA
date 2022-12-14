# https://leetcode.com/problems/wildcard-matching/

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        ls, lp = len(s), len(p)
        dp = [[False for _ in range(lp + 1)] for _ in range(ls + 1)]
        dp[0][0] = True

        for i in range(1, lp + 1):
            if p[i - 1] != '*':
                break
            dp[0][i] = True

        for i in range(1, ls + 1):
            for j in range(1, lp + 1):
                if p[j - 1] in {s[i - 1], '?'}:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]

        return dp[-1][-1]

# Time Complexity O(n ^ 2)
# Space Complexity O(n ^ 2)
