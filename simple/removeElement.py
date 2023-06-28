# -*- coding:utf-8 -*-
# author:HHQ
# datetime:2023/6/27 17:49
# software: PyCharm
# 移除数组元素，不论顺序
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(0, len(nums)):
            if val == nums[i]:
                nums.pop(nums[i])
        return nums

if __name__ == '__main__':
    solution = Solution()
    print(solution.removeElement([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))