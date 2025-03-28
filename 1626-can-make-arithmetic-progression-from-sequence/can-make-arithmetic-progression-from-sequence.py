class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()  
        if len(arr) == 2:
            return True
    
        common_difference = arr[1] - arr[0]
        for i in range(1, len(arr) - 1):
            if arr[i + 1] - arr[i] != common_difference:
                return False
        return True

        