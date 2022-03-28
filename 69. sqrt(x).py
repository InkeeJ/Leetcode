'''
very slow
'''

class Solution:
    def mySqrt(self, x: int) -> int:
        n=0
        while True:
            if n*n <= x < (n+1)*(n+1) : break
            else : n +=1
        return n

'''
faster
'''

class Solution:
    def mySqrt(self, x: int) -> int:
        n=0
        while True:
            if x - (n+1)*(n+1)<0 : break
            else : n +=1
        return n

'''
faster

'''
class Solution:
    def mySqrt(self, x: int) -> int:
        n=0
        if x == 0 or x == 1 : return x
        while True:
            if x - 2**(n+1)<0 : break # 2^n <= x < 2^(n+1)
            else : n +=1
        k = n//2
        m = 2**k
        while True:
            if x - (m+1)*(m+1) <0 : break
            else : m +=1
        return m
'''
binary search method. much faster
'''
class Solution:
    def mySqrt(self, x: int) -> int:
        l = 1
        r = x
        while l <= r:
            m = (l + r) // 2
            m2 = m ** 2
            if m2 == x:
                return m
            if m2 > x:
                r = m - 1
            else:
                l = m + 1
        return l - 1

'''
similar
'''
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        elif x == 1:
            return 1
        root = x / 2
        eps = 0.00001
        while(root - x / root > eps):
            root = 0.5 * (root + x / root)
        return int(root)


'''
Analyze the last two soln ! 
'''