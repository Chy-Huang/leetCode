# -*- coding:utf-8 -*-
# author:HHQ
# datetime:2023/6/28 14:19
# software: PyCharm

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split(' ')
        last_non_empty = next((x for x in reversed(words) if x != ''), 'default')
        return last_non_empty.__len__()


if __name__ == '__main__':
    solution = Solution()
    print(solution.lengthOfLastWord("   fly me   to   the moon  "))
