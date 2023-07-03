# -*- coding:utf-8 -*-
# author:HHQ
# datetime:2023/6/29 13:52
# software: PyCharm


class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        while left <= right:
            mid = (left + right) // 2
            if mid * mid <= x < (mid + 1) * (mid + 1):
                return mid
            elif x < mid * mid:
                right = mid
            else:
                left = mid + 1


if __name__ == '__main__':
    solution = Solution()
    print(solution.mySqrt(7))