class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_1 = 0
        #index_2 = index_1+1
       
        while index_1 < len(nums)-1:
            for index_2 in range(index_1 +1,len(nums)):
                added =  nums[index_1] + nums[index_2]
                if added == target:
                    return [index_1,index_2]
                    break
                else:
                    index_2 +=1
            index_1 +=1
            
        