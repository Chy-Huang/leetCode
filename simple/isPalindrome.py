# -*- coding:utf-8 -*-
# author:HHQ
# datetime:2023/6/27 9:19
# software: PyCharm
# 判断回文数
class Solution:
    def isPalindrome(self, x: int) -> bool:
        num=str(x)
        return num == num[::-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.isPalindrome('121'))