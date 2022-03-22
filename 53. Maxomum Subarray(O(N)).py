class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        n = len(nums)
        local_maximum = global_maximum = nums[0]
        for i in range(1,n):
            local_maximum += nums[i]
            if local_maximum <= 0 : local_maximum =0
            if global_maximum < local_maximum : global_maximum = local_maximum
        return global_maximum
''' 

note

Suppose that A is the given array and B is the subarray.
Then B starts with A[0] or A[i].

1) B starts with A[0]

S(i)=A[0] + ... + A[i] should touch the maximum value as i getting larger by 1. 

In this case, local sum is equal to the global sum.

2) B starts with A[i]

Then for any partial sum from C = A[j], ... , A[i-1] has negative value because C+B < B. 

In this case, local sum is refreshed and started with index i. In particular, the last maximum partial sum is recorded as the global sum.
For instance, A=[3, -4, 5]

A[0] -> 3
A[1] -> -4
A[2] -> 5
A[0,1] -> -1
A[1,2] -> 1
A[0,1,2] -> 4 

----- answer : A[2], which maximum is 5.

local sum starting from initial index is 3, and at the next index it touches below 0. Thus it is initialized, as long as non-positive value appearing.
If positive value has came, then the partial sum counts again. It records local sum again, and compares to the global sum.

So, local sum always represents the 'possible subarray having positive sum', and global sum is the max amongst.

---- 
The key idea lies in the characteristic of the maximum subarray. Wherever it starts, the number previous the subarray should be non-positive (or it is the intial index).
Even more, the sum of a subarray before the maximum subarray has non-positive value. 

If a subarray has positive sum and has a gap from the maximum subarray, then you shoud hvae stored the sum of a subarray and compared it to the maximum subarray.




'''