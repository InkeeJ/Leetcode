dict={"I":1, "V":5, "X":10, "L":50, 'C':100, 'D':500, 'M':1000}

class Solution:
    def romanToInt(self, s: str) -> int:
        answer=0
        for i in range(len(s)-1):
            if dict[s[i]]>=dict[s[i+1]]:
                answer += dict[s[i]]
            else:
                answer -= dict[s[i]]
        answer += dict[s[-1]]
        return answer