# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Brisky
@Version        :  WIN10, Python3.7.9
------------------------------------
@IDE            ： PyCharm
@Description    :
参考链接
https://blog.csdn.net/gongjianbo1992/article/details/105417509
疑问点
1. 为什么打印节点信息语句放在递归的最后一行就成了后序遍历
首先明确后序遍历的定义,先访问左子树,然后访问右子树,最后访问根节点
当你访问到叶子节点,不存在左子树,右子树,此时需要打印节点信息,然后递归退层
接着开始访问右子树信息,因为不存在左右子树,也需要打印,然后递归退层
此时就打印根节点信息,就符合后序遍历的特点

2. 上一层数据是否优先遍历
在递归退层的过程如果遇到上一层数据则会遍历
@CreateTime     :  28/12/2022 14:22
------------------------------------
"""


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


class BinaryTree:
    def __init__(self, args: list):
        self.__root = None  # 根节点
        self.create(args)

    def create(self, args):
        """
        根据参数构建二叉树,采用层级式构建,生成完全二叉树
        :param args:
        :return:
        """
        if not isinstance(args, list):
            raise ValueError("parameter type must be list")
        args_len = len(args)
        if args_len <= 0:
            raise ValueError('length must be greater than 0')
        node_list = []
        for value in args:
            node_list.append(Node(value))
        index = 0
        # 把节点串起来,成为一棵完全二叉树
        while index < args_len:
            # 下标为index的节点x的左右子树的索引分别是2*index+1, 2*index+2
            if 2 * index + 1 < args_len:
                node_list[index].left = node_list[2 * index + 1]
            if 2 * index + 2 < args_len:
                node_list[index].right = node_list[2 * index + 2]
            index += 1
        else:
            self.__root = node_list[0]

    def preorder(self):
        # 前序遍历
        """
        先访问根节点,再访问左右子树
        左子树没有后续节点,则返回访问左子树
        左子树访问完后访问右子树
        个人见解:始终都是先访问根节点,然后再访问左孩子,最后访问右孩子
        疑问:递归给人的感觉就像是每个节点都是根节点的变种
        :return:
        """

        def preorder_recursive(node: Node):
            if node == None:
                # 当一个节点没有左孩子,右孩子时候退层
                return
            print(node.value, end=" ")  # 先访问根节点
            preorder_recursive(node.left)  # 递归访问左子树
            preorder_recursive(node.right)  # 递归访问右子树

        print(f"递归式前序遍历")
        preorder_recursive(self.__root)

        def preorder_forloop(node: Node):
            node_stack = []  # 专门用来存放需要遍历的节点信息
            cursor = node
            while cursor != None or len(node_stack) != 0:  # 判断当前节点是否为空or节点列表为空,为什么需要后面这个条件
                # 后面这个条件存在的原因是访问到叶子节点,
                if cursor != None:
                    print(node.value,end=" ")# 前序遍历,一开始访问到的点肯定是父节点
                    node_stack.append(cursor)
                    cursor=cursor.left
                else: # 当左孩子为空,那么就需要弹出父节点,然后访问右节点
                    cursor=node_stack.pop()
                    cursor=cursor.right
                    pass

        print(f'for循环前序遍历')
        preorder_forloop(self.__root)

    def inorder(self):
        # 中序遍历
        pass

    def postorder(self):
        # 后序遍历
        print()
        pass

    def breadthFirst(self):
        # 广度优先-层级遍历
        pass


if __name__ == '__main__':
    pass
