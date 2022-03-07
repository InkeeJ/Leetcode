class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n=len(nums)
        memory={}
        for i in range(n):
            m=target
            k=nums[i]
            m=m-k
            if m in memory: return [memory[m],i]
            else: memory[k]=i
