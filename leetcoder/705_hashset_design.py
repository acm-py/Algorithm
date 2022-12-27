# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Brisky
@Version        :  WIN10, Python3.7.9
------------------------------------
@IDE            ： PyCharm-> 705_hashset_design.py
@Description    :
题目
不使用任何内建的哈希表库设计一个哈希集合（HashSet）。

实现 MyHashSet 类：

void add(key) 向哈希集合中插入值 key 。
bool contains(key) 返回哈希集合中是否存在这个值 key 。
void remove(key) 将给定值 key 从哈希集合中删除。如果哈希集合中没有这个值，什么也不做。
参考
https://leetcode.cn/problems/design-hashset/solutions/653252/xiang-jie-hashset-de-she-ji-zai-shi-jian-4plc/?languageTags=python3
@CreateTime     :  2022/12/23 22:03
------------------------------------
分析:
hash函数设计:
通过hash方式把键key转换成数组的索引,一般都是对分桶数取模%
处理碰撞冲突问题:拉链法和线性探测法
疑问点:
为什么buckets和itemsPerBucket会是1000和1001呢?
如果是相同元素被不断插入会不会有问题
"""


# 定长拉链数组
class MyHashSet:
    def __init__(self):
        self.buckets = 1000
        self.itemsPerBucket = 1001  # 每个桶能放的数据长度
        self.table = [[] for _ in range(self.buckets)]  # 先初始化所有的桶,不过桶为空数组,为了节省内存

    def hash(self, key):
        """
        求出某个键应该在哪个桶里头
        :param key:
        :return:
        """
        return key % self.buckets

    def pos(self, key):
        """求出key位于桶中的数组中的哪一个位置"""
        return key // self.buckets
        pass

    def add(self, key):
        hashkey = self.hash(key)
        if not self.table[hashkey]:
            self.table[hashkey] = [0] * self.itemsPerBucket  # 如果命中某个hashkey的话则自动创建itemsPerBucket长的空间用来存放数据
        self.table[hashkey][self.pos(key)] = 1
        pass

    def remove(self, key):
        hashkey = self.hash(key)
        # 先判断是否存在,再将pos标志位设置成0
        if self.table[hashkey]:
            self.table[hashkey][self.pos(key)] = 0
        pass

    def contains(self, key):
        hashkey = self.hash(key)
        # 判断table中某个键是否为空列表,一旦为空列表就利用and 短除法,直接返回false
        return (self.table[hashkey] != []) and (self.table[hashkey][self.pos(key)] == 1)
        pass
