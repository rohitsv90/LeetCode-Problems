class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """

        new_list = []
        for num in A:
            num = num*num
            new_list.append(num)
        return sorted(new_list)
        