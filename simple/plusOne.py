# -*- coding:utf-8 -*-
# author:HHQ
# datetime:2023/6/28 14:58
# software: PyCharm
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return list(map(int, list(str(int(''.join(map(str, digits))) + 1))))


if __name__ == '__main__':
    solution = Solution()
    print(solution.plusOne([9, 9, 9]))
