class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ret = []
        for num in range(1, n + 1):
            mul_of_3 = False
            mul_of_5 = False
            if num%3 == 0:
                mul_of_3 = True
            if num%5 == 0:
                mul_of_5 = True
            if mul_of_3 and mul_of_5:
                ret.append("FizzBuzz")
            elif mul_of_3:
                ret.append("Fizz")
            elif mul_of_5:
                ret.append("Buzz")
            else:
                ret.append(str(num))
        return ret