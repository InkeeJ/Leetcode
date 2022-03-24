'''
faster answer
'''

class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        digits = list(map(int,' '.join(str(int(''.join(list(map(str,digits))))+1)).split()))
        return digits

'''
slower answer
'''

class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        count=0
        for i in digits.__reversed__():
            if i != 9 : break
            else : count +=1 #.... 899 -> 2, ...123 -> 9, 999 -> 3
        if count != 0 and count != len(digits):
            digits[-(count+1)] +=1 
            digits[-count:] = count*[0]
        elif count == len(digits):
            digits.append(0)
            digits[:-1] = [0]*count
            digits[0] = 1
        else :
            digits[-1] +=1
        return digits