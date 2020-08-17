class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_dict = dict()
        for number in nums:
            if number in nums_dict:
                nums_dict[number] += 1
            else:
                nums_dict[number] = 1
        for key, val in nums_dict.items():
            if val == 1:
                return key
            