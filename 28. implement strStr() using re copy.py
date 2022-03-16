import re

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        a=-1
        if needle:
            p = re.compile(needle)
            y=p.search(haystack)
            if y : a= y.start()
            else : a= -1
        else:
            a=0
        return a