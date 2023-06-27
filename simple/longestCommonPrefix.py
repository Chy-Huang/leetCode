# -*- coding:utf-8 -*-
# author:HHQ
# datetime:2023/6/27 9:19
# software: PyCharm
# 最长公共前缀
from typing import List


class Solution:
    # 时间复杂度为O(n*m)
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        shortest_str = min(strs, key=len)
        for i, char in enumerate(shortest_str):
            for other in strs:
                if other[i] != char:
                    return shortest_str[:i]
        return shortest_str

    # 时间复杂度无限接近O(n)
    def longestCommonPrefix_On(self, strs: List[str]) -> str:
        if not strs:
            return ""
        strs.sort()
        first = strs[0]
        last = strs[-1]
        i = 0
        while i < len(first) and i < len(last) and first[i] == last[i]:
            i += 1
        return first[:i]


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestCommonPrefix(["flower", "flow", "flight"]))
    print(solution.longestCommonPrefix_On(["flower", "flow", "floight"]))




