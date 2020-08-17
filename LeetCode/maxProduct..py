class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = 0
        for num in nums:
            if num > i:
                j = i
                i = num
            elif num > j:
                j = num
        return (i - 1) * (j - 1)