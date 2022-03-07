class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        memory={}
        for i in range(n):
            m=target
            k=nums[i]
            m=m-k
            if m in memory: return [memory[m],i]
            else: memory[k]=i
