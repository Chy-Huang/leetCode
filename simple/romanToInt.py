# -*- coding:utf-8 -*-
# author:HHQ
# datetime:2023/6/27 9:19
# software: PyCharm
# 根据罗马字符计算数字

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {
            'I': 1,
            'IV': 4,
            'V': 5,
            'IX': 9,
            'X': 10,
            'XL': 40,
            'L': 50,
            'XC': 90,
            'C': 100,
            'CD': 400,
            'D': 500,
            'CM': 900,
            'M': 1000}
        i, total = 0,0
        while i < len(s):
            if s[i: i + 2] in roman_dict:
                total += roman_dict[s[i: i + 2]]
                i += 2
            else:
                total += roman_dict[s[i]]
                i += 1
        return total


if __name__ == '__main__':
    solution = Solution()
    print(solution.romanToInt("MCMXCIV"))
