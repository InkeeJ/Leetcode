def mca(A): #maximum crossing array
    left = right = -(10**4)
    n=len(A)
    mid = n//2
    for i in range(mid):
        x = sum(A[i:mid]) 
        if left < x: 
            left = x
    for j in range(mid+1,n+1):
        x = sum(A[mid:j]) 
        if right < x:
            right = x
    return left+right


def combinestep_maximum(L,Lmax,R,Rmax):
    nums=L+R
    crossing_max = mca(nums)
    return max(Lmax,Rmax,crossing_max)

def MaxSubArray(A):
    n = len(A)
    if n == 1:
        return (A, A[0]) 

    else:
        mid = n //2
     
    # nums = [0,1,2,3] -> len = 4, mid = 2, nums[:mid] = 0,1
    # nums = [0,1,2,3,4] -> len = 5, mid = 2, nums[:mid] = 0,1
    # nums = [0,1] -> len = 2, mid = 1, nums[:mid] = 0
    # nums = [0] -> len = 1, mid = 0, nums[:mid]=[]     
    
        (left, leftmax)=MaxSubArray(A[:mid])
        (right,rightmax)=MaxSubArray(A[mid:])
        return (left+right,combinestep_maximum(left,leftmax,right,rightmax))


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        return MaxSubArray(nums)[1]