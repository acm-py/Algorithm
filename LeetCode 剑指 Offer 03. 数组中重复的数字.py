'''
Author: error: git config user.name && git config user.email & please set dead value or install git
Date: 2022-12-23 16:26:25
LastEditors: error: git config user.name && git config user.email & please set dead value or install git
LastEditTime: 2022-12-23 16:48:01
FilePath: \Algorithm\LeetCode 剑指 Offer 03. 数组中重复的数字.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''

from typing import List


class Solution:

    def findRepeatNumber(self, nums: List[int]) -> int:
        # 记忆化字典
        dict_nums = {}
        for i in nums:
            if i not in dict_nums:
                dict_nums[i] = 1
            else:
                return i

    def findRepeatNumber2(self, nums: List[int]) -> int:
        # 排序
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]: 
                return nums[i]

    def findRepeatNumber3(self, nums: List[int]) -> int:
        # 原地，不使用额外的空间复杂度
        # 这里面的循环不变量就是
        # nums[val] = val -> nums[nums[val]] =  nums[val]
        for idx, val in enumerate(nums):
            if idx != val and nums[val] == val:
                return val
            # 交换
            nums[val], nums[idx] = nums[idx], nums[val]


if __name__ == "__main__":
    s = Solution()
    arr = [2, 3, 1, 0, 2, 5, 3]
    if s.findRepeatNumber(arr) in [2,3] and s.findRepeatNumber2(arr) in [2,3] and s.findRepeatNumber3(arr) in [2,3]:
        print("正确")
    else:
        print("错误")


