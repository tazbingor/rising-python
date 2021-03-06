#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/10/24 上午11:06
# @Author  : Aries
# @Site    : 
# @File    : py015_lists_exercise.py
# @Software: PyCharm
# 操作list练习

# 4-1 比萨:想出至少三种你喜欢的比萨,将其名称存储在一个列表中,再使用 for 循环将每种比萨的名称都打印出来。
# 修改这个 for 循环,使其打印包含比萨名称的句子,而不仅仅是比萨的名称。
# 对于每种比萨,都显示一行输出,如“I like pepperoni pizza”。
# 在程序末尾添加一行代码,它不在 for 循环中,指出你有多喜欢比萨。
# 输出应包 含针对每种比萨的消息,还有一个总结性句子,如“I really love pizza!”。
pizzas = ['大葱肉末披萨', '宫保鸡丁披萨', '韭菜鸡蛋披萨']
for pizza in pizzas:
    print("%s I like pepperoni pizza" % pizza)
print("I really love pizza!")

# 4-2 动物:想出至少三种有共同特征的动物,将这些动物的名称存储在一个列表中, 再使用 for 循环将每种动物的名称都打印出来。
# 修改这个程序,使其针对每种动物都打印一个句子,如“A dog would make a great pet”。
# 在程序末尾添加一行代码,指出这些动物的共同之处,如打印诸如“Any of these animals would make a great pet!”这样的句子。
bears = ['熊猫', '北极熊', '棕熊']
for bear in bears:
    print("%s真可爱!" % bear)
print("但它们也很凶猛!")
