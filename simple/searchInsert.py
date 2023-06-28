# -*- coding:utf-8 -*-
# author:HHQ
# datetime:2023/6/28 13:43
# software: PyCharm
from typing import List


# 搜索插入位置

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            for key, values in enumerate(nums):
                if target < nums[0]:
                    nums.insert(0, target)
                    return 0
                elif target > nums[-1]:
                    nums.append(target)
                    return nums.index(target)
                elif values < target < nums[key + 1]:
                    return key + 1

    def searchNotInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return len(nums)


if __name__ == '__main__':
    solution = Solution()
    print(solution.searchInsert([1, 3, 5, 6], 7))
