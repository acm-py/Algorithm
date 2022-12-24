'''
Author: bing acmpy4592@gmail.com
Date: 2022-12-24 21:17:54
LastEditors: bing acmpy4592@gmail.com
LastEditTime: 2022-12-24 21:18:08
FilePath: \Algorithm\LeetCode\剑指offer系列\LeetCode 剑指offer27. 二叉树的镜像.py
Description: 

Copyright (c) 2022 by bing acmpy4592@gmail.com, All Rights Reserved. 
'''
# Definition for a binary tree node.

class TreeNode:

    def __init__(self, x):

        self.val = x

        self.left = None

        self.right = None

  

class Solution:

    # 递归方法
    def mirrorTree(self, root: TreeNode) -> TreeNode:

        if not root:

            return root

        root.left, root.right = root.right, root.left

        self.mirrorTree(root.left)

        self.mirrorTree(root.right)

        return root