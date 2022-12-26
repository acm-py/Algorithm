'''
Author: bing acmpy4592@gmail.com
Date: 2022-12-26 19:09:19
LastEditors: bing acmpy4592@gmail.com
LastEditTime: 2022-12-26 19:09:24
FilePath: \Algorithm\LeetCode\动态规划\LeetCode509.py
Description: 

Copyright (c) 2022 by bing acmpy4592@gmail.com, All Rights Reserved. 
'''
class Solution:

    def fib(self, n: int) -> int:

        # 没有优化的递归写法

        # if n == 0:

        #     return 0

        # if n == 1:

        #     return 1

        # return self.fib(n-1) + self.fib(n-2)

        # 加备忘录的递归写法

        # hashmap = [0 for _ in range(n+1)]

        # if n == 0:

        #     return 0

        # if n == 1:

        #     return 1

        # if hashmap[n] != 0:

        #     return hashmap[n]

        # hashmap[n] = self.fib(n-1) + self.fib(n-2)

        # return hashmap[n]

  

        # 动态规划解法

        if n == 0:

            return 0

        dp = [0 for _ in range(n+1)]

        # base case

        dp[0] = 0

        dp[1] = 1

        for i in range(2, n+1):

            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]