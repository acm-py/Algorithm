# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Brisky
@Version        :  WIN10, Python3.7.9
------------------------------------
@IDE            ： PyCharm
@Description    :
题目:
用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，
分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )
分析:
栈:先进后出
队列:先进先出

@CreateTime     :  27/12/2022 21:19
------------------------------------
"""


class CQueue:
    def __init__(self):
        self.A, self.B = [], []

    def appendTail(self, value: int) -> None:
        self.A.append(value)
        pass

    def deleteHead(self) -> int:
        if self.B:  # 如果B中还有元素,就说明上一次没有删除完
            return self.B.pop()
        if not self.A: # 如果连A都没有元素就说明B也没有元素,直接返回-1即可
            return -1
        while self.A:
            self.B.append(self.A.pop())  # 把A栈中所有的元素以倒序方式插入B栈中,正好还原了原始的插入顺序
        return self.B.pop()  # 把B的队首元素弹出来
        pass
