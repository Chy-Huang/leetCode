# -*- coding:utf-8 -*-
# author:HHQ
# datetime:2023/6/29 14:10
# software: PyCharm
from functools import reduce


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        dp = [0 for _ in range(n + 1)]
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[i]

    # 使用斐波那契数列
    def climbStairs_reduce(self, n: int) -> int:
        return reduce(lambda x, _: x + [x[-1] + x[-2]], range(n - 1), [1, 2])[n]


if __name__ == '__main__':
    solution = Solution()
    print(solution.climbStairs(9))
