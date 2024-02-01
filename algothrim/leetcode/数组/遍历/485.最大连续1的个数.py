'''
Author: dpsfigo
Date: 2024-02-01 10:54:08
LastEditors: dpsfigo
LastEditTime: 2024-02-01 11:00:31
Description: 请填写简介
'''
'''
给定一个二进制数组 nums ， 计算其中最大连续 1 的个数。

 

示例 1：

输入：nums = [1,1,0,1,1,1]
输出：3
解释：开头的两位和最后的三位都是连续 1 ，所以最大连续 1 的个数是 3.
示例 2:

输入：nums = [1,0,1,1,0,1]
输出：2
 

提示：

1 <= nums.length <= 105
nums[i] 不是 0 就是 1.
'''
class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        max_cnt, cnt = 0, 0
        for i in range(len(nums)):
            if nums[i] == 1:
                cnt += 1
            else:
                max_cnt = max(max_cnt, cnt)
                cnt = 0
        max_cnt = max(max_cnt,cnt)
        return max_cnt

if __name__ == "__main__":
    nums = [1,0,1,1,0,1]
    sol = Solution()
    max_cnt = sol.findMaxConsecutiveOnes(nums)
    print(max_cnt)