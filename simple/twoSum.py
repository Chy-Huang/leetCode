# -*- coding:utf-8 -*-
# author:HHQ
# datetime:2023/6/27 9:19
# software: PyCharm
# 判断两数之和，并返回index
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for i, num in enumerate(nums):
            if target - num in num_dict:
                return [num_dict[target - num], i]
            num_dict[num] = i
        return None


if __name__ == '__main__':
    solution = Solution()
    print(solution.twoSum([2, 7, 11, 15], 9))
