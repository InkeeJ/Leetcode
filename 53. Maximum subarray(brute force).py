class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        n=len(nums)
        temp=-(10**4)
        for i in range(n):
            for j in range(n-1,i-1,-1):
                x=sum(nums[i:j+1])
                if temp < x : temp = x
        return temp
                

 
#This code has O(n^2) time complexity so that it turns out to be "limited time exceeded"
