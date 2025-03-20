class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        import math
        if -2**31 <= dividend and  divisor <= 2**31 - 1:
            try :
                ans = dividend/divisor
                if dividend == -2147483648 and divisor == -1:
                    return 2147483647 
                if ans< 0:
                    return math.ceil(ans)
                else:
                    return math.floor(ans)

            except ZeroDivisionError:
                return
        