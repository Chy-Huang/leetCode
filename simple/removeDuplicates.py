# -*- coding:utf-8 -*-
# author:HHQ
# datetime:2023/6/27 15:43
# software: PyCharm
# 去除重复字段，不增加内存空间
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1


if __name__ == '__main__':
    solution = Solution()
    print(solution.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
