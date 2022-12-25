'''
Author: bing acmpy4592@gmail.com
Date: 2022-12-25 21:15:28
LastEditors: bing acmpy4592@gmail.com
LastEditTime: 2022-12-25 21:15:35
FilePath: \Algorithm\LeetCode\链表专题\LeetCode 23.合并k个升序链表.py
Description: 

Copyright (c) 2022 by bing acmpy4592@gmail.com, All Rights Reserved. 
'''
from typing import List, Optional

# Definition for singly-linked list.

class ListNode:

    def __init__(self, val=0, next=None):

        self.val = val

        self.next = next

class Solution:

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        # 最小堆

        stack = []

        for i in range(len(lists)):

            if lists[i]:

                # 将三个列表头和对应的索引存入stack

                stack.append([lists[i].val, i])

        # 初始化最小堆

        # print(stack)
        import heapq

        heapq.heapify(stack)

        # print(heapq)

        res = ListNode(-1)

        cur = res

        while stack:

            _, i = heapq.heappop(stack)

            temp = lists[i].next

            # 断开next指针

            lists[i].next = None

            cur.next = lists[i]

            cur = cur.next

            if temp:

                lists[i] = temp

                # 将该链表下一个元素放入最小堆中，自动维护

                heapq.heappush(stack, [lists[i].val, i])

        return res.next