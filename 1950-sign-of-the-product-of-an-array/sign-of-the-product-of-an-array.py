class Solution:
    import math
    def arraySign(self, nums: List[int]) -> int:
        product = math.prod(nums)
        x = product
        if x == 0:
            return 0
        elif x > 0:
            return 1
        elif x < 0:
            return -1
        