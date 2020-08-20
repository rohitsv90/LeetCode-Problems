class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        N = len(A)
        result = [None] * N
        
        even = 0
        for i, n in enumerate(A):
            if n % 2 == 0:
                result[even] = n
                even += 2
        odd = 1
        for i, n in enumerate(A):
            if n % 2 == 1:
                result[odd] = n
                odd += 2
        return result