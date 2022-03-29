class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n = len(a)
        m = len(b)
        k = min(n,m)
        temp = '0'
        t=-1
        c= ''
        i=1
        if n == 0 : return b
        if m == 0 : return a
        while i<=k:
            if a[t] == 1 and a[t] == b[t]:
                c = temp + c
                temp = '1'
                
            elif a[t] == 0 and a[t] == b[t]:
                c = temp + c
                temp = '0'
            else:
                if temp == '1':
                    c = '0' + c
                    temp = '0'
                else :
                    c = '1' + c
            i += 1
            t -= 1
        

            
