class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums)==1 or nums[-1]==nums[0] : return 1
        else:
            i=0
            nums.append(nums[i])
            while nums[i]<=nums[i+1]:
                if nums[i]<nums[i+1]:nums.append(nums[i+1])
                i+=1
            j=0
            for data in nums[i+1:]:
                nums[j]=data
                j+=1            
        return j
