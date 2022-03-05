class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n=len(nums)
        m=target
        for i in range(n):
            for j in range(i+1,n):
                k=nums[i]+nums[j]
                if k==m:return [i,j]
                else:continue
