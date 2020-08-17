class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_dict = dict()
        for num in nums:
            if num in nums_dict:
                nums_dict[num] += 1
            else:
                nums_dict[num] = 1
        for k, v in nums_dict.items():
            majority_key = max(nums_dict.keys(), key=nums_dict.get)
        return majority_key