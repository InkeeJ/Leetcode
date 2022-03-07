class Solution:
    def isValid(self, s: str) -> bool:
        temp=s[0]
        n=len(s)
        if n%2 ==1 : return False
        for letter in s[1:]:
            if letter in {'{','(','['}: temp += letter
            else:
                if not temp: return False
                elif temp[-1] == '{': 
                    if letter == '}': temp=temp[:-1]
                    else : return False
                elif temp[-1]=='[':
                    if letter == ']' : temp = temp[:-1]
                    else : return False
                elif temp[-1]=='(':
                    if letter == ')' : temp = temp[:-1]
                    else : return False
        if temp : return False
        return True
