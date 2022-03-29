class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a=a[::-1]
        b=b[::-1]
        num = 0
        for i in range(len(a)):
            if a[i] == '1':
                num += 2**i
            number_a = num
        num = 0
        for i in range(len(b)):
            if b[i] == '1':
                num += 2**i
            number_b = num
        number_c = number_a + number_b
        if number_c == 0 or number_c == 1 : return str(number_c)
        if number_c % 2 == 1 : number_c -= 1; answer = '1'
        else : answer = '0'    
        x= 2
        while x <= number_c:
            x = x*2
            alpha = (number_c%x) // (x//2) 
            answer = str(alpha) + answer
            number_c = number_c - alpha * (x//2)

        return( answer)
                