# The product difference between two pairs (a, b) and (c, d) is defined as (a * b) - (c * d).

# For example, the product difference between (5, 6) and (2, 7) is (5 * 6) - (2 * 7) = 16.

# Given an integer array nums, choose four distinct indices w, x, y, and z such that the product difference between pairs (nums[w], nums[x]) and (nums[y], nums[z]) is maximized.

# Return the maximum such product difference.

class Solution(object):
    def maxProductDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_1 = 0
        max_2 = 0
        min_1 = float('inf')
        min_2 = float('inf')
        for num in nums:
            if num > max_1:
                max_2 = max_1
                max_1 = num
            elif num > max_2:
                max_2 = num

            if num < min_1:
                min_2 = min_1
                min_1 = num
            elif num < min_2:
                min_2 = num
        print("max1",max_1)
        print("max2",max_2)
        print(min_1)
        print(min_2)
        return ((max_1*max_2)-(min_1*min_2))
