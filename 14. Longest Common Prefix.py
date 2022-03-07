class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        n=len(strs)
        if n == 1:
            return strs[0]
        else:
            i=0
            a=True
            temp=''
            while a:
                try:
                    x=strs[0][i]
                    for k in range(1,n):
                        if x == strs[k][i]:
                            if k <n-1:continue
                            elif k==n-1 : temp += x;i+=1 
                        else : a=False;break
                except:
                    a=False
            return temp