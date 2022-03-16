class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        a=-1
        if needle:
            n=len(needle)
            m=len(haystack)
            if m<n: a=-1
            elif m==n:
                if needle==haystack : a=0
                else : a=-1
            else:
                for i in range(m-n+1):
                    if haystack[i:n+i]==needle : a=i;break
                    else:continue
        else:
            a=0
        return a

#it would be better...