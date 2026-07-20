class Solution(object):
    def countTime(self, time):
        """
        :type time: str
        :rtype: int
        """
        s = list(time)
        count = 0
        if "?" not in s:
            return 1
        if s[0] == "?" and s[1] == "?":
            count += 24
        elif s[0] == "?":
            if int(s[1]) < 4 :
                count += 3
            else:
                count += 2
        elif s[1] == "?":
            if s[0] == "2":
                count += 4
            else:
                count += 10
        if s[3] == "?":
            if count != 0:
                count *= 6
            else:
                count+=6
        if s[4] =="?":
            if count != 0:
                count *= 10
            else:
                count+=10
        
        return count
