class Solution(object):
    def maximumTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        s = list(time)
        if s[0] == "?" and s[1] == "?":
            s[0] = "2"
            s[1] = "3"
        elif s[0] == "?":
            if int(s[1]) < 4 :
                s[0] = "2"
            else:
                s[0] = "1"
        elif s[1] == "?":
            if s[0] == "2":
                s[1] = "3"
            else:
                s[1] = "9"
        if s[3] == "?":
            s[3] = "5"
        if s[4] =="?":
            s[4] = "9"
        return "".join(s)
