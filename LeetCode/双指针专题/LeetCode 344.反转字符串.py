'''
Author: bing acmpy4592@gmail.com
Date: 2022-12-28 21:28:34
LastEditors: bing acmpy4592@gmail.com
LastEditTime: 2022-12-28 21:28:44
FilePath: \Algorithm\LeetCode\双指针专题\LeetCode 344.反转字符串.py
Description: 

Copyright (c) 2022 by bing acmpy4592@gmail.com, All Rights Reserved. 
'''
from typing import List


class Solution:

    def reverseString(self, s: List[str]) -> None:

        """

        Do not return anything, modify s in-place instead.

        """

        left, right = 0, len(s)-1

        while left < right:

            s[left], s[right] = s[right], s[left]

            left += 1

            right -= 1