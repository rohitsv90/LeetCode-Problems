class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        new_arr = []
        for i in range(len(arr) - 1):
            right = max(arr[i + 1:])
            new_arr.append(right)
        new_arr.append(-1)
        return new_arr