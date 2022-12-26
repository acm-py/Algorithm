'''
Author: bing acmpy4592@gmail.com
Date: 2022-12-26 19:06:26
LastEditors: bing acmpy4592@gmail.com
LastEditTime: 2022-12-26 19:06:49
FilePath: \Algorithm\LeetCode\动态规划\LeetCode 322.零钱兑换.py
Description: 

Copyright (c) 2022 by bing acmpy4592@gmail.com, All Rights Reserved. 
'''
from typing import List

class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        inf = amount + 1
        dp = [inf for _ in range(amount + 1)]
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[amount] if dp[amount] != (amount + 1) else -1
