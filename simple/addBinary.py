# -*- coding:utf-8 -*-
# author:HHQ
# datetime:2023/6/29 13:21
# software: PyCharm

# 二进制字符相加
class Solution:
    # 使用内置函数实现
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]

    # 通解
    def common_addBinary(self, a: str, b: str) -> str:
        i, j, carry, res = len(a) - 1, len(b) - 1, 0, ""
        while i >= 0 or j >= 0 or carry:
            if i >= 0:
                carry += int(a[i])
                i -= 1
            if j >= 0:
                carry += int(b[j])
                j -= 1
            res = str(carry % 2) + res
            carry //= 2
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.addBinary('100111', '11111'))
