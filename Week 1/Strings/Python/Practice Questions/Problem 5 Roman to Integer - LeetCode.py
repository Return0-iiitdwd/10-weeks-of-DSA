# https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        ans = 0
        i = 0
        while i < len(s):
            n = s[i]
            if n == 'I':
                if i < len(s) - 1:
                    if s[i + 1] == 'V':
                        ans += 4
                        i += 1
                    elif s[i + 1] == 'X':
                        ans += 9
                        i += 1
                    else:
                        ans += 1
                else:
                    ans += 1
            elif n == 'X':
                if i < len(s) - 1:
                    if s[i + 1] == 'L':
                        ans += 40
                        i += 1
                    elif s[i + 1] == 'C':
                        ans += 90
                        i += 1
                    else:
                        ans += 10
                else:
                    ans += 10
            elif n == 'C':
                if i < len(s) - 1:
                    if s[i + 1] == 'D':
                        ans += 400
                        i += 1
                    elif s[i + 1] == 'M':
                        ans += 900
                        i += 1
                    else:
                        ans += 100
                else:
                    ans += 100
            else:
                ans += d[n]
            i += 1
        return ans

# Time Complexity O(n)
# Space Complexity O(1)
