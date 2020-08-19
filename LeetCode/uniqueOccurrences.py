class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        unique_dict = {}
        for i in arr:
            if i in unique_dict:
                unique_dict[i] += 1
            else:
                unique_dict[i] = 1
        unique_arr = []
        for k, v in unique_dict.items():
            if v in unique_arr:
                return False
            else:
                unique_arr.append(v)
        return True