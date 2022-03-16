class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
            # nums.remove(val) you can use this but..

            # remove, an attribution of list data structure is faster than I did on this code. 
            
            if not nums: return 0
            j=len(nums)-1
            i=0
            while i <j:
                if nums[j]==val: j = j-1
                elif nums[i]==val: nums[j],nums[i]=nums[i],nums[j]
                else:i+=1
            if nums[i]==val : return i
            if nums[i] != val : return i+1
            
                

