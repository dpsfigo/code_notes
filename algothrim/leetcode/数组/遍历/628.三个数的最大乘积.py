'''
Author: dpsfigo
Date: 2024-02-05 10:52:10
LastEditors: dpsfigo
LastEditTime: 2024-02-05 13:18:51
Description: 请填写简介
'''
'''
给你一个整型数组 nums ，在数组中找出由三个数组成的最大乘积，并输出这个乘积。

 

示例 1：

输入：nums = [1,2,3]
输出：6
示例 2：

输入：nums = [1,2,3,4]
输出：24
示例 3：

输入：nums = [-1,-2,-3]
输出：-6
 

提示：

3 <= nums.length <= 104
-1000 <= nums[i] <= 1000
'''
class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        sorted(nums)
        n = len(nums)
        return max(nums[0]*nums[1]*nums[n-1], nums[n-3]*nums[n-2]*nums[n-1])

if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,3,4]
    ret = sol.maximumProduct(nums)
    print(ret)
