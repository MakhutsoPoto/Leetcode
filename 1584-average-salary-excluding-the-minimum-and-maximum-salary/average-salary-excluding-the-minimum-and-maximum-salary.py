class Solution:
    def average(self, salary: List[int]) -> float:
        salary.remove(min(salary))
        salary.remove(max(salary))
        final = sum(salary)/len(salary)
        return final
    
        