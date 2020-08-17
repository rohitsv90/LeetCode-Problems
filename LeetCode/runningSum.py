class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        run_sum = 0
        new_nums = []
        for i in nums:
            run_sum += i
            new_nums.append(run_sum)
        return new_nums