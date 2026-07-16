class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        l1 = list(s)
        n = len(l1)
        i = 0
        while i<n :
            if l1[i] != " ":
                break
            else:
                l1.remove(" ")
                n -= 1
        
        l2 = []
        temp = 1
        try:
            for i in range (0,n):
                if i == 0 and l1[i] == "-":
                    temp = -1
                elif i == 0 and l1[i] == "+":
                    temp = 1
                else:
                    l2.append(int(l1[i]))
        except Exception as e:
            pass
        n = len(l2)
        f = 0
        for i in range (0,n):
            f += (l2[i]*(10**(n-1-i)))
        final = temp * f
        if final < -1*(2**31):
            final = -1*(2**31)
        elif final > (2**31) - 1:
            final = (2**31) - 1
        return final
