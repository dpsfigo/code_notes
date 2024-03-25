'''
Author: dpsfigo
Date: 2024-03-25 11:26:14
LastEditors: dpsfigo
LastEditTime: 2024-03-25 11:35:14
Description: 请填写简介
'''
'''
给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。


示例 1:

输入: nums = [-1,0,3,5,9,12], target = 9
输出: 4
解释: 9 出现在 nums 中并且下标为 4
示例 2:

输入: nums = [-1,0,3,5,9,12], target = 2
输出: -1
解释: 2 不存在 nums 中因此返回 -1
 

提示：

你可以假设 nums 中的所有元素是不重复的。
n 将在 [1, 10000]之间。
nums 的每个元素都将在 [-9999, 9999]之间。
'''

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) -1
        while left <= right:
            middle = int((left+right)/2)
            num = nums[middle]
            if num < target:
                left = middle + 1
            elif num > target:
                right = middle -1
            else:
                return middle
        return -1

        

if __name__ == "__main__":
    sol = Solution()
    nums = [-1,0,3,5,9,12]
    target = 2
    ret = sol.search(nums, target)
    print(ret)
