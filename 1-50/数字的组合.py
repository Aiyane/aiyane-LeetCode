#!/usr/bin/env/python3
# -*- coding: utf-8 -*-
# 数字的组合.py
"""
自己出的题
数字的组合: 输出一个数字的全部和式的列表, 例如:
输入: 4
输出: 
[
[4], 
[3, 1], 
[2, 2], 
[2, 1, 1], 
[1, 3], 
[1, 2, 1], 
[1, 1, 2], 
[1, 1, 1, 1]
]
"""
"""
思路: 利用树的深度优先遍历, 左子树表示当前数增加, 右子树表示append一个1, 当tem内所有数之和为n时停止.
"""


def dfa(n, l, r, tem, res):
    if l + r < n:
        return res

    if l + r == n:
        res.append(tem)
    else:
        if l == n == r:
            tem.append(1)
            l -= 1
        if l > 0:
            lt = tem.copy()
            lt[-1] += 1
            res = dfa(n, l-1, r, lt, res)
        if r > 0:
            rt = tem.copy()
            rt.append(1)
            res = dfa(n, l, r-1, rt, res)
    return res


def main(n):
    print(dfa(n, n, n, [], []))


if __name__ == '__main__':
    main(4)
