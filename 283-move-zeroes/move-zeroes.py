class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for number in nums:
            if number == 0:
                nums.pop(nums.index(number))
                nums.insert(len(nums),number)
        return nums