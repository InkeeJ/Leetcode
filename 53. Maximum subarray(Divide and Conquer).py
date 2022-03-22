def mca(A,start,end): #maximum crossing array
    left = right = -(10**4)
    n=end-start
    mid = n//2
    for i in range(mid+1):
        x = sum(A[start+i:start+mid]) 
        if left < x: 
            left = x
    for j in range(mid,n):
        x = sum(A[start+mid:start+j]) #start + end - start  = end  
        if right < x:
            right = x
    return left+right
def combinestep_maximum(nums,L_start,Lmax,R_end,Rmax):
    
    crossing_max = mca(nums,L_start,R_end)
    return (max(Lmax,Rmax,crossing_max),L_start,R_end)
def MaxSubArray(A,start,end) :
    if end-start == 1:
        L_start = start
        R_end = end
        return (A[start], L_start, R_end) 
    else:
        mid = (end-start) //2    
        (L_Value, L_start, L_end)=MaxSubArray(A,start,start+mid)
        (R_Value, R_start, R_end)=MaxSubArray(A,start+mid,end)
        crossing_value = mca(A, L_start, R_end)
        return (max(L_Value, R_Value, crossing_value), L_start, R_end)
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        end = len(nums)
        return MaxSubArray(nums, 0 , end)[0]