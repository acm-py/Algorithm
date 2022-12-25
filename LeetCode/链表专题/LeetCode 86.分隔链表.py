'''
Author: bing acmpy4592@gmail.com
Date: 2022-12-25 21:14:07
LastEditors: bing acmpy4592@gmail.com
LastEditTime: 2022-12-25 21:14:19
FilePath: \Algorithm\LeetCode\链表专题\LeetCode 86.分隔链表.py
Description: 

Copyright (c) 2022 by bing acmpy4592@gmail.com, All Rights Reserved. 
'''
# Definition for singly-linked list.
from typing import Optional

class ListNode:

    def __init__(self, val=0, next=None):

        self.val = val

        self.next = next

class Solution:

    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        # 1. 把一条链表分割成两条链表

        # 2. 一个链表中的元素大小都小于x，另一个链表中元素大小都大于等于x

        # 3. 合并两条链表

        res = ListNode()

        cur = res

        # 小于x的链表

        lessList = ListNode()

        # 大于等于x的链表

        growList = ListNode()

        p1, p2 = lessList, growList

        while head is not None:

            if head.val >= x:

                growList.next = head

                growList = growList.next

            else:

                lessList.next = head

                lessList = lessList.next

            temp = head.next

            # 断开每个节点的next指针

            head.next = None

            head = temp

        lessList.next = p2.next

        return p1.next