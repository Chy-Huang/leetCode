# -*- coding:utf-8 -*-
# author:HHQ
# datetime:2023/6/27 11:25
# software: PyCharm
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode],
                      list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # 如果一个链表已经遍历完，就将另一个链表剩下的部分连接到结果链表的后面
        if list1:
            current.next = list1
        else:
            current.next = list2

        return dummy.next


def create_linked_list(lst):
    dummy = ListNode(0)
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next


def print_linked_list(head):
    while head:
        print(head.val, end=' ')
        head = head.next


if __name__ == '__main__':
    solution = Solution()
    list1 = create_linked_list([1, 2, 4])
    list2 = create_linked_list([1, 3, 4])
    merged_list = solution.mergeTwoLists(list1, list2)
    print_linked_list(merged_list)
