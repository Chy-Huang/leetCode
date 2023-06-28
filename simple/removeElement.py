# -*- coding:utf-8 -*-
# author:HHQ
# datetime:2023/6/27 17:49
# software: PyCharm
# 移除数组元素，不论顺序
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        nums
        return len(nums)


if __name__ == '__main__':
    solution = Solution()
    print(solution.removeElement([3, 2, 2, 3], 3))
