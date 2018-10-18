#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 下一个排列.py
"""
实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

必须原地修改，只允许使用额外常数空间。

以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""
"""
思路：从后往前取出数字，然后从这个数字的后一个数字开始，从前往后比较，找出大于取出数字的最小数字。将两个数字交换。
然后把第一个数字的后一个位置开始全部倒序。
"""
__author__ = 'Aiyane'
import profile

class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        i = l-1
        
        while i >= 0:
            j = i + 1
            index = None
            while j < l and nums[i] < nums[j]:
                if index is None or nums[j] <= nums[index]:
                    index = j
                j += 1
            if index:
                nums[i], nums[index] = nums[index], nums[i]
                nums[i+1:] = nums[i+1:][::-1]
                return None
            i -= 1
        nums.reverse()

def main():
    sol = Solution()
    print(sol.nextPermutation([9,8,3,10,9,8,7,2,1]))
    print(sol.nextPermutation([9,8,3,6,5,4,7,6,5,2,1]))
    print(sol.nextPermutation([2,3,1,3,3]))
    print(sol.nextPermutation([1,1,5]))

if __name__ == '__main__':
    # profile.run('main()')
    main()
