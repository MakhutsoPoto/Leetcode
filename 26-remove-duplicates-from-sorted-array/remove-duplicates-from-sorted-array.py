class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        k = 1  
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:  
                nums[k] = nums[i] 
                k += 1 
        
        return k

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        ''' uniques = []
            nums = set(nums)
            k = len(nums)
            return k'''




        '''for num in nums:
            if num not in uniques:
                uniques.append(num)
            continue
        return len(uniques)'''