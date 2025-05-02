class Solution:
    import math
    def isPowerOfTwo(self, n: int) -> bool:
        '''loger =  math.log(n,2)
        if int(loger) == loger:
            return True
        return False'''
        return n > 0 and (n & (n - 1) == 0)
        