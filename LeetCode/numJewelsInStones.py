class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        result = []
        for i in S:
            if i in J:
                result.append(i)
        return len(result)
                