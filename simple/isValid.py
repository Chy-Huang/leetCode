# -*- coding:utf-8 -*-
# author:HHQ
# datetime:2023/6/27 9:57
# software: PyCharm
# 判断完整的括号

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack


if __name__ == '__main__':
    solution = Solution()
    print(solution.isValid('()[]{}'))
