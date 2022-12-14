# https://leetcode.com/problems/integer-to-roman/

class Solution:
    def intToRoman(self, num: int) -> str:
        hun = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
        ten = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
        one = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']

        th, num = divmod(num, 1000)
        hu, num = divmod(num, 100)
        te, on = divmod(num, 10)

        ans = 'M' * th + hun[hu] + ten[te] + one[on]
        return ans

# Time Complexity O(1)
# Space Complexity O(n)
