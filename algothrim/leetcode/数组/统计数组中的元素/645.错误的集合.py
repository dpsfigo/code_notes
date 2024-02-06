'''
Author: dpsfigo
Date: 2024-02-05 14:41:35
LastEditors: dpsfigo
LastEditTime: 2024-02-06 14:59:25
Description: 请填写简介
'''
'''
集合 s 包含从 1 到 n 的整数。不幸的是，因为数据错误，导致集合里面某一个数字复制了成了集合里面的另外一个数字的值，导致集合 丢失了一个数字 并且 有一个数字重复 。

给定一个数组 nums 代表了集合 S 发生错误后的结果。

请你找出重复出现的整数，再找到丢失的整数，将它们以数组的形式返回。

 

示例 1：

输入：nums = [1,2,2,4]
输出：[2,3]
示例 2：

输入：nums = [1,1]
输出：[1,2]
 

提示：

2 <= nums.length <= 104
1 <= nums[i] <= 104
'''

class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        err_nums = [0,0]
        data = {}
        for num in nums:
            if num in data:
                data[num] += 1
            else:
                data[num] = 1
        for i in range(len(nums)):
            if i+1 in data:
                if data[i+1] == 2:
                    err_nums[0] = i+1
            else:
                err_nums[1] = i+1
        return err_nums
            
if __name__ == "__main__":
    sol = Solution()
    nums = [2,2]
    ret = sol.findErrorNums(nums)
    print(ret)

