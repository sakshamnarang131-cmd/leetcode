class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_list = s.split()
        a = {}
        result = []
        for i in range(len(s_list)):
            a[i] = s_list[i][-1]
            s_list[i] = s_list[i][:-1]
        a_sorted = sorted(a, key=a.get)
        for i in range(len(a_sorted)):
            result.append(s_list[a_sorted[i]])
        return " ".join(result)
