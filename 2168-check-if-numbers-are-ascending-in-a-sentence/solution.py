class Solution(object):
    def areNumbersAscending(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a = []
        s_list = s.split()
        for i in range(len(s_list)):
            if s_list[i].isdigit():
                a.append(int(s_list[i]))
        return a == sorted(a) and len(a) == len(set(a))
